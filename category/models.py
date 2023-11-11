from django.db import models
from django.urls import reverse

# Create your models here.

class CategoryModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    title = models.CharField(name='title', max_length=100, blank=False, null=False)
    image = models.ImageField(name='image', upload_to='category/', blank=False, null=False)

    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('category_list')