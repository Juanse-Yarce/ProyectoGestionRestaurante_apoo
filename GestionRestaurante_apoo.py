class Plato:
    def __init__(self, id: int, nombre: str, descripcion: str, categoria: str, precio: float, stock: int) -> None:
        self.id: int = id
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: int = stock
        self.vendidos: int = 0

    def actualizar_stock(self, cantidad: int) -> None:
        self.stock += cantidad


class Mesa:
    def __init__(self, numero: int, capacidad: int) -> None:
        self.numero: int = numero
        self.capacidad: int = capacidad
        self.estado: str = "Disponible"

    def cambiar_estado(self, estado: str) -> None:
        self.estado = estado