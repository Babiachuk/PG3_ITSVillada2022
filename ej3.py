def INPUTEAME():
    ancho = int(input("ANCHO??: "))
    alto = int(input("ALTO??: "))
    caracter = (input("CARACTER??:"))

    forma = caracter
    for i in range(ancho-1):
        forma += caracter
    for i in range(alto):
        print(forma)




INPUTEAME()
