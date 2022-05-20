class Operacion:
    def __init__(self):
        self.numero = int(input("ingrese un numero: "))
        self.numero2 = int(input("ingrese otro numero: "))
        self.sumaEnteros()
        self.restaEnteros()
        self.multiplicacionEnteros()
        self.divisionEnteros()

    def sumaEnteros(self):
        suma = self.numero + self.numero2
        print("La suma de tus enteros es: ", suma)

    def restaEnteros(self):
        resta = self.numero - self.numero2
        resta2 = self.numero2 - self.numero
        print("la resta de tus enteros es: ", resta, "o al reves: ", resta2)

    def multiplicacionEnteros(self):
        multiplicacion = self.numero * self.numero2
        print("la multiplicacion de tus enteros es: ", multiplicacion)

    def divisionEnteros(self):
        division = self.numero / self.numero2
        division2 = self.numero2 / self.numero
        print("la division de tus enteros es: ", division, "o al reves: ", division2)


operacion1=Operacion()
