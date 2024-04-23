def Take_values():
    # funcion que recibe las notas
    notas = []
    for i in range(3) :
        nota = float(input(f"Intradusca nota de alumno del trimestre {i + 1}: "))
        notas.append(nota)
    return notas

def Average_calculator(Notas) :
    # funcion calcular pormedio de notas 
    return sum(Notas)/len(Notas)

def Approved_reprobate(pormedio) :
    if pormedio >= 5:
        print("el estudiante esta Aprobado con una nota de ", promedio)
    else :
        print("el estudiante esta Reprobado, tiene que estudiar mas")

print("Bienvenido al anilizador de notas de Estudiante")
notas =Take_values()
promedio = Average_calculator(notas)
Approved_reprobate(promedio)