from django import forms
from .models import FaqModel

class FaqForm (forms.ModelForm):
    class Meta:
        model = FaqModel
        fields = ('question', 'answer')