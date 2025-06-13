from mi_conversor import metros_a_kilometros, pulgadas_a_centimetros, gramos_a_kilos,celsius_a_fahrenheit,fahrenheit_a_celsius


def main():
    print("Demostración de la libreria")
    
    print("1000 metros son:",metros_a_kilometros(1000),"kilometros")
    print("10 pulgadas son:",pulgadas_a_centimetros(10),"centimetros")
    print("0 º C son:",celsius_a_fahrenheit(0),"ºF")
    print("32 º F son:",fahrenheit_a_celsius(32),"ºC")
    print("3000 gramos son:",gramos_a_kilos(3000),"KG")
        
if __name__ == "__main__":
    main()
    