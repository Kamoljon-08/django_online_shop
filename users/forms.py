from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm (UserCreationForm):
    phone = forms.CharField(label='Phone Number', max_length=30, required=True, widget=forms.TextInput(attrs={'id': 'phone', 'class': 'form-control bdr'}))
    email = forms.CharField(label='Email Address', max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'email', 'class': 'form-control bdr'}))
    username = forms.CharField(label='Username', max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'username', 'class': 'form-control bdr'}))
    last_name = forms.CharField(label='Last Name', max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'last_name', 'class': 'form-control bdr'}))
    first_name = forms.CharField(label='First Name', max_length=50, required=True, widget=forms.TextInput(attrs={'id': 'first_name', 'class': 'form-control bdr'}))   

    class Meta (UserCreationForm):
        model = CustomUser
        fields = '__all__'

class UsersUpdateForm (forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'phone', 'password', 'image', 'block', 'is_staff', 'is_superuser']

class ResetPasswordForm(forms.Form):
    phone = forms.CharField(label='Phone Number',max_length=20, required=True)

class VerifyForm(forms.Form):
    phone = forms.IntegerField(label='Enter Verify Code', required=True)

class ResetPasswordCompleteForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('password1', 'password2')