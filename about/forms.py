from django import forms
from .models import CompanyFileModel, CompanyMemberModel
from django.contrib.auth.forms import UserCreationForm

class CompanyFileForm (forms.ModelForm):
    class Meta:
        model = CompanyFileModel
        fields = ('title', 'image')

class CompanyMemberForm (forms.ModelForm):
    class Meta:
        model = CompanyMemberModel
        fields = ('first_name', 'last_name', 'email', 'phone', 'job', 'image')