from django.shortcuts import render
from .models import Factura, Empresa, Receptor
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

def index(request):
    receptores = Receptor.objects.all()

    context = {
        'empresas': empresas,
        '': receptores,
    }
    return render(request, 'index.html', context)

@login_required
def facturas(request):
    facturas = Factura.objects.all()
    context = {'facturas':facturas}
    return render(request, 'lista_facturas.html', context)

@login_required
def empresas(request):
    empresas = Empresa.objects.all()
    context = {'empresas':empresas}
    return render(request, 'lista_empresas.html', context)

@login_required
def receptores(request):
    receptores = Receptor.objects.all()
    context = {'receptores':receptores}
    return render(request, 'lista_receptores.html', context)

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'
