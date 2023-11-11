from typing import Any
from django.urls import reverse_lazy
from .models import NotificationModel
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import NotificationForm, NotificationtUpdateForm
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

# Create your views here.

class NotificationUserView (TemplateView):
    model = NotificationModel
    form_class = NotificationForm,
    queryset = NotificationModel.objects.all()
    template_name = 'user/contact.html'

    def get (self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        notification = NotificationModel.objects.filter(pk=pk, block=False).first()

        return render (
            request, self.template_name, 
            {
                'notifications': notification,
            },
        )

class NotificationListView (ListView):
    model = NotificationModel
    context_object_name = 'notifications'
    template_name = 'admin/notifications/notification_list.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class NotificationCreateView (FormView):
    model = NotificationModel
    form_class = NotificationForm
    template_name = 'admin/notifications/notification_create.html'
    success_url = '/notification/list/'

    def form_valid (self, form: Any) -> HttpResponse:
        NotificationModel.objects.create(
            user = self.request.user,
            message = form.cleaned_data['message'],
        )

        return super (NotificationCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class NotificationDetailView (DetailView):
    model = NotificationModel
    context_object_name = 'notification'
    template_name = 'admin/notifications/notification_detail.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class NotificationUpdateView (UpdateView):
    model = NotificationModel
    form_class = NotificationtUpdateForm
    template_name = 'admin/notifications/notification_update.html'
    success_url = '/notification/list/'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class NotificationDeleteView (DeleteView):
    model = NotificationModel
    template_name = 'admin/notifications/notification_delete.html'
    success_url = reverse_lazy('notification_list')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')