#CANTIDAD DE PERSONAS EN EL GRUPO
N = 4

#DICCIONARIO DE AMISTADES
amistades = {(1,2), (2,3), (1,4)}

#Función para retornar a las personas que son amigos
def A(i, j):

    if i == j:
        raise ValueError("Esta expresión no está permitida")
    
    if (i, j) in amistades or (j, i) in amistades:
        return True
    return False

#Función para verificar si hay un amigo en común
def comun(i, j):

    #Lanzar error en caso de detectar valores idénticos
    if i == j:
        raise ValueError("Esta expresión no está permitida")
    
    #Verificar que otra persona sea un amigo en común
    for k in range(1, N+1):

        #Saltar a la siguiente persona en caso de que los valores sean idénticos
        if k == i or k == j:
            continue

        #Retornar verdadero si hay un amigo en común
        if A(i, k) and A(j, k):
            return True
        
    #Retornar falso en caso de no haber un amigo en común 
    return False

try:
    print("---AMISTADES---")
    A1 = int(input("Persona I: "))
    A2 = int(input("Persona J: "))
    print(A(A1,A2))
    print("")

    print("---AMIGOS EN COMÚN---")
    C1 = int(input("Persona I: "))
    C2 = int(input("Persona J: "))
    print(comun(C1,C2))

except ValueError as e:
    #Atrapar el error para que no se caiga el programa
    print(e)

