class CantidadInvalida(Exception):
    def __init__(self, message="La cantidad debe ser un número mayor a 0."):
        self.message = message
        super().__init__(self.message)