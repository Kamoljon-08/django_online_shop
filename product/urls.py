from django.urls import path
from .views import (
    ProductUserList,
    ProductUserDetail,

    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDetailView,
    ProductDeleteView,

    ProductImageCreateView,
    ProductImageUpdateView,
    ProductImageDeleteView,

    ProductCommentCreateView,
    ProductCommentDeleteView,
    ProductCommentUpdateView,

    ProductLikeListView,
    ProductLikeCreateView,
    ProductLikeDeleteView,

    ProductRatingCreateView,

    ProductTagCreateView,
    ProductTagDeleteView,
    ProductTagUpdateView,

    ProductColorCreateView,
    ProductColorDeleteView,
    ProductColorUpdateView,

    ProductSizeCreateView,
    ProductSizeDeleteView,
    ProductSizeUpdateView,

    ProductFilterBrand,
    ProductFilterCategory,
    ProductFilterPrice,
    ProductUserList,
)

urlpatterns = [

    path('list/', ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

    path('list/user/', ProductUserList.as_view(), name='product_list_user'),
    path('detail/user/<int:pk>/', ProductUserDetail.as_view(), name='product_detail_user'),

    path('image/create/<int:pk>/', ProductImageCreateView.as_view(), name='product_image_create'),
    path('image/delete/<int:pk>/', ProductImageDeleteView.as_view(), name='product_image_delete'),
    path('image/update/<int:pk>/', ProductImageUpdateView.as_view(), name='product_image_update'),

    path('comment/create/<int:pk>', ProductCommentCreateView.as_view(), name='product_comment_create'),
    path('comment/delete/<int:pk>', ProductCommentDeleteView.as_view(), name='product_comment_delete'),
    path('comment/update/<int:pk>', ProductCommentUpdateView.as_view(), name='product_comment_update'),

    path('wishlist/', ProductLikeListView.as_view(), name='product_wishlist'),
    path('like/create/<int:pk>', ProductLikeCreateView.as_view(), name='product_like_create'),
    path('like/delete/<int:pk>/', ProductLikeDeleteView.as_view(), name='product_like_delete'),

    path('rating/create/<int:pk>/<int:count>', ProductRatingCreateView.as_view(), name='product_rating_create'),

    path('tag/create/<int:pk>', ProductTagCreateView.as_view(), name='product_tag_create'),
    path('tag/delete/<int:pk>', ProductTagDeleteView.as_view(), name='product_tag_delete'),
    path('tag/update/<int:pk>', ProductTagUpdateView.as_view(), name='product_tag_update'),

    path('color/create/<int:pk>', ProductColorCreateView.as_view(), name='product_color_create'),
    path('color/delete/<int:pk>', ProductColorDeleteView.as_view(), name='product_color_delete'),
    path('color/update/<int:pk>', ProductColorUpdateView.as_view(), name='product_color_update'),

    path('size/create/<int:pk>', ProductSizeCreateView.as_view(), name='product_size_create'),
    path('size/delete/<int:pk>', ProductSizeDeleteView.as_view(), name='product_size_delete'),
    path('size/update/<int:pk>', ProductSizeUpdateView.as_view(), name='product_size_update'),

    path('filter/brand/<str:title>', ProductFilterBrand.as_view(), name='product_filter_brand'),
    path('filter/category/<str:title>', ProductFilterCategory.as_view(), name='product_filter_category'),
    path('filter/price/', ProductFilterPrice.as_view(), name='product_filter_price'),
]