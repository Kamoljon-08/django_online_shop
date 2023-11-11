from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import CategoryForm
from .models import CategoryModel
from django.http import HttpRequest, HttpResponse
from typing import Any

# Create your views here.

class CategoryListView (ListView):
    model = CategoryModel
    context_object_name = 'categories'
    template_name = 'admin/categories/admin_category_list.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class CategoryCreateView (CreateView):
    form_class = CategoryForm
    template_name = 'admin/categories/admin_category_create.html'

    def form_valid (self, form):
        form.save()
        return super(CategoryCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class CategoryDetailView (DetailView):
    model = CategoryModel
    context_object_name = 'category'
    template_name = 'admin/categories/admin_category_detail.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class CategoryUpdateView (UpdateView):
    model = CategoryModel
    fields = ('title', 'block', 'image')
    template_name = 'admin/categories/admin_category_update.html'
    success_url = '/category/list/'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class CategoryDeleteView (DeleteView):
    model = CategoryModel
    template_name = 'admin/categories/admin_category_delete.html'
    success_url = reverse_lazy('category_list')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')