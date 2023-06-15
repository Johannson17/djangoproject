from django.shortcuts import render
from .forms import ContactoForm

def render_contact(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "mensaje enviado"
        else:
            data["form"] = formulario
    return render(request, 'contacts.html', data)