def diasiguiente(d,m,a):

    if (a % 400 == 0):
        a_bisiesto = True
    elif (a % 100 == 0):
        a_bisiesto = False
    elif (a % 4 == 0):
        a_bisiesto = True
    else:
        a_bisiesto = False


    if m in (1, 3, 5, 7, 8, 10, 12):
        mes_len = 31
    elif m == 2:
        if a_bisiesto:
            mes_len = 29
        else:
            mes_len = 28
    else:
        mes_len = 30


    if d < mes_len:
        d += 1
    else:
        d = 1
        if m == 12:
            m = 1
            a += 1
        else:
            m += 1
    
    if m in (1, 3, 5, 7, 8, 10, 12):
        mes_len = 31
    elif m == 2:
        if a_bisiesto:
            mes_len = 29
        else:
            mes_len = 28
    else:
        mes_len = 30

    return d,m,a

dia_actual=(15,2,1974)
dia_siguiente=(diasiguiente(28,2,1974 ))
print(dia_siguiente)
dias_a_sumar=40
dias_existentes=0
fecha_a_encontrar=(25,2,1974)
aux2=()

for i in range(dias_a_sumar):
    dia_siguiente=(diasiguiente(dia_siguiente[0],dia_siguiente[1],dia_siguiente[2]))
    total_dias_sumados=dia_siguiente

if dia_actual[2] >= fecha_a_encontrar[2] or (dia_actual[1] >= fecha_a_encontrar[1] and dia_actual[2] >= fecha_a_encontrar[2]):
        if fecha_a_encontrar[0] < dia_actual[0]:
            aux=dia_actual
            aux2=fecha_a_encontrar
            dia_actual=fecha_a_encontrar
            fecha_a_encontrar=aux

while dia_actual != fecha_a_encontrar:
    dia_actual=(diasiguiente(dia_actual[0],dia_actual[1],dia_actual[2]))
    dias_existentes+=1

fecha_a_encontrar=aux2

print(f"a. Sumando {dias_a_sumar} días a la fecha obtenemos{total_dias_sumados}\nb. De la fecha {dia_actual} a {fecha_a_encontrar} hay {dias_existentes} días existentes")
