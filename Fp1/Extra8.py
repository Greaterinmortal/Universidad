#Se tiene un fichero de texto que contiene información de estudiantes. 
# Cada línea del fichero tiene el siguiente formato: DNI;nombre

#Ejemplo de fichero de entrada:

# 11111111A;Ana López
# 22222222B;Luis Pérez
# 33333333C;Marta Ruiz
# 44444444D;Carlos Pérez

#Además, se tiene un diccionario en memoria llamado notas, cuyas claves son DNIs de estudiantes 
#y cuyos valores son sus calificaciones.

#Ejemplo:

notas = {
    "12345678A": 8.5,
    "87654321B": 9.2,
    "11223344C": 6.7,
    "55667788D": 4.5,
    "99887766E": 7.8,
    "22334455F": 5.9,
    "66778899G": 3.4,
    "33445566H": 8.1,
    "00112233J": 10.0,
    "44556677K": 6.2,
    "77889900L": 7.4,
    "55443322M": 9.5,
    "99001122N": 4.0,
    "33221100P": 5.0,
    "88779955Q": 6.8,
    "22114433R": 7.2,
    "66554411S": 2.5
}

#Escribe una función:

#  |  def generar_informe_notas(fichero_entrada, fichero_salida, notas):  |

#La función debe leer el fichero de entrada y crear un fichero de salida.

#Por cada estudiante del fichero de entrada, debe escribir una línea en el fichero de salida
#con el siguiente formato: DNI;nombre;nota

#Si el DNI del estudiante no aparece en el diccionario notas, se debe escribir: DNI;nombre;SIN NOTA

#Al final del fichero de salida se debe escribir una línea separadora:

#----------

#Y después una línea resumen con este formato: Con nota: X, Sin nota: Y

#Donde:

# X = número de estudiantes que sí tenían nota en el diccionario
# Y = número de estudiantes que no tenían nota en el diccionario

#Ejemplo de salida para los datos anteriores:

# 11111111A;Ana López;7.5
# 22222222B;Luis Pérez;4.0
# 33333333C;Marta Ruiz;9.0
# 44444444D;Carlos Pérez;SIN NOTA
# ----------
# Con nota: 3, Sin nota: 1


def generar_informe_notas(fichero_entrada, fichero_salida, notas):
    total_X = 0
    total_Y = 0
    
    with open(fichero_entrada, "r") as entrada:
        with open(fichero_salida, "w") as salida:
            for linea in entrada:
                linea = linea.rstrip()
                new_line = linea.split(";")
                
                dni = new_line[0]
                nombre = new_line[1]
                
                if dni in notas:
                    nota = notas[dni]
                    salida.write(f"{dni};{nombre};{nota}\n")
                    total_X += 1
                else:
                    salida.write(f"{dni};{nombre};SIN NOTA\n")
                    total_Y += 1
            salida.write(f"--------------------\n")
            salida.write(f"Con nota: {total_X}, Sin nota: {total_Y}")
