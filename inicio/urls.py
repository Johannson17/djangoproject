from django.urls import path
from .views import render_post

app_name='inicio'

urlpatterns= [
    path('', render_post,),
]