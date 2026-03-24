from ClasesDerivadas.mezcladoraConcreto import MezcladoraConcreto
from ClasesDerivadas.vibradorconcreto import VibradorConcreto

def main():
   
    m = MezcladoraConcreto("Mezcladora de Concreto", "EO001", 8, "Operativo", 0.5)
    m.mostrarInformacion()
    m.mezclar()

    print("-" * 30)

    v = VibradorConcreto("Vibrador de Concreto", "EO002", 3, "Operativo", 120)
    v.mostrarInformacion()
    v.vibrar()

if __name__ == "__main__":
    main()