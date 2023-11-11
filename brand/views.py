from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import BrandModel
from .forms import BrandForm
from django.http import HttpRequest, HttpResponse
from typing import Any

# Create your views here.

class BrandListView (ListView):
    model = BrandModel
    context_object_name = 'brands'
    template_name = 'admin/brands/admin_brand_list.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class BrandCreateView (CreateView):
    form_class = BrandForm
    template_name = 'admin/brands/admin_brand_create.html'

    def form_valid (self, form):
        form.save()
        return super(BrandCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class BrandDetailView (DetailView):
    model = BrandModel
    context_object_name = 'brand'
    template_name = 'admin/brands/admin_brand_detail.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class BrandUpdateView (UpdateView):
    model = BrandModel
    template_name = 'admin/brands/admin_brand_update.html'
    fields = ('title', 'block', 'image')
    success_url = '/brand/list/'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class BrandDeleteView (DeleteView):
    model = BrandModel
    template_name = 'admin/brands/admin_brand_delete.html'
    success_url = reverse_lazy('brand_list')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')