from typing import Any
from .models import BasketModel
from users.models import CustomUser
from brand.models import BrandModel
from config.views import sort_product
from category.models import CategoryModel
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from product.models import ProductModel, ProductSizeModel, ProductColorModel
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

class BasketListView (ListView):
    template_name = 'user/cart.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        basket = BasketModel.objects.filter(is_delete=False)
        product_colors = ProductColorModel.objects.filter(block=False)
        product_sizes = ProductSizeModel.objects.filter(block=False)

        return render(request, self.template_name, {
                'baskets': basket,
                'product_sizes': product_sizes,
                'product_colors': product_colors,
            })

class BasketCreateView (TemplateView):
    model = BasketModel
    template_name = 'index.html'

    def get(self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        get_product = ProductModel.objects.filter(block=False, pk=pk).first()
        get_basket = BasketModel.objects.filter(is_delete=False, product=get_product).first()

        if get_basket is not None:
            get_basket.count = get_basket.count + 1
            get_basket.price = get_basket.price + get_product.sale_price

            get_basket.save()

        else:
            BasketModel.objects.create(
                count = 1,
                user = request.user,
                product = get_product,
                price = get_product.sale_price,
            )
            return redirect('/login/')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class BasketDetailView (DetailView):
    pass

class BasketUpdateView (UpdateView):
    model = BasketModel
    template_name = 'user/index.html'

    def get(self, request: HttpRequest, pk, *args: str, **kwargs: Any) -> HttpResponse:
        product_colors = ProductColorModel.objects.filter(block=False, pk=pk).first()
        product_sizes = ProductSizeModel.objects.filter(block=False, pk=pk).first()
        product = ProductModel.objects.filter(block=False, pk=product_colors.product.pk).first()
        baskets = BasketModel.objects.filter(is_delete=False, product=product).first()

        if baskets is not None:
            baskets.color = product_colors
            baskets.sizes = product_sizes
            baskets.save()
        
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class BasketDeleteView (DeleteView):
    model = BasketModel
    template_name = 'user/index.html'

    def get(self, request: HttpRequest, pk, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            basket = BasketModel.objects.filter(pk=pk).first()
            basket.delete()
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return redirect('/404/')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')