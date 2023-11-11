from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class BlogModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    title = models.CharField(name='title', max_length=70)
    block = models.BooleanField(name='block', default=False)
    description = RichTextField(name='description', max_length=100000)
    author = models.ForeignKey(
        'users.CustomUser',
        name='author',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('blog_image_create', args=[str(self.id)])

class BlogImageModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    image = models.FileField(name='image', upload_to='blog/')
    sequence_number = models.IntegerField(name='sequence_number')
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    blog = models.ForeignKey(
        'BlogModel',
        name='blog',
        on_delete=models.CASCADE
    )

    def __str__ (self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('blog_detail', args=[str(self.blog)])

class BlogCommentModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    message = models.TextField(name='message', max_length=500)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    user = models.ForeignKey(
        'users.CustomUser',
        name='user',
        on_delete=models.CASCADE
    )

    blog = models.ForeignKey(
        'BlogModel',
        name='blog',
        on_delete=models.CASCADE,
    )

    def __str__ (self):
        return str(self.id)

    def get_absolute_url (self):
        return reverse('blog_detail', args=[str(self.blog)])