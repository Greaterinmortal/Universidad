#Se tiene una matriz de temperaturas. Cada fila representa una ciudad y cada columna representa un día.

temperaturas = [
    [22, 25, 28, 31],
    [19, 21, 20, 23],
    [30, 32, 29, 35]
]

#Escribe una función:

#--def dias_calor(temperaturas, limite):--
#que devuelva una lista de tuplas con las posiciones donde la temperatura sea mayor estricta que limite.

#Cada tupla debe tener: (fila, columna, temperatura)

def dias_calor(temperaturas, limite):
    lista = []
    for ciudad in range(len(temperaturas)):
        for dia in range(len(temperaturas[ciudad])):
            temp = temperaturas[ciudad][dia]
            if temp > limite:
                tupla = (ciudad, dia, temp)
                lista.append(tupla)
    return lista

if __name__ == "__main__":
    temperaturas = [
    [22, 25, 28, 31],
    [19, 21, 20, 23],
    [30, 32, 29, 35]
]
    print(dias_calor(temperaturas, 24))