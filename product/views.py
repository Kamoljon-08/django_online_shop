import json
import time
from .forms import (
    ProductPriceForm,
    ProductForm,
    ProductUpdateForm,
    
    ProductImageForm,
    ProductImageUpdateForm,

    ProductCommentForm,
    ProductCommentUpdateForm,
    
    ProductTagForm,
    ProductTagUpdateForm,

    ProductColorForm,
    ProductColorUpdateForm,

    ProductSizeForm,
    ProductSizeUpdateForm,)
from .models import (
    ProductModel,
    ProductTagModel,
    ProductLikeModel,
    ProductSizeModel,
    ProductImageModel,
    ProductColorModel,
    ProductRatingModel,
    ProductCommentModel,)
from typing import Any
from random import randrange
from users.models import CustomUser
from brand.models import BrandModel
from django.urls import reverse_lazy
from config.views import sort_product
from category.models import CategoryModel
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse

# Create your views here.

"""
    admin panel for views
"""
class ProductUserList (ListView):
    model = ProductModel
    template_name = 'user/product.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        qqq = []
        www = []
        brands = BrandModel.objects.filter(block=False).order_by('-created_at')
        categories = CategoryModel.objects.filter(block=False).order_by('-created_at')

        min_price = ProductModel.objects.filter(block=False).order_by('sale_price').first()
        max_price = ProductModel.objects.filter(block=False).order_by('-sale_price').first()
        products = ProductModel.objects.filter(block=False)

        sorted_products = sort_product(products)

        for i in brands:
            product_count = ProductModel.objects.filter(block=False, brand=i).count()
            if product_count > 0:
                www.append({'brand': i, 'count': product_count})

        for i in categories:
            product_count = ProductModel.objects.filter(block=False, category=i).count()
            if product_count > 0:
                qqq.append({'category': i, 'count': product_count})

        return render(request, self.template_name,
            {
                'brands': www,
                'prod_categories': qqq,
                'min_price': min_price,
                'max_price': max_price,
                'products': sorted_products
            })

class ProductUserDetail (DetailView):
    model = ProductModel
    form_class = ProductCommentForm,
    queryset = ProductModel.objects.all()
    template_name = 'user/product_detail.html'

    def get (self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        product = ProductModel.objects.filter(pk=pk, block=False).first()
        product_stars = ProductRatingModel.objects.filter(product=pk, block=False)
        product_like = ProductLikeModel.objects.filter(product=pk, block=False).first()
        product_tags = ProductTagModel.objects.filter(product=pk, block=False).order_by('sequence_number')
        product_ratings = ProductRatingModel.objects.filter(product=pk, block=False).order_by('-created_at')
        product_sizes = ProductSizeModel.objects.filter(product=pk, block=False).order_by('sequence_number')
        product_comments = ProductCommentModel.objects.filter(product=pk, block=False).order_by('-created_at')
        product_images = ProductImageModel.objects.filter(product=pk, block=False).order_by('sequence_number')
        product_colors = ProductColorModel.objects.filter(product=pk, block=False).order_by('sequence_number')
        similar_brand = ProductModel.objects.filter(block=False, brand=product.brand.pk).order_by('-created_at')[:60]
        similar_category = ProductModel.objects.filter(block=False, category=product.category.pk).order_by('-created_at')[:60]
        take_stars = ProductModel.get_stars(product_stars)

        get_sorted_brand = sort_product(similar_brand)
        get_sorted_category = sort_product(similar_category)

        ratings_starts = []
        for i in product_ratings:
            get = ProductModel.get_stars([i])
            ratings_starts.append({'stars': get,'ratings': i})

        return render (
            request, self.template_name, 
            {
                'product': product,
                'form': self.form_class,
                'product_stars': take_stars,
                'product_like': product_like,
                'product_tags': product_tags,
                'reviews': len(product_stars),
                'product_sizes': product_sizes,
                'product_colors': product_colors,
                'product_images': product_images,
                'product_ratings': ratings_starts,
                'similar_brands': get_sorted_brand,
                'product_comments': product_comments,
                'similar_categories': get_sorted_category,
            },
        )


class ProductFilterBrand (TemplateView):
    template_name = 'user/product.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        brand = BrandModel.objects.filter(block=False, title=self.kwargs.get('title')).first()
        products = ProductModel.objects.filter(block=False, brand=brand).order_by('-created_at')
        categories = CategoryModel.objects.filter(block=False).order_by('-created_at')

        qqq = []
        www = []
        brands = BrandModel.objects.filter(block=False).order_by('-created_at')
        categories = CategoryModel.objects.filter(block=False).order_by('-created_at')        
        min_price = ProductModel.objects.filter(block=False).order_by('sale_price').first()
        max_price = ProductModel.objects.filter(block=False).order_by('-sale_price').first()

        sorted_product = sort_product(products)

        for i in brands:
            product_count = ProductModel.objects.filter(block=False, brand=i).count()
            if product_count > 0:
                www.append({'brand': i, 'count': product_count})

        for i in categories:
            product_count = ProductModel.objects.filter(block=False, category=i).count()
            if product_count > 0:
                qqq.append({'category': i, 'count': product_count})

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, self.template_name,
            {
                'brands': www,
                'prod_categories': qqq,
                'min_price': min_price,
                'max_price': max_price,
                'products': sorted_product
                
            })

