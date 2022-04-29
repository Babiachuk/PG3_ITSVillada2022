frase = input("frase a ingresar:")


def contVocales(frase):
    vocales = 0
    for i in range(0, int(len(frase))):
        if frase[i] == "a" or frase[i] == "e" or frase[i] == "i" or frase[i] == "o" or frase[i] == "u":
            vocales += 1
    print("tu frase contiene:", vocales, "vocales")


contVocales(frase)
