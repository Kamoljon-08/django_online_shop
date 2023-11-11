from django.urls import path
from .views import (
    AdListView,
    AdCreateView,
    AdDetailView,
    AdUpdateView,
    AdDeleteView,
)

urlpatterns = [
    path('list/', AdListView.as_view(), name='ad_list'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('detail/<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('update/<int:pk>/', AdUpdateView.as_view(), name='ad_update'),
    path('delete/<int:pk>/', AdDeleteView.as_view(), name='ad_delete'),
]