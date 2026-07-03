#Se dispone de un diccionario llamado asignaturas que almacena información sobre varias asignaturas. 
#Las claves del diccionario son códigos de asignatura normalizados, y los valores asociados son tuplas 
#con el nombre de la asignatura y su número de créditos.

asignaturas = {
    "FP2026": ("Fundamentos de Programación", 6),
    "BD1001": ("Bases de Datos", 6),
    "MA0001": ("Matemáticas", 9),
    "PR1234": ("Programación", 6)
}

#Cada código válido tiene el siguiente formato: 2 letras mayúsculas seguidas de 4 dígitos
#Además, el código puede aparecer escrito con un guion o un espacio entre las letras y los números.

#Ejemplos válidos:

#FP2026
#FP-2026
#FP 2026

#Todos ellos deben normalizarse al formato:

#FP2026

#Ejemplos inválidos:

#fp2026
#F2026
#FPP2026
#FP20
#FP20267

#Se dispone también de una lista de códigos escritos por un usuario:

codigos = ["FP-2026", "BD1001", "xx9999", "MA 0001", "PR1234", "AB1234"]

#Escriba una función llamada:

#--def creditos_validos(asignaturas, codigos):--

#que reciba como parámetros:

#- El diccionario asignaturas.
#- Una lista de códigos de asignatura.

#La función debe devolver la suma total de créditos de aquellos códigos que:

#- Tengan un formato válido.
#- Una vez normalizados, existan como clave en el diccionario asignaturas.

#Los códigos con formato incorrecto deben ignorarse.
#Los códigos válidos que no aparezcan en el diccionario también deben ignorarse.

#Puedes usar la función auxiliar validar_codigo(codigo), 
# que devuelve el código normalizado si es válido, o None si no lo es.

from Extra1 import validar_codigo


def creditos_validos(asignaturas, codigos):
    total = 0
    
    for codigo in codigos:
        new_cod = validar_codigo(codigo)
        if new_cod is not None:
                if new_cod in asignaturas:
                    datos = asignaturas[new_cod]
                    creditos = datos[1]
                    total += creditos
    return total


if __name__ == "__main__":
    asignaturas = {
    "FP2026": ("Fundamentos de Programación", 6),
    "BD1001": ("Bases de Datos", 6),
    "MA0001": ("Matemáticas", 9),
    "PR1234": ("Programación", 6)
}
    codigos = ["FP-2026", "BD1001", "xx9999", "MA 0001", "PR1234", "AB1234"]
    print(creditos_validos(asignaturas, codigos))