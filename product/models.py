from django.db import models
from django.urls import reverse
from colorfield.fields import ColorField
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class ProductModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    title = models.CharField(name='title', max_length=70)
    block = models.BooleanField(name='block', default=True)
    description = models.TextField(name='description', max_length=10000)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    super_product = models.BooleanField(name='super_product', default=False)
    price = models.DecimalField(name='price', max_digits=1000000, decimal_places=2)
    brand = models.ForeignKey('brand.BrandModel', name='brand', on_delete=models.CASCADE)
    sale_price = models.DecimalField(name='sale_price', max_digits=1000000, decimal_places=2)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE)
    category = models.ForeignKey('category.CategoryModel', name='category', on_delete=models.CASCADE)
    width = models.IntegerField(name='width', validators=[MaxValueValidator(1000), MinValueValidator(10)])
    depth = models.IntegerField(name='depth', validators=[MaxValueValidator(1000), MinValueValidator(10)])
    height = models.IntegerField(name='height', validators=[MaxValueValidator(1000), MinValueValidator(10)])
    discount = models.IntegerField(name='discount', validators=[MaxValueValidator(100), MinValueValidator(0)])
    sku = models.IntegerField(name='sku', validators=[MaxValueValidator(13), MinValueValidator(13)], unique=True)
    quantity = models.IntegerField(name='quantity', default=0, validators=[MaxValueValidator(1000), MinValueValidator(0)])

    def __str__ (self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('product_list')

    def get_stars (stars:list) -> list:
        list_star = []

        count_stars = 0
        count_exp_int = 0

        for i in stars:
            count_stars += i.stars
            count_exp_int += i.express_interest

        if count_stars > 0 < count_exp_int: 
            star = int(count_stars / count_exp_int)
        else: star = 0

        if star >= 5:
            list_star = [['fill',1], ['fill',2], ['fill',3], ['fill',4], ['fill',5]]
        elif star == 4:
            list_star = [['fill',1], ['fill',2], ['fill',3], ['fill',4], ['blank',5]]
        elif star == 3:
            list_star = [['fill',1], ['fill',2], ['fill',3], ['blank',4], ['blank',5]]
        elif star == 2:
            list_star = [['fill',1], ['fill',2], ['blank',3], ['blank',4], ['blank',5]]
        elif star == 1:
            list_star = [['fill',1], ['blank',2], ['blank',3], ['blank',4], ['blank',5]]
        else:
            list_star = [['blank',1], ['blank',2], ['blank',3], ['blank',4], ['blank',5]]

        return list_star

    def get_req_card (self, images, stars, likes, send_list):
        take_stars = ProductModel.get_stars(stars)
        send_list.append(
            {
                'item': self,
                'likes': likes,
                'images': images,
                'stars': take_stars,              
                'reviews': len(stars),
            }
        )
        return send_list

class ProductImageModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=True)
    image = models.FileField(name='image', upload_to='product/')
    sequence_number = models.IntegerField(name='sequence_number')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE)

    def __str__ (self):
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_list')

class ProductCommentModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    message = models.TextField(name='message', max_length=500)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_detail', args=[str(self.id)])

class ProductLikeModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_list')

class ProductRatingModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    stars = models.SmallIntegerField(name='stars',  blank=False, null=False, default=0)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)
    express_interest = models.IntegerField(name='express_interest', null=True, default=0)

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_list')

class ProductTagModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    title = models.CharField(name='title', max_length=30)
    block = models.BooleanField(name='block', default=False)
    sequence_number = models.IntegerField(name='sequence_number')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE) 
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_list')

class ProductColorModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    color = models.TextField(name='color', max_length=20)
    block = models.BooleanField(name='block', default=False)
    sequence_number = models.IntegerField(name='sequence_number')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE) 

    def __str__ (self) -> str:
        return str(self.color)

    def get_absolute_url (self):
        return reverse('product_list')

class ProductSizeModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    size = models.CharField(name='size', max_length=30)
    block = models.BooleanField(name='block', default=False)
    sequence_number = models.IntegerField(name='sequence_number')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    product = models.ForeignKey('ProductModel', name='product', on_delete=models.CASCADE)
    color = models.ForeignKey('ProductColorModel', name='color', on_delete=models.CASCADE)
    by_user = models.ForeignKey('users.CustomUser', name='by_user', on_delete=models.CASCADE) 
    add_or_subtract_price = models.DecimalField(name='add_or_subtract_price', max_digits=1000000, decimal_places=2)
    quantity = models.SmallIntegerField(name='quantity', validators=[MaxValueValidator(1000), MinValueValidator(1)])

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('product_list')