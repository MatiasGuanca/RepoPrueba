# Funciones para: generar una lista de 50 números aleatorios del 1 al 100
# Recibir una lista como parámetro y devolver true si contiene elementos repetidos 
# Recibir una lista como parámetro y devolver una lista nueva con los elementos únicos de la lista 
import random 

def generar_lista_random():
    lista_random = []
    for i in range(100):
        lista_random.append(random.randint(1,100))
    return lista_random

#generar_lista_random()

def evaluar_repetidos(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(i != j and lista[i] == lista[j]):
                return True
    return False

print(evaluar_repetidos([1,1,2,3,4,5,6]))

def limpiar_repetidos(lista):
    copia = []
    if (evaluar_repetidos(lista)):
        for i in range(len(lista)):
            if(lista[i] not in copia):
                copia.append(lista[i])      
    return copia

print(limpiar_repetidos([1,1,2,3,4,4,5,6]))