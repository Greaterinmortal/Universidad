def componer_fila(fila_roja, fila_verde, fila_azul):
    fila_resultado = []
    for posicion in range(len(fila_roja)):
        r = fila_roja[posicion]
        g = fila_verde[posicion]
        b = fila_azul[posicion]
        pixel = (r, g, b)
        fila_resultado.append(pixel)
    return fila_resultado

def componer_imagen(componentes):
    rojos = componentes[0]
    verdes = componentes[1]
    azules = componentes[2]
    
    imagen_resultado = []
    
    for pos in range(len(rojos)):
        fila_rgb = componer_fila(
            rojos[pos],
            verdes[pos],
            azules[pos]
        )
        imagen_resultado.append(fila_rgb)
    return imagen_resultado
