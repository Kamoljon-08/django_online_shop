from django.db import models
from django.urls import reverse
# Create your models here.

class AdModel (models.Model):
    link = models.URLField(name='link', max_length=100)
    image = models.FileField(name='image', upload_to='ad/')
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)

    def __str__ (self):
        return self.go_url

    def get_absolute_url (self):
        return reverse ('ad_list')