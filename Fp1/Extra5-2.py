#Usamos una estructura parecida:

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
            "22222222B": 9.0
        },
        "MAT": {
            "11111111A": 5.0,
            "33333333C": 8.5
        },
        "BD": {}
    } #Notas
)

#Escribe una función:

#  |  def actualizar_notas(datos_academicos, dni, nuevas_notas):  |  

#donde nuevas_notas es una lista de tuplas: [("FP1", 8.0), ("BD", 6.5), ("FIS", 9.0)] -> [(cod_asig, nota)]

#La función debe:

# - Si el dni no existe en el diccionario de estudiantes, no hacer nada.
# - Si el dni existe, actualizar el diccionario de notas.
# - Cada tupla de nuevas_notas tiene (codigo_asignatura, nota).
# - Si el código de asignatura existe en el diccionario de notas, se actualiza o se añade la nota.
# - Si el código no existe, se ignora.

#Ejemplo:

#actualizar_notas(datos_academicos, "33333333C", [("FP1", 6.5), ("BD", 7.0), ("FIS", 10)])

#Después de llamar a la función:

#datos_academicos[2]["FP1"]["33333333C"]  # 6.5
#datos_academicos[2]["BD"]["33333333C"]   # 7.0

#Pero "FIS" se ignora porque no existe.


def actualizar_notas(datos_academicos, dni, nuevas_notas):
    asignaturas = datos_academicos[0]
    estudiantes = datos_academicos[1]
    notas = datos_academicos[2]
    
    if dni not in estudiantes:
        return "No existe dni"
    
    for tupla in nuevas_notas:
        cod_asig = tupla[0]
        new_nota = tupla[1]
        if cod_asig in notas:
            cod_notas = notas[cod_asig]
            cod_notas[dni] = new_nota


if __name__ == "__main__":
    actualizar_notas(datos_academicos, "33333333C", [("FP1", 6.5), ("BD", 7.0), ("FIS", 10)])

    print(datos_academicos[2]["FP1"])
    print(datos_academicos[2]["BD"])