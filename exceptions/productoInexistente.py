class ProductoInexistente(Exception):
    def __init__(self, message="El producto no existe en el menú."):
        self.message = message
        super().__init__(self.message)