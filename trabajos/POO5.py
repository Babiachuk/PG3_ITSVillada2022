class Persona:
    def __init__(self):
        self.nombre = input("Ingrese un nombre: ")
        self.edad = int(input("ingrese una edad: "))
        self.impresion()

    def impresion(self):
        print("tu nombre es", self.nombre, "y tenes", self.edad, "años")


persona1 = Persona()


class Empleado(Persona):

    def __init__(self):
        self.sueldo = int(input("ingrese su sueldo: "))
        self.verificarImpuestos()

    def verificarImpuestos(self):
        if self.sueldo > 3000:
            print("tenes que pagar Impuestos")


empleado1 = Empleado()
