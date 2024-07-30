from django.contrib import admin
from .models import Factura, DetalleFactura, Empresa, Receptor, FacturaEstado, FormaPago

class DetalleFacturaInline(admin.TabularInline):
    model = DetalleFactura
    extra = 1

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'empresa', 'receptor', 'fecha_emision', 'tipo_factura', 'forma_pago')
    list_filter = ('fecha_emision', 'tipo_factura', 'forma_pago')
    search_fields = ('empresa__razon_social', 'receptor__razon_social', 'numero')
    inlines = [DetalleFacturaInline]
    readonly_fields = ('numero',)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'rut', 'domicilio', 'giro')
    search_fields = ('razon_social', 'rut')

class ReceptorAdmin(admin.ModelAdmin):
    list_display = ('razon_social', 'rut', 'domicilio')
    search_fields = ('razon_social', 'rut')

class FacturaEstadoAdmin(admin.ModelAdmin):
    list_display = ('estado',)
    search_fields = ('estado',)

class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('forma_pago',)
    search_fields = ('forma_pago',)

admin.site.register(Factura, FacturaAdmin)
admin.site.register(DetalleFactura)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Receptor, ReceptorAdmin)
admin.site.register(FacturaEstado, FacturaEstadoAdmin)
admin.site.register(FormaPago, FormaPagoAdmin)
