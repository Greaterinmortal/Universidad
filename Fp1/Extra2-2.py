#Se tiene una matriz de temperaturas:

temperaturas = [
    [22, 25, 28, 31],
    [19, 21, 20, 23],
    [30, 32, 29, 35]
]

#Escriba una función:

#def guardar_dias_calor(nombre_fichero):

#que cree un fichero de texto cuyo nombre viene dado por nombre_fichero.

#En el fichero deben escribirse solo las temperaturas mayores estrictas que limite.

#Cada línea tendrá este formato: fila;columna;temperatura

from Extra2 import dias_calor


def guardar_dias_calor(temperaturas, limite, nombre_fichero):
        lista_temp = dias_calor(temperaturas, limite)
        
        with open(nombre_fichero, "w") as fichero:
            for dato in lista_temp:
                fila = dato[0]
                columna = dato[1]
                temp = dato[2]
                linea = f"{fila};{columna};{temp}\n"
                fichero.write(linea)


if __name__ == "__main__":
    temperaturas = [
    [22, 25, 28, 31],
    [19, 21, 20, 23],
    [30, 32, 29, 35]
]
    guardar_dias_calor(temperaturas, 24, "calor.txt")
