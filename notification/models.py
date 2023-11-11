from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class NotificationModel (models.Model):
    id = models.AutoField(name='id', primary_key=True)
    message = RichTextField(name='message', max_length=500)
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    user = models.ForeignKey(
        'users.CustomUser',
        name='user', 
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return str(self.id)

    def get_absolute_url(self):
        return reverse('notification_list')