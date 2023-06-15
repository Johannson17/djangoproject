from django.urls import path
from .views import render_contact

app_name='Contacto'

urlpatterns= [
    path('', render_contact),
]