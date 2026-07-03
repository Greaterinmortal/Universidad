import re


def validar_codigo(codigo):
    patron = r"[A-Z]{2}[- ]?\d{4}"
    if re.fullmatch(patron, codigo):
        nuevo = codigo.replace("-", "")
        nuevo = nuevo.replace(" ", "")
        return nuevo
    else:
        return None


lista_codigos = ["AB1234", "XY-0001", "fp2026", "FP 2026", "ABC1234", "ZZ9999"]
def codigos_validos(lista_codigos):
    lista = []
    for codigo in lista_codigos:
        normalizado = validar_codigo(codigo)
        if normalizado is not None:
            lista.append(normalizado)
    return lista
   
if __name__ == "__main__":
    lista_codigos = ["AB1234", "XY-0001", "fp2026", "FP 2026", "ABC1234", "ZZ9999"]
    print(codigos_validos(lista_codigos))