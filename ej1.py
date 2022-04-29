lista = [12, 31, 67, 97, 45, 22]
print(lista)


def funcion(lista):
    for i in lista:

        try:
            numero = int(input("ingrese el numero deseado: "))
            print(lista.index(numero))
            pass
        except ValueError:
            print("el numero no esta en la lista")
        except KeyboardInterrupt:
            break


funcion(lista)
