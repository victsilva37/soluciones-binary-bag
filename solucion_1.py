#Función para que reciba las instrucciones como parámetro
def vuelve(instrucciones):

    #Posición inicial
    posicion = 0

    #Iteración para mover al robot horizontalmente según las instrucciones
    for caracter in instrucciones:
        
        #Mover el robot un metro a la izquierda
        if caracter == 'I':
            posicion -=1
            
        #Mover al robot un metro a la derecha
        elif caracter == 'D':
            posicion +=1
            
    #Ver posición actual     
    print(f"Posición: {posicion}")

    #Retornar true si el robot vuelve a la posición inicial
    if posicion == 0:
        return True
    else:
        return False
    
#Instrucciones para mover al robot
instr = input('Ingrese las instrucciones: ')

#Pasar como parámetro las instrucciones ingresadas por el usuario
print(vuelve(instr))

    