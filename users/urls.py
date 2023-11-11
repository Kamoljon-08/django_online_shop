from django.urls import path
from .views import (
    LoginViews,
    RegisterViews,
    UsersListView,
    UsersDetailView,
    UsersCreateView,
    UsersDeleteView,
    UsersUpdateView,
    UsersResetPasswordView,
    UsersPasswordResetVerifyView,
    UsersPasswordResetCompleteView,
)

urlpatterns = [
    path('login/', LoginViews.as_view(), name='login'),
    path('list/', UsersListView.as_view(), name="user_list"),
    path('register/', RegisterViews.as_view(), name='register'),
    path('create/', UsersCreateView.as_view(), name='user_create'),
    path('detail/<int:pk>/', UsersDetailView.as_view(), name='user_detail'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='user_delete'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='user_update'),
    path('password_reset/', UsersResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/verify/', UsersPasswordResetVerifyView.as_view(),name='password_reset_verify'),
    path('password_reset/complete/<uuid>/<code>/', UsersPasswordResetCompleteView.as_view(),name='password_reset_confirm'),
]