class EquipoObra:
    def __init__(self, nombre, identificador, consumoCombustible, estado):
        self.nombre = nombre
        self.identificador = identificador
        self.consumoCombustible = consumoCombustible
        self.estado = estado

    def iniciar(self):
        self.estado = "operativo"
        print(f"El equipo {self.nombre} ha sido iniciado")

    def detener(self):
        self.estado = "detenido"
        print(f"El equipo {self.nombre} se ha detenido")

    def mostrarInformacion(self):
        print(f"Equipo: {self.nombre}")
        print(f"ID: {self.identificador}")
        print(f"Consumo: {self.consumoCombustible} L/h")
        print(f"Estado: {self.estado}")