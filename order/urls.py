from django.urls import path
from .views import (
    UsersOrderListView,

    OrderListView,
    OrderCreateView,
    OrderDetailView,
    OrderUpdateView,
    OrderDeleteView,
)

urlpatterns = [
    path('user/list/', UsersOrderListView.as_view(), name='user_order_list'),

    path('list/', OrderListView.as_view(), name='order_list'),
    path('create/', OrderCreateView.as_view(), name='order_create'),
    path('detail/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDeleteView.as_view(), name='order_delete'),
]