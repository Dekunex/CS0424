
import math

def PerimetroQuadrato(lato):
    return 4 * lato

def PerimetroCerchio(raggio):
    return 2 * math.pi * raggio

def PerimetroRettangolo(base, altezza):
    return 2 * (base + altezza)

def main():
    print("Calcoliamo i perimetri di diverse forme geometriche: ")
    print("1) Quadrato")
    print("2) Cerchio")
    print("3) Rettangolo")
    
    scelta = input("Inserisci un numero: ")
    
    if scelta == "1":
        lato = float(input("Inserisci la lunghezza del lato: "))
        perimetro = PerimetroQuadrato(lato)
        print(f"il perimetro del Quadrato è: {perimetro}")
        
    elif scelta == "2":
        raggio = float(input("Inserisci il raggio del cerchio: "))
        perimetro = PerimetroCerchio(raggio)
        print(f"il raggio del cerchio è: {perimetro} ")
    
    elif scelta == "3":
        base = float(input("Inserisci la base del rettangolo: ")) 
        altezza = float(input("Inserisci la lunghezza del rettangolo:  "))
        perimetro = PerimetroRettangolo(base, altezza)
        print(f"Il perimetro del rettangolo è {perimetro}") 
               
    else:
         print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()