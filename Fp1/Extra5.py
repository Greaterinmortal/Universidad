#Se tiene esta estructura:

datos_academicos = (
    {
        "FP1": ("Fundamentos de Programación I", 1, 6),
        "MAT": ("Matemáticas", 1, 9),
        "BD": ("Bases de Datos", 2, 6)
    }, #Asignaturas
    {
        "11111111A": "Ana López",
        "22222222B": "Luis Pérez",
        "33333333C": "Marta Ruiz"
    }, #Estudiantes
    {
        "FP1": {
            "11111111A": 7.5,
            "22222222B": 9.0,
            "33333333C": 6.0
        },
        "MAT": {
            "11111111A": 5.0,
            "33333333C": 8.5
        },
        "BD": {}
    } #Notas
)

#Escribe una función:

#--def mejor_estudiante(datos_academicos, codigo):--

#La función debe devolver: (nombre_estudiante, nota) del estudiante con la nota más alta en la asignatura indicada por codigo.

#Casos especiales:

#Si codigo no existe en el diccionario de asignaturas, debe devolver: "NO ASG"
#Si codigo existe pero no tiene notas, debe devolver: "NO NOTAS"


def mejor_estudiante(datos_academicos, codigo):
    asignaturas = datos_academicos[0]
    estudiantes = datos_academicos[1]
    notas = datos_academicos[2]
    
    if codigo not in asignaturas:
        return "NO ASG"
    
    if codigo not in notas:
        return "NO NOTAS"
    
    cod_notas = notas[codigo]
    if len(cod_notas) == 0:
        return "NO NOTAS"
    
    mejor_nota = None
    mejor_dni = None
    
    for dni in cod_notas:
        nota = cod_notas[dni]
        if mejor_nota is None or nota > mejor_nota:
            mejor_nota = nota
            mejor_dni = dni
    
    nombre = estudiantes[mejor_dni]
    return (nombre, mejor_nota)


if __name__ == "__main__":
    print(mejor_estudiante(datos_academicos, "FP1"))
    # ("Luis Pérez", 9.0)

    print(mejor_estudiante(datos_academicos, "MAT"))
    # ("Marta Ruiz", 8.5)

    print(mejor_estudiante(datos_academicos, "BD"))
    # "NO NOTAS"

    print(mejor_estudiante(datos_academicos, "FIS"))
    # "NO ASG"