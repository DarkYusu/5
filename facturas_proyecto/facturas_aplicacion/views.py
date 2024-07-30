from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Factura, DetalleFactura
from .forms import FacturaForm, DetalleFacturaForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = '/'

class FacturaListView(View):
    def get(self, request):
        facturas = Factura.objects.all()
        return render(request, 'lista_facturas.html', {'facturas': facturas})

# Crear Factura
class FacturaCreateView(View):
    def get(self, request):
        form = FacturaForm()
        return render(request, 'factura_form.html', {'form': form})

    def post(self, request):
        form = FacturaForm(request.POST)
        if form.is_valid():
            factura = form.save()
            return redirect('factura_list')
        return render(request, 'factura_form.html', {'form': form})

# Actualizar Factura
class FacturaUpdateView(View):
    def get(self, request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        form = FacturaForm(instance=factura)
        return render(request, 'factura_form.html', {'form': form})

    def post(self, request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('factura_list')
        return render(request, 'factura_form.html', {'form': form})

# Eliminar Factura
class FacturaDeleteView(View):
    def get(self, request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        return render(request, 'factura_confirm_delete.html', {'factura': factura})

    def post(self, request, pk):
        factura = get_object_or_404(Factura, pk=pk)
        factura.delete()
        return redirect('factura_list')


# Listar Detalles de Factura
class DetalleFacturaListView(View):
    def get(self, request, factura_id):
        factura = get_object_or_404(Factura, pk=factura_id)
        detalles = factura.detalles.all()
        return render(request, 'detalle_factura_list.html', {'factura': factura, 'detalles': detalles})

# Crear Detalle de Factura
class DetalleFacturaCreateView(View):
    def get(self, request, factura_id):
        form = DetalleFacturaForm()
        return render(request, 'detalle_factura_form.html', {'form': form, 'factura_id': factura_id})

    def post(self, request, factura_id):
        form = DetalleFacturaForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.factura_id = factura_id
            detalle.save()
            return redirect('detalle_factura_list', factura_id=factura_id)
        return render(request, 'detalle_factura_form.html', {'form': form, 'factura_id': factura_id})

# Actualizar Detalle de Factura
class DetalleFacturaUpdateView(View):
    def get(self, request, pk):
        detalle = get_object_or_404(DetalleFactura, pk=pk)
        form = DetalleFacturaForm(instance=detalle)
        return render(request, 'detalle_factura_form.html', {'form': form, 'factura_id': detalle.factura_id})

    def post(self, request, pk):
        detalle = get_object_or_404(DetalleFactura, pk=pk)
        form = DetalleFacturaForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('detalle_factura_list', factura_id=detalle.factura_id)
        return render(request, 'detalle_factura_form.html', {'form': form, 'factura_id': detalle.factura_id})

# Eliminar Detalle de Factura
class DetalleFacturaDeleteView(View):
    def get(self, request, pk):
        detalle = get_object_or_404(DetalleFactura, pk=pk)
        return render(request, 'detalle_factura_confirm_delete.html', {'detalle': detalle})

    def post(self, request, pk):
        detalle = get_object_or_404(DetalleFactura, pk=pk)
        factura_id = detalle.factura_id
        detalle.delete()
        return redirect('detalle_factura_list', factura_id=factura_id)