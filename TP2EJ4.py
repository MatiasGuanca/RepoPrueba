'''
Eliminar de una lista de palabras que se encuentren en una segunda lista.
Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.
'''

from curses.ascii import isalpha


def EliminarPalabras (listaOriginal,listaEliminar):
    for i in range(len(listaOriginal)):
        if listaOriginal[i] in listaEliminar:
            listaOriginal.remove(listaOriginal[i])
            encontro=True
            break
        else:
            encontro=False
    return listaOriginal,encontro

'''en esta función se generan las listas con las palabras ingresadas por el usuario'''
def ArmarListas():
    seguir = "s"
    primerLista=[]
    segundaLista=[]

    while seguir=="s":
        print("Lista de palabras hasta al momento",primerLista)
        inputUsuario = input("Ingrese palabra a añadir en la lista: ").lower()
        while inputUsuario.isdigit():
            inputUsuario = input("ERROR. Ingrese una palabra valida a añadir en la lista: ").lower()

        primerLista.append(inputUsuario)
        seguir=input("¿Desea continuar? s/n").lower()

    seguir = "s"
    while seguir=="s":
        print("Lista de palabras a remover hasta el momento",segundaLista)
        inputUsuario = input("Ingrese palabra a añadir en la lista: ").lower()
        while inputUsuario.isdigit():
            inputUsuario = input("ERROR. Ingrese una palabra valida a añadir en la lista: ").lower()

        segundaLista.append(inputUsuario)
        seguir=input("¿Desea continuar? s/n").lower()
    if len(primerLista) != 0 and len(segundaLista) != 0:
        return True,primerLista,segundaLista
    else:
        return False

def main():
    ''' Hardcodeo de las listas'''
    #primerLista = ["Manzana","Pera","Kiwi","Banana"] 
    #segundaLista = ["Manzana","Banana"]

    ''' Función para armar listas piendole las palabras al usuario '''
    listaCompleta = ArmarListas()
    if listaCompleta[0]==True:
        lista=listaCompleta[1]
        eliminarLista=listaCompleta[2]
        print("Lista original: ",lista,"\nLista de palabras a eliminar: ",eliminarLista)  

        seElimina=EliminarPalabras(lista,eliminarLista)
        if seElimina[1] == True:
            print("La lista con los elementos removidos es: ",seElimina[0])
        else:
            print("No se encontraron palabras a eliminar")
    else:
        "ERROR. No se han ingresado palabras para eliminjar"

main()





