año = int(input("ingrese el año a verificar:"))


def bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:  # si no es multiplo de 100
            if año % 400 == 0:
                print("el año es bisiesto")
            else:
                print("el año no es bisiesto")
        else:
            print("el año es bisiesto")
    else:
        print("el año no es bisiesto")


bisiesto(año)
