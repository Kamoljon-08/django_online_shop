from django import forms
from .models import BlogModel, BlogImageModel, BlogCommentModel

class BlogForm (forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ('title', 'description')

class BlogImageForm (forms.ModelForm):
    class Meta:
        model = BlogImageModel
        fields = ('sequence_number', 'image')

class BlogImageUpdateForm (forms.ModelForm):
    sequence_number = forms.CharField(label='Sequence Number', max_length=1000, required=True, widget=forms.TextInput(attrs={'id': 'sequence_number'}))

    class Meta:
        model = BlogImageModel
        fields = ('sequence_number', 'block', 'image')

class BlogCommentForm (forms.ModelForm):
    message = forms.CharField(label='Enter your comment', max_length=500, required=True, widget=forms.Textarea(attrs={'id': 'message', 'placeholder': 'Enter your comment here...', 'rows': '12', 'class': 'form-control bdr2'}))

    class Meta:
        model = BlogCommentModel
        fields = ['message',]

class BlogCommentUpdateForm (forms.ModelForm):
    message = forms.CharField(label='Enter your comment', max_length=500, required=True, widget=forms.Textarea(attrs={'id': 'messages', 'placeholder': 'Enter your comment here...', 'rows': '12', 'class': 'form-control bdr2', 'style': "width: 100%"})),
    class Meta:
        model = BlogCommentModel
        fields = ['message', 'block']