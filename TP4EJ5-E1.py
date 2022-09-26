'''
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N, y devuelva otra cadena con palabras que tengan N 

o más caracteres de la cadena

original. Escribir también un programa para verificar el comportamiento de la misma. Hacer tres versiones de la función, para cada uno de los siguientes casos:

A- utilizando solo ciclos normales

B- utilizando listas por comprensión

C- utilizando la función filter

'''



def filtrarPalabrasA(cadena,entero):
    array=cadena.split(" ")
    length=len(array)
    for i in range(length):
        if len(array[i])>=entero:
            cadena=""
            cadena=cadena+array[i]
    return cadena

def filtrarPalabrasB(cadena,entero):
    array=cadena.split(" ")
    for i in array:
        if len(i)<entero:
            array.remove(i)
    cadena=' '.join(array)     
    return cadena 
    
    
def main():
    cadena="hola mundo chau"
    print(cadena)
    print(filtrarPalabrasA(cadena,5))
    print(filtrarPalabrasB(cadena,5))
    

main()