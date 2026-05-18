from entities.producto import Producto

class ProductoPedido:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def calcularSubtotal(self):
        return self.producto.precio * self.cantidad