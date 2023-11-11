from django.urls import path
from .views import (
    NotificationUserView,

    NotificationListView,
    NotificationCreateView,
    NotificationDetailView,
    NotificationUpdateView,
    NotificationDeleteView
)

urlpatterns = [
    path('contact/', NotificationUserView.as_view(), name='contact'),

    path('list/', NotificationListView.as_view(), name='notification_list'),
    path('create/', NotificationCreateView.as_view(), name='notification_create'),
    path('detail/<int:pk>/', NotificationDetailView.as_view(), name='notification_detail'),
    path('update/<int:pk>/', NotificationUpdateView.as_view(), name='notification_update'),
    path('delete/<int:pk>/', NotificationDeleteView.as_view(), name='notification_delete'),
]