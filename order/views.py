from typing import Any
from .models import OrderModel
from users.models import CustomUser
from brand.models import BrandModel
from basket.models import BasketModel
from config.views import sort_product
from product.models import ProductModel
from category.models import CategoryModel
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import OrderCreateForm, OrderUpdateForm

class UsersOrderListView (ListView):
    pass

class OrderListView (ListView):
    model = OrderModel
    template_name = 'admin/orders/order_list.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        order = OrderModel.objects.filter(block=False)

        return render(request, self.template_name, {
                'orders': order,
            })
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class OrderCreateView (FormView):
    form_class = OrderCreateForm
    template_name = 'user/checkout.html'
    success_url = '/'

    # def form_valid(self, form):
    #     print('Hello')
    #     form.save()
    #     return super(OrderCreateView, self).form_valid(form)

        # model = OrderModel
        # form_class = OrderCreateForm
        # template_name = 'user/checkout.html'
        # success_url = '/'

    def form_valid(self, form):
        basket = BasketModel.objects.filter(is_delete=False).order_by('-created_at')
        amount_price = 0
        for i in basket:
            amount_price = amount_price + i.price
        OrderModel.objects.create(
            user=self.request.user,
            total_price=amount_price,
            city=form.cleaned_data['city'],
            country=form.cleaned_data['country'],
            address=form.cleaned_data['address'],
            postcode=form.cleaned_data['postcode'], 
            company_name=form.cleaned_data['company_name'],
        )
        return super(OrderCreateView, self).form_valid(form)

    # def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     if request.user.is_superuser:
    #         return super().dispatch(request, *args, **kwargs)
    #     return redirect('/404/')

class OrderDetailView (DetailView):
    model = OrderModel
    template_name = 'admin/order/order_detail.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class OrderUpdateView (UpdateView):
    model = OrderModel
    template_name = 'admin/order/order_update.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class OrderDeleteView (DeleteView):
    model = OrderModel
    template_name = 'admin/order/order_delete.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')