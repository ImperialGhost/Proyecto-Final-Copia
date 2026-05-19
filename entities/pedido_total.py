from typing import List
from entities.subtotal_producto import SubtotalProducto

# la libreria typing se utiliza para proporcionar soporte para anotaciones de tipo en Python.
# en este caso la usamos debido a que la lista de productos debe tener solo un tipo de dato.

class Pedido:


    
    iva = 0.16

    def __init__(self):
        self.productos: List[SubtotalProducto] = []

    def agregar_item(self, producto: SubtotalProducto, cantidad: int):
        nuevo_item = SubtotalProducto(producto, cantidad)
        self.productos.append(nuevo_item)

    # el @property lo usamos para definir los metodos como propiedades, de manera que podemos acceder a ellos
    # como si fuesen atributos sin la necesidad de estarlos llamando como funciones. :D

    @property
    def suma_subtotales(self):
        return sum(item.subtotal_neto for item in self.productos)

    @property
    def monto_iva(self):
        return self.suma_subtotales * self.iva

    @property
    def total_final(self):
        return self.suma_subtotales + self.monto_iva
    
    
    def vaciar_pedido(self):
  
         self.productos = []