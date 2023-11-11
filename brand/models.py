from django.db import models
from django.urls import reverse

# Create your models here.

class BrandModel (models.Model):
    title = models.CharField(name='title', max_length=50)
    block = models.BooleanField(name='block', default=False)
    image = models.ImageField(name='image', upload_to='brand/')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('brand_list')