from campers import *
from rutas import *
from trainers import *
from reportes import *
import datos

opc_menurol = ("1. Camper","2. Trainer","3. Coordinador","4. Seccion Reportes","5. Para salir")

opc_menureportes = ("1. Listar los campers que se encuentren en estado de inscrito","2. Listar los campers que aprobaron el examen inicial","3. Listar los entrenadores que se encuentran trabajando con CAMPUSLANDS","4. Listar los campers que cuentan con bajo rendimiento","5. Listar los campers y trainers que se encuentren asociados a una ruta de entrenamiento","6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado")

opc_menucoordi = ("1. Registrar Camper","2. Mostrar los campers registrados","3. Ingresar notas de un Camper","4. Cambiar estado de un camper","5. Agregar nueva ruta de entrenamiento a un camper","6. Eliminar a un camper de la base de datos","7. Agregar nueva ruta de entrenamiento","8. Mostrar rutas de entrenamiento","9. Registrar Trainer","10. Mostrar Trainers","11. Asignar ruta de entrenamiento a un trainer","12. Salir")

opc_menuestado = ("1. En proceso de ingreso","2. Inscrito","3. Aprobado","4. Cursando","5. Graduado","6. Expulsado","7. Retirado")

def menurol():
    print("Seleccione el rol con el cual desea ingresar a CAMPUSLANDS --->")
    for i in opc_menurol:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menucoordi():
    print("Seleccione --->")
    for i in opc_menucoordi:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menureportes():
    print("Seleccione --->")
    for i in opc_menureportes:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menuestado():
    print("Seleccione el estado nuevo que quiera asignar al camper --->")
    for i in opc_menuestado:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menu_principal():
    cargar_datos()
    while True:
        print("---------------------------------------------------")
        opc = menurol()
        if opc == len(opc_menurol):
            print("Saliendo...")
            break    
        elif opc == 1:
            print("PERFECTO CAMPER BIENVENIDO A CAMPUSLANDS")
        elif opc == 2:
            print("PERFECTO TRAINER BIENVENIDO A CAMPUSLANDS")
        elif opc == 3:
            while True:
                print("---------------------------------------------------")
                print("BIENVENIDO A CAMPUSLANDS COORDINADOR")
                opc = menucoordi()
                if opc == len(opc_menucoordi):
                    print("Saliendo...")
                    break    
                elif opc == 1:
                    registrar_camper(datos.campers)
                elif opc == 2:
                    mostrarcampers(datos.campers)
                elif opc == 3:
                    ingresarnotas_camper(datos.campers)  
                elif opc == 4:
                    cambiarestado_camper(datos.campers)
                elif opc == 5:
                    asignarruta_camper(datos.campers)
                elif opc == 6:
                    eliminar_camper(datos.campers)          
                elif opc == 7:
                    agregarnueva_ruta()   
                elif opc == 8:
                    mostrarrutas()    
                elif opc == 9:
                    registrar_trainer(trainers)  
                elif opc == 10:
                    mostrartrainers(trainers)  
                elif opc == 11:
                    asignarruta_trainer(trainers) 
        elif opc == 4:
            while True:
                print("---------------------------------------------------")
                print("BIENVENIDO AL MODULO DE REPORTES")
                opc = menureportes()
                if opc == len(opc_menureportes):
                    print("Saliendo...")
                    break    
                elif opc == 1:
                    listarcampersinscritos(datos.campers)
                    break
                elif opc == 2:
                    listarcampersaprobados(datos.campers)
                    break
                elif opc == 3:
                    break 
                elif opc == 4:
                    cambiarestado_camper(campers)
                elif opc == 5:
                    agregarnueva_ruta()   
                elif opc == 6:
                    mostrarrutas()    
                elif opc == 7:
                    registrar_trainer(trainers)  
                elif opc == 8:
                    mostrartrainers(trainers)  
                elif opc == 9:
                    asignarruta_trainer(trainers)             
                     
        



