from django.contrib import admin

# Register your models here.

from .models import ProductModel, ProductLikeModel, ProductRatingModel

admin.site.register(ProductModel)
admin.site.register(ProductLikeModel)
admin.site.register(ProductRatingModel)