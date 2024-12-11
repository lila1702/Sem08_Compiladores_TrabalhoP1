class Token:
    def __init__(self, tipo, valor=None):
        self.tipo = tipo
        self.valor = valor
        
    def __repr__(self):
        if (self.valor is not None):
            return f"Token({self.tipo}, {repr(self.valor)})"
        return f"Token({self.tipo})"