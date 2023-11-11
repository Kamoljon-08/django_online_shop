from django import forms
from .models import SponsorModel

class SponsorForm (forms.ModelForm):
    class Meta:
        model = SponsorModel
        fields = ('title', 'link', 'image')