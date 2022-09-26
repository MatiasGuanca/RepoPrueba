#Resolver el siguiente problema, diseñando las funciones a utilizar:

#una clinica necesita un programa para atender a sus pacientes. Cada paciente que ingresa se anuncia en recepción indicando su numero de afiliado(numero entero de 4 digitos)
#y además indica si viene por una urgencia (ingresando un 0) o con un turno(ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego se solicita:

#A- Mostrar un listado de los pacientes atendidos por ugencia y un listado de los pacientes atendidos por turno en el orden que llegaron a la clinica.
#B- Realizar la busqueda de número de afiliado e informar cuántas veces fue atendido por turno y cuántas por ugencia.
#   repetir esta busqueda hasta que se ingrese -1 como número de afiliado

def VerifNum(num):
    if len(num)==4:
        return True
    else:
        return False
def BusquedaAfiliado(lista,afiliado):
    atendido=0
    for x in lista:
        if x == afiliado:
            atendido+=1
    return atendido
    
def PrintPacientes(lista1,lista2):
    print("Los pacientes atendidos por urgencia son:")

    if len(lista1)>0:
        for i in range(len(lista1)):
            print(lista1[i])
    else:
        print("No hay pacientes atendidos por urgencia\n")
        
    print("Los pacientes atendidos por turno son:")
    if len(lista2)>0:
        for i in range(len(lista2)):
            print(lista2[i])
    else:
        print("No hay pacientes atendidos por turno\n")
        

pacientesUrgencia=[]
pacientesTurno=[]
numeroSocio=input("Ingrese su numero de afiliado: ")

while VerifNum(numeroSocio):
    int(numeroSocio)
    turno=BusquedaAfiliado(pacientesUrgencia,numeroSocio)
    urgencia=BusquedaAfiliado(pacientesTurno,numeroSocio)
    print(f"Usted ha sido atendido por turno {turno} veces y por urgencias {urgencia} veces ")
    print("-------------------------------------------------------------------")
    pacienteAsunto=int(input("Ingrese si viene por una urgencia(0) o con turno(1) "))
    if pacienteAsunto==0:
        pacientesUrgencia.append(numeroSocio)
    else:
        pacientesTurno.append(numeroSocio)
    numeroSocio=input("Ingrese su numero de afiliado: ")

PrintPacientes(pacientesUrgencia,pacientesTurno)
    