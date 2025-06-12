from conversores.longitud import metros_a_kilometros, pulgadas_a_centimetros
from conversores.temperatura import celsius_a_fahrenheit
from conversores.masa import gramos_a_kilos

def main():
    print("Conversor de Unidades")
    print("1.Metros a KM")
    print("2.Pulgadas a CM")
    print("3.Celsis a Fahrenheit")
    print("4.Gramos a kilos")
    opcion = input("Elige una opción entre estas 4:")
    
    if opcion == "1":
        metros = float(input("Introduce metros: "))
        print(f"{metros} metros son {metros_a_kilometros(metros)}kilometros ")
    elif opcion == "2":
        pulgadas = float(input("Introduce pulgadas: "))
        print(f"{pulgadas}pulgadas son {pulgadas_a_centimetros(pulgadas)}centimetros")
    elif opcion == "3":
        celsius = float(input("Introduce los grados celsius: "))
        print(f"{celsius}ºC  son {celsius_a_fahrenheit(celsius)}ºF")
    elif opcion == "4":
        masa = float(input("Introduce la masa: "))
        print(f"{masa} gramos son{gramos_a_kilos(masa)} kilogramos")
    else:
        print("Opción no válida")
    
if __name__ == "__main__":
    main()
    