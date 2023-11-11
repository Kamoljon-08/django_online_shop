from django.db import models
from django.urls import reverse

# Create your models here.

class FaqModel (models.Model):
    answer = models.TextField(name='answer', max_length=500)
    block = models.BooleanField(name='block', default=False)
    question = models.CharField(name='question', max_length=100)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)

    def __str__ (self):
        return self.question

    def get_absolute_url (self):
        return reverse('faq_list')