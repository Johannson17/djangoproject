from django.db import models 
from django.db.models.fields import CharField, URLField, TextField, DateField 
from django.db.models.fields.files import ImageField
import datetime 

class info(models.Model):
    title = CharField(max_length=50)
    sub_title = CharField(max_length=100)
    description = TextField()
    image = ImageField()

class degree(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    date1 = DateField()
    date = DateField(default=datetime.date.today)

class experience(models.Model):
    title = CharField(max_length=100)
    description = TextField()
    puesto = CharField(max_length=100)
    date1 = DateField()
    date = DateField(default=datetime.date.today)