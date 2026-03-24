from Clases.EquipoObra import EquipoObra

class VibradorConcreto(EquipoObra):
    def __init__(self, nombre, identificador, consumo, estado, frecuenciaVibracion):
        super().__init__(nombre, identificador, consumo, estado)
        self.frecuenciaVibracion = frecuenciaVibracion

    def vibrar(self):
        print("El vibrador está compactando el concreto")

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Frecuencia: {self.frecuenciaVibracion} Hz")