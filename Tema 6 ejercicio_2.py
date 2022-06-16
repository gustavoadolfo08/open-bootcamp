class Alumno:
    def definir(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def verificar(self):
        if self.nota < 10:
            print("Lo siento, Usted reprobo")
        else:
            print("Felicidades, Usted aprobo")

    def imprimealumno(self):
        print("Nombre y Apellido:", self.nombre," ", "Nota Final:", self.nota)

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.definir("Gustavo Gomez",18)
alumno2.definir("Mariolbi Carrera", 9)

alumno1.imprimealumno()
alumno1.verificar()
alumno2.imprimealumno()
alumno2.verificar()
