from django import forms

class OrganizationAddForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    support = forms.CharField(max_length=100)
    mail = forms.CharField(max_length=100)
    phone = forms.IntegerField()
    city = forms.CharField(max_length=100)
    img = forms.FileField()