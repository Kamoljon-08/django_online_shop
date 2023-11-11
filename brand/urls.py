from django.urls import path
from .views import (
    BrandListView,
    BrandCreateView,
    BrandDetailView,
    BrandUpdateView,
    BrandDeleteView,
)

urlpatterns = [
    path('list/', BrandListView.as_view(), name='brand_list'),
    path('create/', BrandCreateView.as_view(), name='brand_create'),
    path('detail/<int:pk>/', BrandDetailView.as_view(), name='brand_detail'),
    path('update/<int:pk>/', BrandUpdateView.as_view(), name='brand_update'),
    path('delete/<int:pk>/', BrandDeleteView.as_view(), name='brand_delete'),
]