from enums.tipoProducto import TipoProducto


class Producto:
    def __init__(self, idProducto: int, nombre: str, precio: float, tipo: TipoProducto):
        self.idProducto = idProducto
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo