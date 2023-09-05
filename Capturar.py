#Este escript busca capturar a los alumnos en una base de datos

#Esta funcion solicitara los datos a capturar de los alumnos
def AlumnosCaptured():
    pass


#Objeto alumno
class Alumno():
    def __init__(self, Nombre, Semestre, Carrera):
        self.Name = Nombre
        self.Semestre = Semestre
        self.Carrera = Carrera
    def getNombre(self):
        return self.Name
    def getSemestre(self):
        return self.Semestre
    def getCarrera(self):
        return self.Carrera
    

Alu = Alumno("Estaban",2,"ITICS")


