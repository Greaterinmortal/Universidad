#Escribe una función en Python llamada:

#--def validar_correo(correo):--

#que reciba como parámetro una string que debería representar una dirección de correo electrónico 
# y verifique si es válida.

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

#La función debe devolver: True -> si el correo es válido, y: False -> si no lo es.

import re


def validar_correo(correo):
    user = r"[A-Za-z0-9]+([._-][A-Za-z0-9]+)*"
    hostname = r"[A-Za-z0-9]+([._-][A-Za-z0-9]+)*"
    tld = r"[A-Za-z]{2,}"
    patron = user + r"\@" + hostname + r"\." + tld
    
    if re.fullmatch(patron, correo):
        return True
    else:
        return False


if __name__ == "__main__":
    print(validar_correo("ejemplo@dominio.com"))          # True
    print(validar_correo("correo@sin_espacio.com"))       # True
    print(validar_correo(".invalid@correo.com"))          # False
    print(validar_correo("usuario@dominio con espacio.com")) #False