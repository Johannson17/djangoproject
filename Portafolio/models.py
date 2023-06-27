from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

def upload_to_static(instance, filename):
    return f'portfolio/{filename}'

class project(models.Model):
    tittle = CharField(max_length=100)
    description = CharField(max_length=250)
    img = ImageField(upload_to=upload_to_static)
    url = URLField(blank=True)
