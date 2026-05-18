from entities.producto import Producto
from enums.tipo_producto import Tipo_producto

class SubtotalProducto:
    Descuentos = {
        Tipo_producto.BEBIDA: 0.10,
        Tipo_producto.COMIDA: 0.15,
        Tipo_producto.POSTRE: 0.20,
        Tipo_producto.OTRO: 0.05
    }

    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    @property
    def subtotal_bruto(self):
        return self.producto.precio * self.cantidad

    @property
    def monto_descuento(self):
        porcentaje = self.Descuentos.get(self.producto.tipo, 0)
        return self.subtotal_bruto * porcentaje

    @property
    def subtotal_neto(self):
        return self.subtotal_bruto - self.monto_descuento