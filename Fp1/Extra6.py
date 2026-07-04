#Un fichero de entrada contiene texto cualquiera. Dentro del texto pueden aparecer DNIs 
# con estos formatos válidos:

#12345678A
#12345678-A
#12345678 A

#Es decir: 8 dígitos + opcionalmente espacio o guion + una letra mayúscula

#Escribe una función:

#--def recuperar_dnis(fichero_entrada, fichero_salida):--

#La función debe:

# - Leer todo el contenido del fichero de entrada.
# - Buscar todos los DNIs válidos.
# - Normalizar cada DNI quitando espacios o guiones.
# - Escribir en el fichero de salida una línea por cada DNI encontrado con este formato:
# - DNI_normalizado:DNI_original

#Al final escribir: Normalizados: X, Total: Y

#Donde:

#X = número de DNIs cuyo formato cambió
#Y = número total de DNIs encontrados


import re


def recuperar_dnis(fichero_entrada, fichero_salida):
    total = 0
    normalizados = 0
    
    patron_dni = r"[0-9]{8}[- ]?[A-Z]"
    
    with open(fichero_entrada, "r") as entrada:
        texto = entrada.read()
    
    dnis = re.findall(patron_dni, texto)
    
    with open(fichero_salida, "w") as salida:
        for dni in dnis:
            dni_normal = dni.replace("-", "")
            dni_normal = dni_normal.replace(" ", "")
            
            if dni_normal != dni:
                normalizados += 1
            total += 1
            
            salida.write(f"{dni_normal}:{dni}\n")
        salida.write(">>>>>>>>>>\n")
        salida.write(f"Normalizados: {normalizados}, Total: {total}\n")
