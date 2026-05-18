from enums.tipo_producto import Tipo_producto


class Producto:
    def __init__(self, id_producto: int, nombre: str, precio: float, tipo: Tipo_producto):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo

    def __str__(self):
        return f"{self.nombre} ${self.precio}"