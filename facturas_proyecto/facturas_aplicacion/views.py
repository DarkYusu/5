from django.shortcuts import render
from .models import Factura, Empresa, Receptor

def index(request):
    facturas = Factura.objects.all()
    empresas = Empresa.objects.all()
    receptores = Receptor.objects.all()

    context = {
        'facturas': facturas,
        'empresas': empresas,
        'receptores': receptores,
    }
    return render(request, 'index.html', context)
