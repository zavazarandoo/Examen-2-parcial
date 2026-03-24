from ClasesDerivadas.mezcladoraConcreto import MezcladoraConcreto
from ClasesDerivadas.vibradorconcreto import VibradorConcreto

def main():
    
    m = MezcladoraConcreto("Mezcladora de Concreto", "EO001", 8, "Operativo", 0.5)
    
    m.iniciar()  
    m.mezclar()
    m.detener()
    m.mostrarInformacion()
    print("-" * 40)

   
    v = VibradorConcreto("Vibrador de Concreto", "EO002", 3, "Operativo", 120)
    
    v.iniciar()  
    v.vibrar()
    v.detener()
    v.mostrarInformacion()
    
if __name__ == "__main__":
    main()