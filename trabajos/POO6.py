class Familia:
    def __init__(self):
        self.padre = input("ingrese el nombre del padre: ")
        self.madre = input("ingrese el nombre de la madre: ")
        self.hijos = []
        n = int(input("ingresa el numero de hijos: "))
        for i in range(0, n):
            print("ingresa el nombre de un hijo", i, )
            item = input()
            self.hijos.append(item)
        print("el nombre de tus hijos es: ", self.hijos)

    def __str__(self):
        cadena = "los nombres de tu familia son: " + self.padre + "," + self.madre
        for i in self.hijos:
            cadena = cadena + "," + i
        return cadena


familia1 = Familia()

print(familia1)
