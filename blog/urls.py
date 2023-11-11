from django.urls import path
from .views import (
    UserBlogList,
    UserBlogDetail,

    BlogListView,
    BlogCreateView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,

    BlogImageCreateView,
    BlogImageDetailView,
    BlogImageUpdateView,
    BlogImageDeleteView,

    BlogCommentCreateView,
    BlogCommentUpdateView,
    BlogCommentDeleteView,
)

urlpatterns = [
    path('', UserBlogList.as_view(), name='blog'),
    path('user/detail/<int:pk>/', UserBlogDetail.as_view(), name='detail'),

    path('list/', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

    path('image/create/<int:pk>/', BlogImageCreateView.as_view(), name='blog_image_create'),
    path('image/detail/<int:pk>/', BlogImageDetailView.as_view(), name='blog_image_detail'),
    path('image/update/<int:pk>/', BlogImageUpdateView.as_view(), name='blog_image_update'),
    path('image/delete/<int:pk>/', BlogImageDeleteView.as_view(), name='blog_image_delete'),

    path('comment/create/<int:pk>', BlogCommentCreateView.as_view(), name='blog_comment_create'),
    path('comment/update/<int:pk>', BlogCommentUpdateView.as_view(), name='blog_comment_update'),
    path('comment/delete/<int:pk>', BlogCommentDeleteView.as_view(), name='blog_comment_delete'),
]