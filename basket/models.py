from django.db import models
from django.urls import reverse

# Create your models here.

class BasketModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    is_delete = models.BooleanField(name='is_delete', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    count = models.SmallIntegerField(name='count', blank=False, null=False, default=0)
    user = models.ForeignKey('users.Customuser', name='user', on_delete=models.CASCADE)
    product = models.ForeignKey('product.ProductModel', name='product', on_delete=models.CASCADE)
    price = models.DecimalField(name='price', max_digits=10, decimal_places=2, blank=False, null=False)
    sizes = models.ForeignKey('product.ProductSizeModel', name='sizes', on_delete=models.CASCADE, blank=True, null=True)
    color = models.ForeignKey('product.ProductColorModel', name='color', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.id)

    def get_absolute_url(self):
        return reverse('cart')