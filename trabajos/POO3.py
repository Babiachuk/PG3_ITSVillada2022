class Triangulo:

    def inicializar(self):
        self.lado1 = int(input("ingrese la medida de un lado del triangulo: "))
        self.lado2 = int(input("ingrese otra medida: "))
        self.lado3 = int(input("ingrese una ultima medida: "))

    def ladoMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            print("el lado mayor es:", self.lado1)
        if self.lado2 > self.lado1 and self.lado2 > self.lado3:
            print("el lado mayor es:", self.lado2)
        if self.lado3 > self.lado2 and self.lado3 > self.lado1:
            print("el lado mayor es:", self.lado3)

        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("son todos iguales ??")

    def esEquilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("tu triangulo es equilatero :)")
        else:
            print("tu triangulo no es equilatero :(")


triangulo1 = Triangulo()
triangulo1.inicializar()
triangulo1.ladoMayor()
triangulo1.esEquilatero()
