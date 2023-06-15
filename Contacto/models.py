from django.db import models
from django.db.models.fields import URLField
from django.db.models.fields.files import ImageField

class contact(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    numero = models.IntegerField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()