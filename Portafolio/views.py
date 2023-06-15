from django.shortcuts import render
from .models import project

def render_projects(request):
    projects = project.objects.all()
    return render(request, 'projects.html', {'projects': projects})
