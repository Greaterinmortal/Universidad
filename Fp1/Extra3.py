#Un fichero entrada.txt contiene temperaturas, una por línea:

#22
#31
#19
#35
#28

#Escribe una función:

#--def copiar_altas(fichero_entrada, fichero_salida, limite):--

#Que lea el fichero de entrada y escriba en el fichero de salida solo las temperaturas mayores que limite.
#Si llamamos:

#--copiar_altas("entrada.txt", "salida.txt", 30)--
#el fichero salida.txt debe quedar:

#31
#35

def copiar_altas(fichero_entrada, fichero_salida, limite):
    with open(fichero_entrada, "r") as entrada:
        with open(fichero_salida, "w") as salida:
            for linea in entrada:
                new_line = int(linea)
                if new_line > limite:
                    salida.write(f"{new_line} + \n")