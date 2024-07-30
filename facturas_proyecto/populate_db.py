import datetime
from facturas_aplicacion.models import Empresa, Receptor, FormaPago, Factura, DetalleFactura, FacturaEstado

def run():
    # Crear Empresas
    empresa1 = Empresa.objects.create(
        razon_social='Empresa A',
        rut='12345678-9',
        domicilio='Calle Falsa 123',
        giro='Tecnología'
    )

    empresa2 = Empresa.objects.create(
        razon_social='Empresa B',
        rut='98765432-1',
        domicilio='Avenida Siempre Viva 742',
        giro='Consultoría'
    )

    # Crear Receptores
    receptor1 = Receptor.objects.create(
        razon_social='Receptor X',
        rut='11223344-5',
        domicilio='Calle Real 456'
    )

    receptor2 = Receptor.objects.create(
        razon_social='Receptor Y',
        rut='55667788-9',
        domicilio='Calle Principal 789'
    )

    # Crear Formas de Pago
    forma_pago1 = FormaPago.objects.create(forma_pago='Efectivo')
    forma_pago2 = FormaPago.objects.create(forma_pago='Tarjeta de Crédito')
    forma_pago3 = FormaPago.objects.create(forma_pago='Transferencia Bancaria')

    # Crear Estados de Factura
    estado1 = FacturaEstado.objects.create(estado='Pendiente')
    estado2 = FacturaEstado.objects.create(estado='Pagada')
    estado3 = FacturaEstado.objects.create(estado='Anulada')

    # Crear Facturas
    factura1 = Factura.objects.create(
        empresa=empresa1,
        receptor=receptor1,
        fecha_emision=datetime.date.today(),
        tipo_factura='FE',
        forma_pago=forma_pago1
    )

    factura2 = Factura.objects.create(
        empresa=empresa2,
        receptor=receptor2,
        fecha_emision=datetime.date.today(),
        tipo_factura='FD',
        forma_pago=forma_pago2
    )

    # Crear Detalles de Factura
    detalle1 = DetalleFactura.objects.create(
        factura=factura1,
        descripcion='Producto A',
        cantidad=10,
        precio_unitario=100,
        descuento=50
    )

    detalle2 = DetalleFactura.objects.create(
        factura=factura1,
        descripcion='Producto B',
        cantidad=5,
        precio_unitario=200,
        descuento=25
    )

    detalle3 = DetalleFactura.objects.create(
        factura=factura2,
        descripcion='Servicio A',
        cantidad=1,
        precio_unitario=1000,
        descuento=100
    )

    detalle4 = DetalleFactura.objects.create(
        factura=factura2,
        descripcion='Servicio B',
        cantidad=2,
        precio_unitario=500,
        descuento=50
    )

    print("Datos insertados correctamente.")
