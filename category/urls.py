from django.urls import path
from .views import (
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)
urlpatterns = [
    path('list/', CategoryListView.as_view(), name='category_list'),
    path('create/', CategoryCreateView.as_view(), name='category_create'),
    path('update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]