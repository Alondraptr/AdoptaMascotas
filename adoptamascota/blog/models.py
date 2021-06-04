from django.db import models
from organization.models import Organization

# Creación de campos de la tabla 'organization'
class Blog(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique = True)
    description = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'blog' # Le doy de nombre 'blog' a nuestra tabla en la Base de Datos