class ProductFilterCategory (TemplateView):
    template_name = 'user/product.html'

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        category = CategoryModel.objects.filter(block=False, title=self.kwargs.get('title')).first()
        products = ProductModel.objects.filter(block=False, category=category).order_by('-created_at')

        www = []
        qqq = []
        brands = BrandModel.objects.filter(block=False).order_by('-created_at')
        categories = CategoryModel.objects.filter(block=False).order_by('-created_at')
        min_price = ProductModel.objects.filter(block=False).order_by('sale_price').first()
        max_price = ProductModel.objects.filter(block=False).order_by('-sale_price').first()

        sorted_product = sort_product(products)

        for i in brands:
            product_count = ProductModel.objects.filter(block=False, brand=i).count()
            if product_count > 0:
                www.append({'brand': i, 'count': product_count})

        for i in categories:
            product_count = ProductModel.objects.filter(block=False, category=i).count()
            if product_count > 0:
                qqq.append({'category': i, 'count': product_count})

        # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return render(request, self.template_name,
            {
                'brands': www,
                'prod_categories': qqq,
                'min_price': min_price,
                'max_price': max_price,
                'products': sorted_product
                
            })

class ProductFilterPrice (FormView):
    model = ProductModel
    form_class = ProductPriceForm
    queryset = ProductModel.objects.all()
    template_name = 'user/product.html'

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super(ProductFilterPrice, self).get_form_kwargs()
        products = ProductModel.objects.all()
        kwargs['max'] = products.order_by('-sale_price').first().sale_price
        kwargs['min'] = products.order_by('sale_price').first().sale_price
        return kwargs

    def form_valid(self, form: Any) -> HttpResponse:
        products = ProductModel.objects.all()
        obj = ProductModel.objects.filter(sale_price__range=[form.cleaned_data['min_price'], form.cleaned_data['price']]).all()
        products = ProductModel.objects.all()
        form = ProductPriceForm(products.order_by('-sale_price').first().sale_price, products.order_by('sale_price').first().sale_price)
        sorted_products = sort_product(obj)

        return render(self.request, self.template_name, {'products': sorted_products, 'form': form,})


