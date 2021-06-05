from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=250)
    pet_type = forms.CharField(max_length=100)   # Select
    breed = forms.CharField(max_length=100, required=False)    # Raza
    age = forms.IntegerField()
    castrated = forms.BooleanField(required=False, initial=False)
    illness = forms.CharField(max_length=250, required=False)

    img_1 = forms.ImageField(required=False)
    img_2 = forms.ImageField(required=False)
    img_3 = forms.ImageField(required=False)
    img_4 = forms.ImageField(required=False)

    class Meta:
        model = Pet
        fields = '__all__'


