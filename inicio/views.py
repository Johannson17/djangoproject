from django.shortcuts import render, get_object_or_404
from .models import info
from .models import degree
from .models import experience

def render_post(request):
    infos = info.objects.all()
    degrees = degree.objects.all()
    experiences = experience.objects.all()
    return render(request, 'me.html', {'infos': infos, 'degrees': degrees, 'experiences': experiences})