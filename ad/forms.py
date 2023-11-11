from django import forms
from .models import AdModel

class AdForm (forms.ModelForm):
    class Meta:
        model = AdModel
        fields = ('link', 'image')