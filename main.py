import Buscador, Capturar, Listar
from Capturar import AlumnosCaptured
<<<<<<< HEAD
from Listar import ListarAlu
from Buscador import BuscarAlu
=======
>>>>>>> 198f7c846783c4fa10aeb998e11b91abf3d49d90

#Funcion menu
def Menu():
    while True:
<<<<<<< HEAD
        print("\n\n----------------------------------------------\n                 MENU                  \n",
              "1) Capturar alumno\n", "2) Buscar alumno\n", "3) Listar alumnos\n", "4) Salir")
        try:
            Opcion = int(input("Seleccione una opcion... "))
        except ValueError:
            print("Esa opcion no existe")
            break
        
        if Opcion == 1:
            AlumnosCaptured()
        elif Opcion == 2:
            print("Seleccione el parametro por el cual hara la busqueda\n", 
                  "1) Nombre\n", "2) Carrera\n", "3) Semestre\n", "4) N0 Control\n", "5) RFC")
            try:
                BuscarAlu(int(input("Selecciona una opcion... ")))
            except ValueError:
                print("Esa opcion no existe")
                break
        elif Opcion == 3:
            ListarAlu()                     
=======
        print("                 MENU                  \n",
              "1) Capturar alumno\n", "2) Buscar alumno\n", "3) Listar alumnos\n", "4) Salir")
        Opcion = int(input("Seleccione una opcion... "))
        if Opcion == 1:
            AlumnosCaptured()
        elif Opcion == 2:
            BuscarAlu()
        elif Opcion == 3:
            ListarALu()
>>>>>>> 198f7c846783c4fa10aeb998e11b91abf3d49d90
        else:
            break
    
    print("BYE")


        
Menu()