from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):

    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    support = forms.CharField(max_length=100)
    mail = forms.EmailField()
    phone = forms.IntegerField()
    city = forms.CharField(max_length=100)
    img = forms.ImageField(required=False)
    fb_url = forms.CharField(max_length=200, required=False)
    ig_url = forms.CharField(max_length=200, required=False)
    yt_url = forms.CharField(max_length=200, required=False)
    tw_url = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Organization
        fields = '__all__'
