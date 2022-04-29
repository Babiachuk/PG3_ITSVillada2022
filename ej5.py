str = input("ingrese una palabra para analizar: ")


def capicua(str):
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return print("no es capicua")
    return print("es capicua")


capicua(str)
