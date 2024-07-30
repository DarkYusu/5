from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Factura, Empresa, Receptor, DetalleFactura
from .forms import FacturaForm, DetalleFacturaForm, EmpresaForm, ReceptorForm
from django.contrib.auth.decorators import login_required

@login_required
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

class EmpresaListView(View):
    def get(self, request):
        empresas = Empresa.objects.all()
        return render(request, 'lista_empresas.html', {'empresas': empresas})

class ReceptorListView(View):
    def get(self, request):
        receptores= Receptor.objects.all()
        return render(request, 'lista_receptores.html', {'receptores': receptores})
    
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
    
# Crear Empresa
class EmpresaCreateView(View):
    def get(self, request):
        form = EmpresaForm()
        return render(request, 'empresa_form.html', {'form': form})

    def post(self, request):
        form = EmpresaForm(request.POST)
        if form.is_valid():
            empresa = form.save()
            return redirect('empresa_list')
        return render(request, 'empresa_form.html', {'form': form})
    
# Actualizar Empresa
class EmpresaUpdateView(View):
    def get(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        form = EmpresaForm(instance=empresa)
        return render(request, 'empresa_form.html', {'form': form})

    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa_list')
        return render(request, 'empresa_form.html', {'form': form})
    
# Eliminar Empresa
class EmpresaDeleteView(View):
    def get(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        return render(request, 'empresa_confirm_delete.html', {'empresa': empresa})

    def post(self, request, pk):
        empresa = get_object_or_404(Empresa, pk=pk)
        empresa.delete()
        return redirect('empresa_list')
    
# Crear Receptor
class ReceptorCreateView(View):
    def get(self, request):
        form = ReceptorForm()
        return render(request, 'receptor_form.html', {'form': form})

    def post(self, request):
        form = ReceptorForm(request.POST)
        if form.is_valid():
            receptor = form.save()
            return redirect('receptor_list')
        return render(request, 'receptor_form.html', {'form': form})
    
# Actualizar Receptor
class ReceptorUpdateView(View):
    def get(self, request, pk):
        receptor = get_object_or_404(Receptor, pk=pk)
        form = ReceptorForm(instance=receptor)
        return render(request, 'receptor_form.html', {'form': form})

    def post(self, request, pk):
        receptor = get_object_or_404(Empresa, pk=pk)
        form = ReceptorForm(request.POST, instance=receptor)
        if form.is_valid():
            form.save()
            return redirect('receptor_list')
        return render(request, 'receptor_form.html', {'form': form})
    
# Eliminar Empresa
class ReceptorDeleteView(View):
    def get(self, request, pk):
        receptor = get_object_or_404(Receptor, pk=pk)
        return render(request, 'receptor_confirm_delete.html', {'receptor': receptor})

    def post(self, request, pk):
        receptor = get_object_or_404(Receptor, pk=pk)
        receptor.delete()
        return redirect('receptor_list')

# Detalle Factura completa
def factura_detail(request, pk):
    factura = get_object_or_404(Factura, pk=pk)
    detalles = DetalleFactura.objects.filter(factura=factura)
    subtotal_original = sum(detalle.cantidad * detalle.precio_unitario for detalle in detalles)
    descuento_total = sum(detalle.cantidad * detalle.descuento for detalle in detalles)
    subtotal_con_descuento = subtotal_original - descuento_total
    iva_monto = subtotal_con_descuento * 0.19
    total = subtotal_con_descuento + iva_monto
    return render(request, 'factura_detail.html', {
        'factura': factura,
        'detalles': detalles,
        'subtotal': subtotal_con_descuento,
        'iva_monto': iva_monto,
        'total': total,
        'descuento_total': descuento_total
    })

