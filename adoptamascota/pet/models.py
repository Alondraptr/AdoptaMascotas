from django.db import models
from organization.models import Organization

# Creación de campos de la tabla 'pet'
class Pet(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    pet_type = models.CharField(max_length=100)   # Select
    breed = models.CharField(max_length=100, default='No se sabe')    # Raza
    age = models.IntegerField()
    castrated = models.BooleanField()
    illness = models.CharField(max_length=250, blank=True) # Enfermedad

    img_1 = models.ImageField(upload_to='pet_img', blank=True, default='')
    img_2 = models.ImageField(upload_to='pet_img', blank=True, default='')
    img_3 = models.ImageField(upload_to='pet_img', blank=True, default='')
    img_4 = models.ImageField(upload_to='pet_img', blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pet' # Le doy de nombre 'pet' a nuestra tabla en la Base de Datos
