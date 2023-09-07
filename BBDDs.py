#Este script hara la conexion a la BBDD, enviara y recibira informacion
import sqlite3

def ENVIARBBDD(Alumno):
    C = sqlite3.connect('ALUMNOS ITSANJUAN.db')
    cursor = C.cursor()
    
    NControl = Alumno.getNControl()
    Nombre = Alumno.getNombre()
    Semestre = Alumno.getSemestre()
    Carrera = Alumno.getCarrera()
    Rfc = Alumno.getRfc()

    datos = [NControl, Nombre, Semestre, Carrera, Rfc]
    print(datos)
    cursor.execute(f"INSERT INTO alumnos VALUES (?, ?, ?, ?, ?)", datos)
    C.commit()
    C.close()






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