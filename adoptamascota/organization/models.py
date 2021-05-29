from django.db import models
from django.utils import timezone
 
# Creación de campos de la tabla 'organization' 
class Organization(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    support = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    phone = models.IntegerField()
    city = models.CharField(max_length=100)
    img = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'organization' # Le doy de nombre 'organization' a nuestra tabla en la Base de Datos
