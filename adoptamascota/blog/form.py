from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)

    class Meta:
        model = Blog
        fields = '__all__'
