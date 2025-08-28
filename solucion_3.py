#Librería para gestionar caracteres especiales
import re

#Función para encontrar la palabra más frecuente
def palabra_mas_frecuente(texto, lista_a_ignorar):

    #Obtener las palabras del texto y transformarlas a minúsculas
    palabras = texto.lower().split()

    #Inicializar la frecuencia de palabras
    frecuencia = {}

    #Recorrer todas la palabras del texto
    for palabra in palabras:

        #Eliminar caracters especiales
        palabra_limpia = re.sub(r"[^\w\s]", "", palabra)

        #Verificar que la palabra no esté en la lista a ignorar
        if palabra_limpia not in lista_a_ignorar:
            if palabra_limpia in frecuencia:
                frecuencia[palabra_limpia] += 1
            else:
                frecuencia[palabra_limpia] = 1

    #Obtener la palabra más frecuente
    palabra_frec = max(frecuencia, key=frecuencia.get)
    return palabra_frec


#Ingresar texto
texto_input = input("Ingresa el texto: ")
print("-------------------------------------------------")
#Inicializar lista de palabras a ignorar
lista_ign = []

#Número de palabras a ignorar
try:
    n_palabras_ign = int(input("Número de palabras a ignorar: "))
    print("-------------------------------------------------")
except ValueError:
    print("Debes ingresar un número válido.")
    n_palabras_ign = int(input("Número de palabras a ignorar: "))

#Solicitar palabras a ignorar
while len(lista_ign) + 1 <= n_palabras_ign:
    palabra_ign = input("Ingresa las palabra a ignorar: ")
    lista_ign.append(palabra_ign.lower())

#Mostrar las palabras más frecuente
print("-------------------------------------------------------------------------")
print(f"Palabra más frecuente: {palabra_mas_frecuente(texto_input, lista_ign)}")
print("-------------------------------------------------------------------------")

