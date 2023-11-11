from typing import Any
from uuid import uuid4
from random import randint
from .models import CustomUser
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import FormView, ListView, TemplateView, DetailView
from .forms import RegisterForm, UsersUpdateForm, ResetPasswordForm, VerifyForm, ResetPasswordCompleteForm

# Create your views here.

class LoginViews (LoginView):
    template_name = 'user/auth/login.html'
    redirect_authenticated_user = True
    success_url = 'index'

class RegisterViews (FormView):
    template_name = 'user/auth/signup.html'
    form_class = RegisterForm
    # redirect_authenticated_user = True
    success_url = '/user/login'
    
    def form_valid(self, form):
        form.save()
        return super(RegisterViews, self).form_valid(form)
        
class UsersListView (ListView):
    model = CustomUser
    queryset = CustomUser.objects.all()
    template_name = 'admin/users/admin_users_list.html'
    context_object_name = 'users'      

    def get (self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.method == "POST":
            searchSelected = request.POST.get('selected')
            empsearch = CustomUser.objects.filter(last_name=searchSelected) 

            return render (request, 'admin/users/admin_users_list.html', {'users': empsearch})

        else:
            displayemp=CustomUser.objects.all()
            return render (request, 'admin/users/admin_users_list.html', {'users': displayemp})

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersCreateView (CreateView):
    form_class = RegisterForm
    template_name = 'admin/users/admin_users_create.html'
    success_url = '/user/list'    
    
    def form_valid(self, form):
        form.save()
        return super(UsersCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersDeleteView (DeleteView):
    model = CustomUser
    template_name = 'admin/users/admin_users_delete.html'
    success_url = reverse_lazy('user_list')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersUpdateView (UpdateView):
    model = CustomUser
    template_name = 'admin/users/admin_users_update.html'
    fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password', 'image', 'block', 'is_staff', 'is_superuser']
    success_url = '/user/list'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersDetailView (DetailView):
    model = CustomUser
    context_object_name = 'user'
    template_name = 'admin/users/admin_users_detail.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersResetPasswordView (FormView):
    form_class = ResetPasswordForm
    template_name = 'user/auth/password_reset_form.html'
    success_url = '/'

    def form_valid(self, form):
        user = CustomUser.objects.filter(phone=form.cleaned_data['phone']).first()
        if user is not None:
            code = randint(100000, 999999)
            self.request.session['code'] = code
            self.request.session['phone'] = user.phone
            print(code) 
            # send(form.cleaned_data['phone'], code)
            return redirect('/user/password_reset/verify/')
        messages.error(self.request, 'No such number exists:')
        return redirect('/user/password_reset/')

class UsersPasswordResetVerifyView (FormView):
    form_class = VerifyForm
    template_name = 'user/auth/password_reset_verify.html'
    success_url = '/'

    def form_valid(self, form):
        code = self.request.session.get('code')
        if code is None:
            return redirect('/404/')
        if code == form.cleaned_data['phone']:
            uuid = str(uuid4())
            self.request.session['uuid'] = uuid
            return redirect(f'/user/password_reset/complete/{uuid}/{code}/')
        return render(self.request, self.template_name, {'form': form})

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        code = self.request.session.get('code')
        if request.user.is_anonymous and code != None:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class UsersPasswordResetCompleteView (FormView):
    form_class = ResetPasswordCompleteForm
    template_name = "user/auth/password_reset_confirm.html"
    success_url = '/'
    
    def form_valid(self, form):
        code = self.request.session.get('code')
        uuid = self.request.session.get('uuid')
        if str(code) == self.kwargs.get('code') and uuid == self.kwargs.get('uuid'):
            phone = self.request.session['phone']
            user = CustomUser.objects.filter(phone=phone).first()
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.save()
            del self.request.session['code']
            del self.request.session['uuid']
            del self.request.session['phone']
            return render(self.request, 'user/auth/password_reset_complete.html', {})
        return redirect('/404/')

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        code = self.request.session.get('code')
        uuid = self.request.session.get('uuid')
        if str(code) == self.kwargs.get('code') and uuid == self.kwargs.get('uuid'):
            return render(request, self.template_name, {'form': ResetPasswordCompleteForm})
        return redirect('/404/')