class ProductListView (ListView):
    model = ProductModel
    context_object_name = 'products'
    template_name = 'admin/products/admin_product_list.html'
    success_url = '/product/list/'

    def get (self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        products = ProductModel.objects.all()
        send_list = []
        for i in products:
            images = ProductImageModel.objects.filter(product=i.pk)
            stars = ProductRatingModel.objects.filter(product=i.pk)
            likes = ProductLikeModel.objects.filter(product=i.pk).first()
            
            ProductModel.get_req_card(i, images, stars, likes, send_list)
        return render(request, self.template_name, {'products': send_list})

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductCreateView (FormView):
    model = ProductModel
    form_class = ProductForm
    template_name = 'admin/products/admin_product_create.html'
    success_url = '/product/list/'

    def form_valid (self, form: Any) -> HttpResponse:
        ProductModel.objects.create(
            by_user = self.request.user,
            title = form.cleaned_data['title'],
            width = form.cleaned_data['width'],
            depth = form.cleaned_data['depth'],
            price = form.cleaned_data['price'],
            brand = form.cleaned_data['brand'],
            height = form.cleaned_data['height'],
            discount = form.cleaned_data['discount'],
            category = form.cleaned_data['category'],
            sku = randrange(1000000000000, 9999999999999),
            description = form.cleaned_data['description'],
            sale_price = form.cleaned_data['price'] - ((form.cleaned_data['discount'] * form.cleaned_data['price']) / 100)  
        )

        return super(ProductCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductUpdateView (UpdateView):
    model = ProductModel
    form_class = ProductUpdateForm
    queryset = ProductModel.objects.all()
    template_name = 'admin/products/admin_product_update.html'
    success_url = '/product/list/'

    def form_valid (self, form: Any) -> HttpResponse:
        form.instance.sale_price = form.cleaned_data['price'] - ((form.cleaned_data['discount'] * form.cleaned_data['price']) / 100)
        form.save()
        return super(ProductUpdateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductDetailView (DetailView):
    model = ProductModel
    form_class = ProductCommentForm,
    queryset = ProductModel.objects.all()
    template_name = 'admin/products/admin_product_detail.html'

    def get (self, request: HttpRequest, pk, *args: Any, **kwargs: Any) -> HttpResponse:
        product = ProductModel.objects.filter(pk=pk).first()
        product_stars = ProductRatingModel.objects.filter(product=pk)
        product_like = ProductLikeModel.objects.filter(product=pk).first()
        product_tags = ProductTagModel.objects.filter(product=pk).order_by('sequence_number')
        product_sizes = ProductSizeModel.objects.filter(product=pk).order_by('sequence_number')
        product_images = ProductImageModel.objects.filter(product=pk).order_by('sequence_number')
        product_comments = ProductCommentModel.objects.filter(product=pk).order_by('-created_at')
        product_colors = ProductColorModel.objects.filter(product=pk).order_by('sequence_number')
        product_ratings = ProductRatingModel.objects.filter(product=pk, block=False).order_by('-created_at')
        take_stars = ProductModel.get_stars(product_stars)

        return render (
            request, self.template_name, 
            {
                'product': product,
                'form': self.form_class,
                'product_stars': take_stars,
                'product_like': product_like,
                'product_tags': product_tags,
                'reviews': len(product_stars),
                'product_sizes': product_sizes,
                'product_colors': product_colors,
                'product_images': product_images,
                'product_comments': product_comments,
            },
        )
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductDeleteView (DeleteView):
    model = ProductModel
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_list')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductImageCreateView (FormView):
    model = ProductImageModel
    form_class = ProductImageForm
    template_name = 'admin/products/admin_product_image_create.html'
    success_url = '/product/list/'

    def form_valid (self, form):
        product = ProductModel.objects.filter(pk=self.kwargs.get('pk')).first()

        ProductImageModel.objects.create(
            product = product,
            by_user = self.request.user,
            image = form.cleaned_data['image'],
            sequence_number = form.cleaned_data['sequence_number'],
        )
        return super(ProductImageCreateView, self).form_valid(form)

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductImageDeleteView (DeleteView):
    model = ProductImageModel
    queryset = ProductImageModel.objects.all()
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_detail')

    def form_valid (self, form: Any):
        product_images = ProductImageModel.objects.filter(pk=self.kwargs.get('pk')).first()
        get_pk = product_images
        product_images.delete()

        return redirect('/product/detail/' + str(get_pk.product.pk))
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductImageUpdateView (UpdateView):
    model = ProductImageModel
    form_class = ProductImageUpdateForm
    template_name = 'admin/products/admin_product_image_update.html'
    success_url = '/product/list/'   

    def form_valid(self, form):
        product_image = ProductImageModel.objects.filter(pk=self.kwargs.get('pk'))
        product_image.update(
            image = form.cleaned_data['image'],
            block = form.cleaned_data['block'],
            sequence_number = form.cleaned_data['sequence_number'],
        ) 

        return redirect('/product/detail/' + str(product_image[0].product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductCommentCreateView (FormView):
    model = ProductCommentModel
    form_class = ProductCommentForm
    template_name = 'admin/products/admin_product_detail.html'

    def form_valid (self, form: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            product = ProductModel.objects.filter(pk=self.kwargs.get('pk')).first()
            ProductCommentModel.objects.create(
                product = product,
                by_user = self.request.user,
                message = form.cleaned_data['message']
            )

            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return redirect('/user/login/')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductCommentUpdateView (UpdateView):
    model = ProductCommentModel
    form_class = ProductCommentUpdateForm
    queryset = ProductCommentModel.objects.all()
    template_name = 'admin/products/admin_product_comment_update.html'

    def form_valid (self, form):
        product_comment = ProductCommentModel.objects.filter(pk=self.kwargs.get('pk'))
        product_comment.update(
            block = form.cleaned_data['block'],
            message = form.cleaned_data['message'],
        )
        
        return redirect('/product/detail/' + str(product_comment[0].product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductCommentDeleteView (DeleteView):
    model = ProductCommentModel
    queryset = ProductCommentModel.objects.all()
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_list')

    def form_valid (self, form: Any):
        product_comments = ProductCommentModel.objects.filter(pk=self.kwargs.get('pk')).first()
        get_pk = product_comments
        product_comments.delete()

        return redirect('/product/detail/' + str(get_pk.product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductLikeListView (ListView):
    model = ProductLikeModel
    template_name = 'user/wishlist.html'
    success_url = '/product/wishlist/'

    def get (self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            product_likes = ProductLikeModel.objects.filter(by_user=self.request.user).order_by('-created_at')
            product_images = ProductImageModel.objects.filter(block=False)

            return render(request, self.template_name, {'product_likes': product_likes, 'product_images': product_images})    
        return redirect('/user/login/')

class ProductLikeCreateView (CreateView):
    model = ProductLikeModel
    template_name = 'user/wishlist.html'
    success_url = "/product/wishlist/"

    def get(self, request: HttpRequest, pk, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            product = ProductModel.objects.filter(pk=pk).first()
            product_like = ProductLikeModel.objects.filter(product=product.pk).first()
            if product_like is None:
                ProductLikeModel.objects.create(
                    by_user = self.request.user,
                    product = product
                )
            else:
                product_like.delete()
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return redirect('/user/login/')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductLikeDeleteView (DeleteView):
    model = ProductLikeModel
    template_name = 'user/wishlist.html'
    success_url = '/product/wishlist/'

    def get(self, request: HttpRequest, pk, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            product = ProductModel.objects.filter(pk=pk).first()
            product_like = ProductLikeModel.objects.filter(product=product.pk).first()
            product_like.delete()
            return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        return redirect('/404/')

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductRatingCreateView (TemplateView):
    template_name = 'user/index.html'
    model = ProductRatingModel

    def get(self, request: HttpRequest, pk, count, *args: str, **kwargs: Any) -> HttpResponse:
        if count >= 1 and count <= 5:
            if self.request.user.is_anonymous:
                return redirect('/user/login/')
            else:
                product = ProductModel.objects.filter(pk=pk).first()
                rating = ProductRatingModel.objects.filter(product=product, by_user=self.request.user).first()

                if rating == None:
                    ProductRatingModel.objects.create(
                        stars = count,
                        product = product,
                        express_interest = 1,
                        by_user = self.request.user,
                    )   
                else:
                    if self.request.user == rating.by_user:
                        rating_2 = ProductRatingModel.objects.filter(product=product, by_user=self.request.user)
                        rating_2.update(
                            stars = count 
                        )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductTagCreateView (FormView):
    model = ProductTagModel
    form_class = ProductTagForm
    template_name = 'admin/products/admin_product_create.html'
    success_url = '/product/list/'
    def form_valid(self, form):
        product = ProductModel.objects.filter(pk=self.kwargs.get('pk')).first()
        ProductTagModel.objects.create(
            product = product,
            by_user = self.request.user,
            title = form.cleaned_data['title'],
            sequence_number = form.cleaned_data['sequence_number'],
        )
        super(ProductTagCreateView, self).form_valid(form)
        return redirect('/product/detail/'+ str(self.kwargs.get('pk')))
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductTagUpdateView (UpdateView):
    model = ProductTagModel
    form_class = ProductTagUpdateForm
    template_name = 'admin/products/admin_product_tag_update.html'
    success_url = '/product/list/'

    def form_valid (self, form: Any) -> HttpResponse:
        product_tag = ProductTagModel.objects.filter(pk=self.kwargs.get('pk'))
        product_tag.update(
            title = form.cleaned_data['title'],
            block = form.cleaned_data['block'],
            sequence_number = form.cleaned_data['sequence_number']
        )
        return redirect('/product/detail/' + str(product_tag[0].product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductTagDeleteView (DeleteView):
    model = ProductTagModel
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_list')

    def form_valid (self, form: Any):
        product_tag = ProductTagModel.objects.filter(pk=self.kwargs.get('pk')).first()
        get_pk = product_tag.product.pk
        product_tag.delete()

        return redirect('/product/detail/' + str(get_pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductColorCreateView(FormView):
    model = ProductColorModel
    form_class = ProductColorForm
    template_name = 'admin/products/admin_product_color_create.html'
    success_url = '/product/list/'
    
    def form_valid (self, form):
        product = ProductModel.objects.filter(pk=self.kwargs.get('pk')).first()
        ProductColorModel.objects.create(
            product = product,
            by_user = self.request.user,
            color = form.cleaned_data['color'],
            sequence_number = form.cleaned_data['sequence_number'],                        
        )

        super(ProductColorCreateView, self).form_valid(form)
        return redirect('/product/detail/' + str(self.kwargs.get('pk')))
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductColorUpdateView (UpdateView):
    model = ProductColorModel
    form_class = ProductColorUpdateForm
    template_name = 'admin/products/admin_product_color_update.html'

    def form_valid (self, form):
        product_color = ProductColorModel.objects.filter(pk=self.kwargs.get('pk'))
        product_color.update(
            block = form.cleaned_data['block'],
            color = form.cleaned_data['color'],
            sequence_number = form.cleaned_data['sequence_number'],                        
        )

        return redirect('/product/detail/' + str(product_color[0].product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductColorDeleteView (DeleteView):
    model = ProductColorModel
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_list')

    def form_valid (self, form: Any):
        product_color = ProductColorModel.objects.filter(pk=self.kwargs.get('pk')).first()
        get_pk = product_color.product.pk
        product_color.delete()

        return redirect('/product/detail/' + str(get_pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')


class ProductSizeCreateView (FormView):
    model = ProductSizeModel
    form_class = ProductSizeForm
    template_name = 'admin/products/admin_product_size_create.html'
    success_url = '/product/list/'

    def form_valid (self, form):
        product = ProductModel.objects.filter(pk=self.kwargs.get('pk'))
        ProductSizeModel.objects.create(
            product = product[0],
            by_user = self.request.user,
            size = form.cleaned_data['size'],
            color = form.cleaned_data['color'],
            quantity = form.cleaned_data['quantity'],
            sequence_number = form.cleaned_data['sequence_number'],
            add_or_subtract_price = form.cleaned_data['add_or_subtract_price']
        )

        product.update(
            quantity = product[0].quantity + form.cleaned_data['quantity'] 
        )

        super(ProductSizeCreateView, self).form_valid(form)
        return redirect('/product/detail/' + str(self.kwargs.get('pk')))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductSizeUpdateView (UpdateView):
    model = ProductSizeModel
    form_class = ProductSizeUpdateForm
    template_name = 'admin/products/admin_product_size_update.html'

    def form_valid (self, form):
        product_size = ProductSizeModel.objects.filter(pk=self.kwargs.get('pk'))
        product = ProductModel.objects.filter(pk=product_size[0].product.pk)

        product.update(
            quantity = product[0].quantity - product_size[0].quantity,
        )

        product_size.update(
            size = form.cleaned_data['size'],
            block = form.cleaned_data['block'],
            color = form.cleaned_data['color'],
            quantity = form.cleaned_data['quantity'],
            sequence_number = form.cleaned_data['sequence_number']                       
        )

        product.update(
            quantity = product[0].quantity + form.cleaned_data['quantity'] 
        )
        
        return redirect('/product/detail/' + str(product_size[0].product.pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')

class ProductSizeDeleteView (DeleteView):
    model = ProductSizeModel
    template_name = 'admin/products/admin_product_delete.html'
    success_url = reverse_lazy('product_list')

    def form_valid (self, form: Any):
        product_size = ProductSizeModel.objects.filter(pk=self.kwargs.get('pk')).first()
        get_pk = product_size.product.pk
        product_size.delete()

        return redirect('/product/detail/' + str(get_pk))

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        return redirect('/404/')         