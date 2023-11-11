from django.views.generic import TemplateView, View, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseRedirect
from typing import Any
from django.views.generic.edit import FormView
from order.forms import OrderCreateForm 
from basket.models import BasketModel
from ad.models import AdModel
from product.models import (
    ProductModel,
    ProductSizeModel,
    ProductLikeModel,
    ProductColorModel,
    ProductImageModel,
    ProductRatingModel,
)
from django.core.serializers import serialize
import json
from category.models import CategoryModel

def find_top_product (ProductModel, ProductLikeModel) -> list:
        all_products = ProductModel.objects.filter(block=False)
        get_id_count = []
        sort_top_product = []
        for i in all_products:
            all_products_likes = ProductLikeModel.objects.filter(product=i.id, block=False)
            count = 0
            for j in all_products_likes:
                count += 1
            get_id_count.append({"id": i.id, "count": count})
        
        get_id_count = sorted(get_id_count, key=lambda x: (-x['count']))

        for i in get_id_count:
            get_detail = ProductModel.objects.filter(id=i['id']).first()
            sort_top_product.append(get_detail)

        return sort_top_product

def sort_product (products):
    return_list = []

    for i in products:
        stars = ProductRatingModel.objects.filter(block=False, product=i)
        likes = ProductLikeModel.objects.filter(block=False, product=i).first()
        images = ProductImageModel.objects.filter(block=False, product=i).order_by('sequence_number')
        
        ProductModel.get_req_card(i, images, stars, likes, return_list)

    return return_list

def get_home (title, request):
    choose_stars = []
    ads = AdModel.objects.filter(block=False).order_by('-created_at')

    take_top_products = find_top_product(ProductModel, ProductLikeModel)
    
    old_products = ProductModel.objects.filter(block=False).order_by('created_at')[:50]
    new_products = ProductModel.objects.filter(block=False).order_by('-created_at')[:50]
    rating_products = ProductRatingModel.objects.filter(block=False).order_by('-stars')[:50]
    super_deals = ProductModel.objects.filter(block=False, super_product=True).order_by('-created_at')

    for i in rating_products: 
        product = ProductModel.objects.filter(block=False, pk=i.product.pk).first()
        choose_stars.append(product)

    sort_old = sort_product(old_products)
    sort_new = sort_product(new_products)
    sort_rated = sort_product(choose_stars)
    sort_super_deals = sort_product(super_deals)
    sort_top_product = sort_product(take_top_products)

    category = CategoryModel.objects.filter(block=False, title=title).first()
    default_category = CategoryModel.objects.filter(block=False).order_by('-created_at').first()
    products = []
    
    if title: products = ProductModel.objects.filter(block=False, category=category).order_by('-created_at')
    else: products = ProductModel.objects.filter(block=False, category=default_category).order_by('-created_at')

    www = sort_product(products)

    sort_top_products = []
    sort_top_products.append(sort_top_product[:5])
    sort_top_products.append(sort_top_product[5:10])

    return render(request, 'user/index.html', 
        {
            'ads': ads,
            'old': sort_old,
            'products': www,
            'new': sort_new,
            'rated': sort_rated,
            'super_deals': sort_super_deals,
            'top_products': sort_top_products, 
        })

def Sort_Category_Products (request, title):
    return_answer = get_home(title, request)
    return return_answer

class homeView (View):
    def get (self, request, *args, **kwargs):
        return_answer = get_home(self.kwargs.get('title'), request)
        return return_answer

class aboutView (TemplateView):
    template_name = 'user/about.html'

class blogView (TemplateView):
    template_name = 'user/blog.html'

class blogDetailView (TemplateView):
    template_name = 'user/blog_detail.html'

class cartView (TemplateView):
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

class contactView (TemplateView):
    template_name = 'user/contact.html'

class faqView (TemplateView):
    template_name = 'user/faq.html'

class checkoutView (FormView):
    form_class = OrderCreateForm
    template_name = 'user/checkout.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(OrderCreateView, self).form_valid(form)

class productView (TemplateView):
    template_name = 'user/product.html'

class productDetailView (TemplateView):
    template_name = 'user/product_detail.html'

class wishlistView (TemplateView):
    template_name = 'user/wishlist.html'

class PageView (TemplateView):
    template_name = 'admin/admin_index.html'


