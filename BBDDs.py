#Este script hara la conexion a la BBDD, enviara y recibira informacion
import sqlite3

def ENVIARBBDD(Alumno):
    C = sqlite3.connect('ALUMNOS ITSANJUAN.db')
    cursor = C.cursor()

    
    NControl = (Alumno.getNControl())
    Nombre = (Alumno.getNombre())
    Semestre = (Alumno.getSemestre())
    Carrera = (Alumno.getCarrera())
    Rfc = (Alumno.getRfc())
    
    datos = [NControl, Nombre, Semestre, Carrera, Rfc]
    print(datos)
<<<<<<< HEAD
    try:
        cursor.execute(f"INSERT INTO alumnos VALUES (?, ?, ?, ?, ?)", datos)
        C.commit()
    except sqlite3.IntegrityError:
        print("La key no puede repetirse, el numero de control debe cambiar")
    finally:
        C.close()


def Select(Columna, Valor):

    C = sqlite3.connect('ALUMNOS ITSANJUAN.db')
    cursor = C.cursor()
    if Columna == 0:

        cursor.execute(f"SELECT * FROM alumnos")
        resultados = cursor.fetchall()
        

    elif Columna != 0:

        cursor.execute(f"SELECT * FROM alumnos WHERE {Columna} = ?", (Valor,))
        #cursor.execute(f"SELECT * FROM alumnos WHERE {Columna} = {Valor}")
        resultados = cursor.fetchall()

    C.close()
    return resultados
    

    
=======
    cursor.execute(f"INSERT INTO alumnos VALUES (?, ?, ?, ?, ?)", datos)
    C.commit()
    C.close()

def Abrir():
    C = sqlite3.connect('ALUMNOS ITSANJUAN.db')
    cursor = C.cursor()
    cursor.execute(f"")
    C.close()
>>>>>>> 198f7c846783c4fa10aeb998e11b91abf3d49d90







<<<<<<< HEAD
#Asi se creo la BBDD en sqlite3, Nombre de la tabla y columnas
=======



>>>>>>> 198f7c846783c4fa10aeb998e11b91abf3d49d90

"""
C = sqlite3.connect('ALUMNOS ITSANJUAN.db')
cursor = C.cursor()

# Crear la tabla
cursor.execute('''
    CREATE TABLE alumnos (
        NControl INTEGER PRIMARY KEY,
        Nombre TEXT,
        Semestre INTEGER,
        Carrera TEXT,
        Rfc TEXT
    )
''')

# Cerrar la conexión a la base de datos
C.close()
"""