class Persona():

    def inicializar(self, nombre):
        self.nombre = nombre

    def imprimir(self):
        print("nombre: ", self.nombre)


persona1 = Persona()
persona1.inicializar("pancho")
persona2 = Persona()
persona2.inicializar("javier")
persona2.imprimir()
persona1.imprimir()
