class PedidoTotal:
    Iva = 0.16
    def __init__(self, cliente: str, productos: list):
        self.cliente = cliente
        self.productos = productos

    def agregarProducto(self, producto):
        self.productos.append(producto)