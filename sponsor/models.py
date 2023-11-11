from django.db import models
from django.urls import reverse

# Create your models here.

class SponsorModel (models.Model):
    link = models.URLField(name='link', max_length=100)
    title = models.CharField(name='title', max_length=70)
    block = models.BooleanField(name='block', default=False)
    image = models.ImageField(name='image', upload_to='sponsor/')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)


    def __str__ (self):
        return self

    def get_absolute_url (self):    
        return reverse('sponsor_list')