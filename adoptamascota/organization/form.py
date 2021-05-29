from django import forms
from .models import Organization

class OrganizationAddForm(forms.ModelForm):
    
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    support = forms.CharField(max_length=100)
    mail = forms.EmailField()
    phone = forms.IntegerField()
    city = forms.CharField(max_length=100)
    img = forms.FileField()    

    class Meta:
        model = Organization
        fields = ('name', 'description','support','mail','phone','city')
