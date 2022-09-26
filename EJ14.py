direccion = input("Ingrese su dirección de correo.").lower()

def verifyUser(array):
    if search(array)==True:
        for i in range(len(array)):
            if array[i] == "@":
                slice=array[0:i]
                slice2=array[i:-7]
                if slice.isalnum() == True and len(slice2)>=1:
                    return True, slice2
                else:
                    return False
                
def search(array):
    arr=0
    for x in array:
        if x == "@":
            arr+=1
    if arr == 1:
        return True
    else:
        return False
    
def verifyComAr(array):
    slice=array[-7:] 
    if slice == ".com.ar":
        return True
    else:
        return False
    
def verifyMail(array):
    if search(array) and verifyComAr(array) and verifyUser(array):
        print("El mail es valido")
    else:
        print("El mail es invalido")

listaDom=[]

while direccion != "":
    verifyMail(direccion)
    listaDom.append(verifyUser(direccion)[1])
    sortedLista = sorted(listaDom)
    
    direccion = input("Ingrese su dirección de correo.").lower()
    
print(sortedLista)
    
    
