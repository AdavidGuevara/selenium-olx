class Vehiculo():
    def __init__(self, titulo, precio, detalle, ubicacion):
        self.titulo = titulo
        self.precio = precio
        self.detalle = detalle
        self.ubicacion = ubicacion


    def mostrarVehiculo(self):
        return {"titulo": self.titulo, "precio": self.precio, "detalle": self.detalle, "ubicacion": self.ubicacion}
