from django import forms
from .models import BrandModel

class BrandForm (forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = ('title', 'image')