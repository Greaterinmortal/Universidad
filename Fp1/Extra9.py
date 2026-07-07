#Se tiene una estructura de datos académicos:

datos_academicos = (
    {
        "FP1": ("Fundamentos de Programación I", 1, 6),
        "MAT": ("Matemáticas", 1, 9),
        "BD": ("Bases de Datos", 2, 6),
        "FIS": ("Física", 2, 6)
    },
    {
        "11111111A": "Ana López",
        "22222222B": "Luis Pérez",
        "33333333C": "Marta Ruiz",
        "44444444D": "Carlos Díaz"
    },
    {
        "FP1": {},
        "MAT": {},
        "BD": {},
        "FIS": {}
    }
)

#La tupla contiene:

#posición 0 -> diccionario de asignaturas
#posición 1 -> diccionario de estudiantes
#posición 2 -> diccionario de calificaciones

#El diccionario de calificaciones tiene esta forma:

{
    "FP1": {
        "11111111A": 7.5,
        "22222222B": 4.0
    },
    "MAT": {
        "33333333C": 8.0
    }
}
#Fichero de entrada

#Se tiene un fichero de texto donde cada línea tiene este formato: DNI;CODIGO_ASIGNATURA;notas

#Las notas aparecen separadas por comas.

#Ejemplo de fichero:

#11111111A;FP1;7.0,8.0,9.0
#22222222-B;FP1;3.0,4.0,5.0
#33333333 C;MAT;8.5,9.0
#99999999Z;BD;6.0,7.0
#44444444D;XXX;10.0
#maldni;FIS;5.0,6.0
#11111111A;BD;4.0,6.0,8.0

#--Validez del DNI--

#Un DNI es válido si cumple: 8 dígitos + opcionalmente espacio o guion + una letra mayúscula

#Ejemplos válidos:

#11111111A
#22222222-B
#33333333 C

#Ejemplos no válidos:

#maldni
#123A
#11111111-a

#Si el DNI es válido, debe normalizarse quitando espacio o guion:

#22222222-B -> 22222222B
#33333333 C -> 33333333C
#Función pedida

#Escribe una función:

#def importar_calificaciones(datos_academicos, fichero_entrada, fichero_salida):

#La función debe leer el fichero de entrada y crear un fichero de salida.

##Reglas de procesamiento

#Para cada línea del fichero:

#La línea se considera correcta si se cumplen estas tres condiciones:

#1. El DNI tiene formato válido.
#2. El DNI normalizado existe en el diccionario de estudiantes.
#3. El código de asignatura existe en el diccionario de calificaciones.

#Si la línea es correcta:

#Convierte las notas a float.
#Calcula la media de las notas.
#Guarda esa media en el diccionario de calificaciones:
#calificaciones[codigo][dni_normalizado] = media
#Escribe en el fichero de salida: DNI_NORMALIZADO;CODIGO;MEDIA;OK

#Si la línea es incorrecta:

#No modifica el diccionario.
#Escribe en el fichero de salida:
#DNI_ORIGINAL;CODIGO;ERROR

#Resumen final
#Al final del fichero de salida debe escribirse:

#----------
#Procesadas: X
#Correctas: Y
#Incorrectas: Z
#Mejor media: DNI;CODIGO;MEDIA

#Donde:

#X = número total de líneas procesadas
#Y = número de líneas correctas
#Z = número de líneas incorrectas

#La mejor media es la media más alta entre todas las líneas correctas procesadas.

#Si no hay ninguna línea correcta, debe escribirse:

#Mejor media: SIN DATOS

import re


def importar_calificaciones(datos_academicos, fichero_entrada, fichero_salida):
    asignaturas = datos_academicos[0]
    estudiantes = datos_academicos[1]
    notas = datos_academicos[2]
    
    total_X = 0
    total_Y = 0
    total_Z = 0
    mejor_media = None
    mejor_dni = None
    mejor_codigo = None
    
    patron_dni = r"[0-9]{8}[- ]?[A-Z]"
    
    with open(fichero_entrada, "r") as entrada:
        with open(fichero_salida, "w") as salida:
            for linea in entrada:
                linea = linea.rstrip()
                new_line = linea.split(";")
                dni = new_line[0]
                cod_asig = new_line[1]
                nota = new_line[2]
                total_X += 1
                
                if re.fullmatch(patron_dni, dni):
                    dni_normal = dni.replace("-", "")
                    dni_normal = dni_normal.replace(" ", "")
                    
                    if dni_normal in estudiantes and cod_asig in notas:
                        notas_reales = nota.split(",")
                        
                        total = 0
                        for mark in notas_reales:
                            total += float(mark)
                        
                        media = total / len(notas_reales)
                        notas[cod_asig][dni_normal] = media
                        
                        salida.write(f"{dni_normal};{cod_asig};{media};OK\n")
                        total_Y += 1
                        
                        if mejor_media is None or media > mejor_media:
                            mejor_media = media
                            mejor_dni = dni_normal
                            mejor_codigo = cod_asig
                            
                    else:
                        salida.write(f"{dni};{cod_asig};ERROR\n")
                        total_Z += 1
                else:
                    salida.write(f"{dni};{cod_asig};ERROR\n")
                    total_Z += 1

            salida.write(f"-------------------------------\n")
            salida.write(f"Procesadas: {total_X}\n")
            salida.write(f"Correctas: {total_Y}\n")
            salida.write(f"Incorrectas: {total_Z}\n")
            
            if mejor_media is None:
                salida.write(f"Mejor media: SIN DATOS\n")
            else:
                salida.write(f"Mejor media: {mejor_dni};{mejor_codigo};{mejor_media}\n")
