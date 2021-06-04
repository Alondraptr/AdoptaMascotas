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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'pet' # Le doy de nombre 'pet' a nuestra tabla en la Base de Datos
