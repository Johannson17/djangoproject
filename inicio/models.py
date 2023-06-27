from django.db import models 
from django.db.models.fields import CharField, URLField, TextField, DateField 
from django.db.models.fields.files import ImageField
import datetime 

def upload_to_static(instance, filename):
    return f'inicio/{filename}'

class info(models.Model):
    title = CharField(max_length=50)
    sub_title = CharField(max_length=100)
    description = TextField()
    image = ImageField(upload_to=upload_to_static)

class degree(models.Model):
    title = CharField(max_length=50)
    sub_title = CharField(max_length=100)
    description = TextField()
    date1 = DateField()
    date = DateField(default=datetime.date.today)

class experience(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    puesto = CharField(max_length=100)
    date1 = DateField()
    date = DateField(default=datetime.date.today)