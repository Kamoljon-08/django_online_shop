from django import forms
from .models import OrderModel

class OrderCreateForm (forms.ModelForm):
    country = forms.CharField(label='Country', max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'country', 'class': 'form-control bdr'}))
    city = forms.CharField(label='City', max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'city', 'class': 'form-control bdr'}))
    address = forms.CharField(label='Address', max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'address', 'class': 'form-control bdr'}))
    company_name = forms.CharField(label='Company Name', max_length=100, required=True, widget=forms.TextInput(attrs={'id': 'company_name', 'class': 'form-control bdr'}))
    postcode = forms.CharField(label='Postcode', max_length=7, required=True, widget=forms.TextInput(attrs={'id': 'postcode', 'class': 'form-control bdr'}))   

    class Meta:
        model = OrderModel
        fields = ('country', 'city', 'address', 'company_name', 'postcode')

class OrderUpdateForm (forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ('country', 'city', 'address', 'company_name', 'postcode','history', 'block')