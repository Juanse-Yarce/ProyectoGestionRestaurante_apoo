class Plato:
    def __init__(self, id: int, nombre: str, descripcion: str, categoria: str, precio: float, stock: bool):
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: bool = stock
        self.vendidos: int = 0