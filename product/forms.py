from django import forms
from .models import (
    ProductModel,
    ProductTagModel,
    ProductLikeModel,
    ProductSizeModel,
    ProductImageModel,
    ProductColorModel,
    ProductCommentModel,
)

class ProductPriceForm(forms.Form):
    min_price = forms.FloatField(required=False, widget=forms.TextInput(attrs={"min":"0", "max":"7", "oninput":"validity.valid||(value='1');","id":"min_price","class":"price-range-field", "value":"150"}))
    price = forms.FloatField(required=False)

    def __init__(self, max, min, *args, **kwargs):
        super(ProductPriceForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget = forms.TextInput(attrs={"min":'1', "max":f'{len(str(max))}', "oninput":f"validity.valid||(value='{max}');", "id":"max_price", "class":"price-range-field", "value": int(max)})
        self.fields['min_price'].widget = forms.TextInput(attrs={"min":"1", "max":f'{len(str(max))}', "oninput":f"validity.valid||(value='{min}');","id":"min_price","class":"price-range-field", "value":int(min)})

class ProductForm (forms.ModelForm):
    description = forms.CharField(label='Description', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'description', 'placeholder': 'Enter your description here...', 'rows': '12', 'class': 'form-control bdr2'}))

    class Meta:
        model = ProductModel
        fields = ('title', 'width', 'depth', 'height', 'description', 'discount', 'price', 'brand', 'category')

class ProductUpdateForm (forms.ModelForm):
    description = forms.CharField(label='Description', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'description', 'placeholder': 'Enter your description here...', 'rows': '12', 'class': 'form-control bdr2'}))

    class Meta:
        model = ProductModel
        fields = ('title', 'block', 'width', 'depth', 'height', 'description', 'super_product', 'discount', 'price', 'brand', 'category')


class ProductImageForm (forms.ModelForm):
    class Meta:
        model = ProductImageModel
        fields = ('sequence_number', 'image')

class ProductImageUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductImageModel
        fields = ('block', 'sequence_number', 'image')


class ProductCommentForm (forms.ModelForm):
    message = forms.CharField(label='Enter your message', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'description', 'placeholder': 'Enter your message here...', 'rows': '12', 'class': 'form-control bdr2'}))
    class Meta:
        model = ProductCommentModel
        fields = ['message',]

class ProductCommentUpdateForm (forms.ModelForm):
    message = forms.CharField(label='Enter your message', max_length=10000, required=True, widget=forms.Textarea(attrs={'id': 'description', 'placeholder': 'Enter your message here...', 'rows': '12', 'class': 'form-control bdr2'}))
    class Meta:
        model = ProductCommentModel
        fields = ('block', 'message')


class ProductTagForm (forms.ModelForm):
    class Meta:
        model = ProductTagModel
        fields = ('title', 'sequence_number')

class ProductTagUpdateForm (forms.ModelForm):
    class Meta:
        model = ProductTagModel
        fields = ('title', 'sequence_number', 'block')

    
class ProductColorForm (forms.ModelForm):
    color = forms.CharField(label='Color', required=True, widget=forms.TextInput(attrs={'id': 'color', 'type': 'color'}))
    class Meta:
        model = ProductColorModel
        fields = ('color', 'sequence_number')

class ProductColorUpdateForm (forms.ModelForm):
    color = forms.CharField(label='Color', required=True, widget=forms.TextInput(attrs={'id': 'color', 'type': 'color'}))
    class Meta:
        model = ProductColorModel
        fields = ('color', 'sequence_number', 'block')


class ProductSizeForm (forms.ModelForm):
    class Meta:
        model = ProductSizeModel
        fields = ('color', 'size', 'sequence_number', 'add_or_subtract_price', 'quantity')

class ProductSizeUpdateForm (forms.ModelForm):
    class Meta:
        model = ProductSizeModel
        fields = ('color', 'size', 'sequence_number', 'add_or_subtract_price', 'quantity', 'block')