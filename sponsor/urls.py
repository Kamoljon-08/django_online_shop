from django.urls import path
from .views import (
    SponsorListView,
    SponsorCreateView,
    SponsorDetailView,
    SponsorUpdateView,
    SponsorDeleteView,
)

urlpatterns = [
    path('list/', SponsorListView.as_view(), name='sponsor_list'),
    path('create/', SponsorCreateView.as_view(), name='sponsor_create'),
    path('detail/<int:pk>/', SponsorDetailView.as_view(), name='sponsor_detail'),
    path('update/<int:pk>/', SponsorUpdateView.as_view(), name='sponsor_update'),
    path('delete/<int:pk>/', SponsorDeleteView.as_view(), name='sponsor_delete'),
]