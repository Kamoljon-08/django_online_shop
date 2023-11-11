from django.urls import reverse
from django.db import models

# Create your models here.

class CompanyFileModel (models.Model):
    image = models.FileField(name='image', upload_to='about/')
    title = models.CharField(name='title', blank=False, max_length=20)
    block = models.BooleanField(name='block', blank=True, default=True)
    created_at = models.DateTimeField(name='created_at', blank=True, auto_now=True)

    def get_absolute_url (self):
        return reverse('about_list')

    def get_req (self):
        return self

class CompanyMemberModel (models.Model):
    image = models.ImageField(name='image', upload_to='about/')
    job = models.CharField(name='job', blank=True, max_length=20)
    phone = models.CharField(name='phone', blank=True, max_length=25)
    email = models.EmailField(name='email', blank=True, max_length=30)
    block = models.BooleanField(name='block', blank=True, default=True)
    last_name = models.CharField(name='last_name', blank=True, max_length=30)
    first_name = models.CharField(name='first_name', blank=True, max_length=40)
    created_at = models.DateTimeField(name='created_at', blank=True, auto_now=True)

    def get_absolute_url (self):
        return reverse('about_list') 

    def get_req (self):
        return self