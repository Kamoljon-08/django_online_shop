from django.urls import path
from .views import (
    FaqListView,
    FaqCreateView,
    FaqDetailView,
    FaqDeleteView,
    FaqUpdateView,
    UserFaqListView,
)

urlpatterns = [
    path('', UserFaqListView.as_view(), name='faq'),
    path('list/', FaqListView.as_view(), name='faq_list'),
    path('create/', FaqCreateView.as_view(), name='faq_create'),
    path('delete/<int:pk>/', FaqDeleteView.as_view(), name='faq_delete'),
    path('detail/<int:pk>/', FaqDetailView.as_view(), name='faq_detail'),
    path('update/<int:pk>/', FaqUpdateView.as_view(), name='faq_update'),
]