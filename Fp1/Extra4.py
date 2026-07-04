#Un fichero de entrada contiene texto cualquiera, por ejemplo:

#----------------------------------------------------------#
#Contacta con ana@gmail.com o con luis_23@ulpgc.es.
#Este no vale: .malo@correo.com
#Este tampoco: usuario@dominio.c
#Otro válido: nombre.apellido-01@empresa-tech.org
#----------------------------------------------------------#

#Escribe una función:

#--def extraer_correos(fichero_entrada, fichero_salida):--

#La función debe:

#Leer el contenido completo del fichero de entrada.
#Buscar todos los correos que tengan formato válido según el patrón del ejercicio anterior.
#Escribir en el fichero de salida un correo válido por línea.
#Al final, escribir una línea resumen con este formato:
#Total: X

#donde X es el número de correos válidos encontrados.

#Ejemplo de salida:

#ana@gmail.com
#luis_23@ulpgc.es
#nombre.apellido-01@empresa-tech.org
#Total: 3
#-----------------------------------------------------------------------------------------------------------------#
#Una dirección de correo electrónico tiene el siguiente formato básico:   user@hostname.tld  

#Donde:

#user está compuesto por una secuencia de bloques formados por uno o más caracteres mayúsculos, 
# minúsculos o dígitos del 0 al 9, en cualquier orden. Los bloques se pueden separar entre sí por un punto ., 
# un guion - o un guion bajo _.

#Ejemplos de user válidos:

#Name01-First.Last_user101
#201-user.lastname

#hostname se forma igual que user.

#tld es una secuencia de, como mínimo, dos letras, mayúsculas o minúsculas.

#Ejemplos de tld válidos:

#EU
#es
#org
#arpa
#parent



import re


def extraer_correos(fichero_entrada, fichero_salida):
    total = 0
    
    user = r"[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*"
    hostname = r"[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*"
    tld = r"[A-Za-z]{2,}"
    patron = user + r"\@" + hostname + r"\." + tld
    
    with open(fichero_entrada, "r") as entrada:
        texto = entrada.read()
        
    correos = re.findall(patron, texto)
    
    with open(fichero_salida, "w") as salida:
        for correo in correos:
            salida.write(f"{correo}\n")
            total += 1
        salida.write(f"Total: {total}\n")
