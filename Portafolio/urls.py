from django.urls import path
from .views import render_projects

app_name='Portafolio'

urlpatterns= [
    path('', render_projects),
]