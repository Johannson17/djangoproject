from django.contrib import admin
from .models import info
from .models import degree
from .models import experience

admin.site.register(info)
admin.site.register(degree)
admin.site.register(experience)