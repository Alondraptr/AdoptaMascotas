from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
 
# Creación de campos de la tabla 'organization' 
class Organization(models.Model):
    name = models.CharField(max_length=100, unique = True)
    description = models.CharField(max_length=250)
    support = models.CharField(max_length=100)
    mail = models.EmailField(max_length=100, unique = True)
    phone = models.IntegerField(unique = True)
    city = models.CharField(max_length=100)
    img = models.ImageField(upload_to='org_img', blank=True, default='')
    fb_url = models.CharField(max_length=200, blank=True, default='')
    ig_url = models.CharField(max_length=200, blank=True, default='')
    yt_url = models.CharField(max_length=200, blank=True, default='')
    tw_url = models.CharField(max_length=200, blank=True, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
    class Meta:
        db_table = 'organization' # Le doy de nombre 'organization' a nuestra tabla en la Base de Datos
