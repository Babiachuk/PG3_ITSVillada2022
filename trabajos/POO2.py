class Alumno():

    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("nombre: ",self.nombre)
        print("nota: ",self.nota)

    def estado(self):
        if self.nota >= 4:
            print("Regular")
        else:
            print("Libre")

alumno1= Alumno()
alumno2= Alumno()
alumno1.inicializar("juan",5)
alumno2.inicializar("alejo",3)
alumno1.imprimir()
alumno1.estado()
alumno2.imprimir()
alumno2.estado()