from django import forms
from .models import Factura, DetalleFactura, Empresa, Receptor, FacturaEstado, FormaPago

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['empresa', 'receptor', 'fecha_emision', 'tipo_factura', 'forma_pago']
        widgets = {
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'fecha_emision': 'Fecha',
            'tipo_factura': 'Tipo de Factura',
            'forma_pago': 'Forma de Pago',
        }

class DetalleFacturaForm(forms.ModelForm):
    class Meta:
        model = DetalleFactura
        fields = ['descripcion', 'cantidad', 'precio_unitario', 'descuento']
        widgets = {
            'descuento': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
            'precio_unitario': forms.NumberInput(attrs={'step': '1', 'min': '0'}),
        }
        labels = {
            'descripcion': 'Descripción',
            'cantidad': 'Cantidad',
            'precio_unitario': 'Precio (CLP)',
            'descuento': 'Descuento (CLP)',
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razon_social', 'rut', 'domicilio', 'giro']
        labels = {
            'razon_social': 'Razón Social',
            'rut': 'RUT',
            'domicilio': 'Domicilio',
            'giro': 'Giro',
        }

class ReceptorForm(forms.ModelForm):
    class Meta:
        model = Receptor
        fields = ['razon_social', 'rut', 'domicilio']
        labels = {
            'razon_social': 'Razón Social',
            'rut': 'RUT',
            'domicilio': 'Domicilio',
        }

class FacturaEstadoForm(forms.ModelForm):
    class Meta:
        model = FacturaEstado
        fields = ['estado']
        labels = {
            'estado': 'Estado',
        }

class FormaPagoForm(forms.ModelForm):
    class Meta:
        model = FormaPago
        fields = ['forma_pago']
        labels = {
            'forma_pago': 'Forma de Pago',
        }
