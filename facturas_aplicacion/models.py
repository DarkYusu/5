from django.db import models

class Empresa(models.Model):
    razon_social = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    domicilio = models.CharField(max_length=255)
    giro = models.CharField(max_length=255)

    def __str__(self):
        return self.razon_social

class Receptor(models.Model):
    razon_social = models.CharField(max_length=255)
    rut = models.CharField(max_length=12, unique=True)
    domicilio = models.CharField(max_length=255)

    def __str__(self):
        return self.razon_social
    
class FormaPago(models.Model):
    forma_pago = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.forma_pago
    
class Factura(models.Model):
    TIPO_FACTURA_CHOICES = [
        ('FE', 'Factura Electrónica'),
        ('FD', 'Factura de Exportación'),
    ]

    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    numero = models.AutoField(primary_key=True)
    fecha_emision = models.DateField()
    tipo_factura = models.CharField(max_length=2, choices=TIPO_FACTURA_CHOICES)
    forma_pago = models.ForeignKey(FormaPago, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"Factura {self.numero} - {self.fecha_emision}"


class DetalleFactura(models.Model):
    factura = models.ForeignKey('Factura', related_name='detalles', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.PositiveIntegerField()
    descuento = models.PositiveIntegerField(default=0)
    
    @property
    def subtotal(self):
        return (self.precio_unitario * self.cantidad) - self.descuento
    
    def __str__(self):
        return f"{self.descripcion} - Cantidad: {self.cantidad}"

class FacturaEstado(models.Model):
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.estado
