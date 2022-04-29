numero = (input("ingrese el numero para analizar: "))


def isStep(numero):
    for i in range(0, len(numero)):
        if int(numero[i]) - int(numero[i + 1]) == 1 or int(numero[i]) - int(numero[i + 1]) == -1:
            return True
        else:
            return False


if isStep(numero):
    print("el numero es step")
else:
    print("el numero no es step")
