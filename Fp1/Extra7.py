#Se tiene una estructura de datos académicos:

datos_academicos = (
    {
        "FP1": ("Fundamentos de Programación I", 1, 6),
        "MAT": ("Matemáticas", 1, 9),
        "BD": ("Bases de Datos", 2, 6)
    }, #Asignaturas
    {
        "11111111A": "Ana López",
        "22222222B": "Luis Pérez",
        "33333333C": "Marta Ruiz"
    }, #Estudiantes
    {
        "FP1": {
            "11111111A": 7.5,
            "22222222B": 9.0
        },
        "MAT": {
            "11111111A": 5.0,
            "33333333C": 8.5
        },
        "BD": {}
    } #Notas
)

#Un fichero de entrada contiene líneas con este formato:

#dni;codigo_asignatura;nota

#Ejemplo de fichero:

# 33333333-C;FP1;6.5
# 11111111A;BD;7.0
# 99999999Z;MAT;8.0
# 22222222 B;FIS;9.0
# maldni;FP1;5.0

#Escribe una función:

#  -|  def importar_notas(datos_academicos, fichero_entrada, fichero_salida):  |-

#La función debe leer el fichero de entrada y procesar cada línea.

#----Reglas----

#Un DNI es válido si cumple: 8 dígitos + opcionalmente espacio o guion + letra mayúscula

#Ejemplos válidos:

# 11111111A
# 33333333-C
# 22222222 B

#Si el DNI es válido, se debe normalizar quitando espacio o guion.

#Ejemplo:

# 33333333-C -> 33333333C
# 22222222 B -> 22222222B

#Una línea se actualiza solo si:

# - el DNI tiene formato válido
# - el DNI normalizado existe en estudiantes
# - el código existe en el diccionario de notas

#Si todo es correcto:

# notas[codigo][dni_normalizado] = nota

#Si algo falla, se ignora esa línea.

#---Fichero de salida---

#Por cada línea procesada, se debe escribir:

# - dni_normalizado;codigo;nota;OK -> si se actualizó correctamente, o: dni_original;codigo;nota;ERROR -> si se ignoró.

#Al final del fichero se debe escribir:

#  ----------
#  Actualizadas: X, Ignoradas: Y

import re


def importar_notas(datos_academicos, fichero_entrada, fichero_salida):
    asignaturas = datos_academicos[0]
    estudiantes = datos_academicos[1]
    notas = datos_academicos[2]
    
    total_X = 0
    total_Y = 0
    
    patron_dni = r"[0-9]{8}[- ]?[A-Z]"
    
    with open(fichero_entrada, "r") as entrada:
        with open(fichero_salida, "w") as salida:
            for linea in entrada:
                linea = linea.rstrip()
                new_line = linea.split(";")
                dni = new_line[0]
                cod_asig = new_line[1]
                nota = new_line[2]
                
                if re.fullmatch(patron_dni, dni):
                    dni_normal = dni.replace("-", "")
                    dni_normal = dni_normal.replace(" ", "")
                    
                    if dni_normal in estudiantes and cod_asig in notas:
                        nota_float = float(nota)
                        notas[cod_asig][dni_normal] = nota_float
                        salida.write(f"{dni_normal};{cod_asig};{nota};OK\n")     
                        total_X += 1                    
                    else:
                        salida.write(f"{dni};{cod_asig};{nota};ERROR\n")
                        total_Y += 1
                else:
                    salida.write(f"{dni};{cod_asig};{nota};ERROR\n")
                    total_Y += 1
                    
            salida.write(f"--------------------\n")
            salida.write(f"Actualizadas: {total_X}, Ignoradas: {total_Y}\n")
