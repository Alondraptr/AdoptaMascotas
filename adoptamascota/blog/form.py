from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)

    img_1 = forms.ImageField()
    img_2 = forms.ImageField(required=False)
    img_3 = forms.ImageField(required=False)
    img_4 = forms.ImageField(required=False)

    class Meta:
        model = Blog
        fields = '__all__'
