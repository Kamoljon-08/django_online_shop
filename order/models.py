from django.db import models
from django.urls import reverse

# Create your models here.

class OrderModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    city = models.CharField(name='city', max_length=100)
    block = models.BooleanField(name='block', default=False)
    address = models.CharField(name='address', max_length=100)
    country = models.CharField(name='country', max_length=100)
    history = models.BooleanField(name='history', default=False)
    company_name = models.CharField(name='company_name', max_length=100)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    postcode = models.DecimalField(name='postcode', max_digits=7, decimal_places=0)
    user = models.ForeignKey('users.Customuser', name='user', on_delete=models.CASCADE)
    total_price = models.DecimalField(name='total_price', max_digits=10, decimal_places=2, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('checkout')