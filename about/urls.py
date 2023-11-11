from django.urls import path
from .views import (
   UserAboutView,
   AdminAboutView,
   CompanyFileCreateView,
   CompanyFileUpdateView,
   CompanyFileDetailView,
   CompanyFileDeleteView,
    
   CompanyMemberCreateView,
   CompanyMemberDeleteView,
   CompanyMemberDetailView,
   CompanyMemberUpdateView,
)

urlpatterns = [
    path('', UserAboutView.as_view(), name='about'),
    path('list/', AdminAboutView.as_view(), name='about_list'),
    
    path('file/create/', CompanyFileCreateView.as_view(), name='file_create'),
    path('file/delete/<int:pk>', CompanyFileDeleteView.as_view(), name='file_delete'),
    path('file/update/<int:pk>', CompanyFileUpdateView.as_view(), name='file_update'),
    path('file/detail/<int:pk>', CompanyFileDetailView.as_view(), name='file_detail'),

    path('member/create/', CompanyMemberCreateView.as_view(), name='member_create'),
    path('member/update/<int:pk>/', CompanyMemberUpdateView.as_view(), name='member_update'),
    path('member/detail/<int:pk>/', CompanyMemberDetailView.as_view(), name='member_detail'),
    path('member/delete/<int:pk>/', CompanyMemberDeleteView.as_view(), name='member_delete'),
]