from campers import *

rutas = ["Ruta NodeJS","Ruta Java","Ruta NetCore"]

nuevasrutas = ["1. Fundamentos de programación","2. Programación Web","3. Programación formal","4. Bases de datos","5. Backend"]

def menuruta():
    print("Seleccione la ruta de entrenamiento que le desea asignar al camper --->")
    cont = 1
    for i in rutas:
        print(cont,i)
        cont += 1
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menurutas():
    print("Seleccione la nueva ruta de entrenamiento que desea agregar --->")
    for i in nuevasrutas:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def agregarnueva_ruta():
    print("-----------------------------------------------")
    while True:
        print("--------------------------------------------------------")
        opc = menurutas()
        if opc == len(nuevasrutas)+1:
            print("Saliendo...")
            break    
        elif opc == 1:
            rutas.append("Ruta Fundamentos de programación")
            break
        elif opc == 2:
            rutas.append("Ruta Programación Web")
            break
        elif opc == 3:
            rutas.append("Ruta Programación formal")
            break
        elif opc == 4:
            rutas.append("Ruta Bases de datos")
            break
        elif opc == 5:
            rutas.append("Ruta Backend")
            break
    print("------------------------------------------------------")
    print("----- RUTA AGREGADA EXITOSAMENTE -----")
    print("------------------------------------------------------")

def asignarruta():
    print("-----------------------------------------------")
    while True:
        print("--------------------------------------------------------")
        opc = menuruta()
        if opc == len(rutas)+1:
            print("Saliendo...")
            break    
        elif opc == 1:
            rut = rutas[0]
            break
        elif opc == 2:
            rut = rutas[1]
            break
        elif opc == 3:
            rut = rutas[2]
            break
        elif opc == 4:
            rut = rutas[3]
            break
        elif opc == 5:
            rut = rutas[4]
            break
        elif opc == 6:
            rut = rutas[5]
            break
        elif opc == 7:
            rut = rutas[6]
            break
        elif opc == 8:
            rut = rutas[7]
            break
    print("------------------------------------------------------")
    print("------------- RUTA ASIGNADA EXITOSAMENTE -------------")
    print("------------------------------------------------------")
    return rut

def mostrarrutas():
    print("LAS RUTAS DE ENTRENAMIENTO SON : ")
    print("")
    for valor in rutas:
        print(valor)