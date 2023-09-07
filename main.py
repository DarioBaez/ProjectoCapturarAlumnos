import Buscador, Capturar, Listar
from Capturar import AlumnosCaptured

#Funcion menu
def Menu():
    while True:
        print("                 MENU                  \n",
              "1) Capturar alumno\n", "2) Buscar alumno\n", "3) Listar alumnos\n", "4) Salir")
        Opcion = int(input("Seleccione una opcion... "))
        if Opcion == 1:
            AlumnosCaptured()
        elif Opcion == 2:
            BuscarAlu()
        elif Opcion == 3:
            ListarALu()
        else:
            break
    
    print("BYE")


        
Menu()