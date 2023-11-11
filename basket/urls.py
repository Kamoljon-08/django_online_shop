from django.urls import path
from .views import BasketListView, BasketCreateView, BasketDetailView, BasketUpdateView, BasketDeleteView

urlpatterns = [
    path('list/', BasketListView.as_view(), name='basket_list'),
    path('create/<int:pk>/', BasketCreateView.as_view(), name='basket_create'),
    path('detail/<int:pk>/', BasketDetailView.as_view(), name='basket_detail'),
    path('update/<int:pk>/', BasketUpdateView.as_view(), name='basket_update'),
    path('delete/<int:pk>/', BasketDeleteView.as_view(), name='basket_delete'),
]