from Clases.EquipoObra import EquipoObra

class MezcladoraConcreto(EquipoObra):
    def __init__(self, nombre, identificador, consumo, estado, capacidadTambor):
        super().__init__(nombre, identificador, consumo, estado)
        self.capacidadTambor = capacidadTambor

    def mezclar(self):
        print("La mezcladora está preparando concreto")

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Capacidad del tambor: {self.capacidadTambor} m3")