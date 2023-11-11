"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from .views import (
    homeView,
    cartView,
    aboutView,
    contactView,
    productView,
    wishlistView,
    checkoutView,
    PageView,
    productDetailView,
    Sort_Category_Products
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_panel/', PageView.as_view(), name='admin_panel'),

    path('ad/', include('ad.urls')),
    path('faq/', include('faq.urls')),
    path('blog/', include('blog.urls')),
    path('user/', include('users.urls')),
    path('about/', include('about.urls')),
    path('brand/', include('brand.urls')),
    path('sponsor/', include('sponsor.urls')),
    path('product/', include('product.urls')),
    path('category/', include('category.urls')),
    path('basket/', include('basket.urls')),
    path('notification/', include('notification.urls')),
    path('order/', include('order.urls')),

    path('', homeView.as_view(), name='index'),
    path('cart/', cartView.as_view(), name='cart'),
    path('user/', include('django.contrib.auth.urls')),
    path('contact/', contactView.as_view(), name='contact'),
    path('product/', productView.as_view(), name='product'),
    path('wishlist/', wishlistView.as_view(), name='wishlist'),
    path('checkout/', checkoutView.as_view(), name='checkout'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('<str:title>/', Sort_Category_Products, name='category_products'),


    path('product/detail/', productDetailView.as_view(), name='product_detail'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
