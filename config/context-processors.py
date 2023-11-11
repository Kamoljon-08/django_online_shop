from typing import Any
from basket.models import BasketModel
from category.models import CategoryModel
from product.models import ProductImageModel
from django.http import HttpRequest, HttpResponse


def context (request):
    product_images = ProductImageModel.objects.filter(block=False)
    basket = BasketModel.objects.filter(is_delete=False).order_by('-created_at')
    all_categories = CategoryModel.objects.filter(block=False).order_by('-created_at')
    total_count = 0
    total_price = 0
    for i in basket:
        total_count = total_count + i.count
        total_price = total_price + i.price

    return {
        'basket': basket,
        'total_count': total_count,
        'total_price': total_price,
        'product_images': product_images,
        'all_categories': all_categories,
        'nav_categories': all_categories[:10],
    }