from django import forms
from .models import (
    NotificationModel,

)

class NotificationForm (forms.ModelForm):
    message = forms.CharField(label='Message', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'Message', 'placeholder': 'Enter your message here...', 'rows': '12', 'class': 'form-control bdr2'}))
    class Meta:
        model = NotificationModel
        fields = ('message',)

class NotificationtUpdateForm (forms.ModelForm):
    message = forms.CharField(label='Message', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'Message', 'placeholder': 'Enter your message here...', 'rows': '12', 'class': 'form-control bdr2'}))
    class Meta:
        model = NotificationModel
        fields = ('message', 'block',)
