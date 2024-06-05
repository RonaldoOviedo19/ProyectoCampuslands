import opciones
from rutas import *
from datos import *

def registrar_camper(data):
    print("--------------------------------------------------")
    camper = {}
    doc = input("Ingrese el documento del camper que desea registrar: ")    
    if data.get(doc, None) == None:
        camper["Nombres"] = input("Ingrese los nombres del camper a registrar: ")
        camper["Apellidos"] = input("Ingrese los apellidos del camper a registrar: ")
        camper["Direccion"] = input("Ingrese la direccion del camper a registrar: ")
        camper["Acudiente"] = input("Ingrese el nombre del acudiente del camper a registrar: ")
        camper["Tel Celular"] = int(input("Ingrese el numero celular del camper a registrar: "))
        camper["Tel Fijo"] = int(input("Ingrese el numero de telefono fijo del camper a registrar: "))
        camper["Estado"] = "Inscrito"
        camper["Riesgo"] = False
        data[doc] = camper
        guardar_datos()
        print("-------------------------------------------")
        print("----- USUARIO REGISTRADO EXITOSAMENTE -----")
        print("-------------------------------------------")
    else:
        print("LO SENTIMOS ESTE CAMPER YA ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")

def eliminar_camper(data):
    print("--------------------------------------------------")
    doc = input("Ingrese el documento del camper que desea eliminar: ")    
    if data.get(doc, None) != None:
        del data[doc]
        guardar_datos()
        print("-------------------------------------------")
        print("----- USUARIO ELIMINADO EXITOSAMENTE -----")
        print("-------------------------------------------")
    else:
        print("LO SENTIMOS ESTE CAMPER NO SE ENUENTRA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")

def mostrarcampers(campers, prefijo="- "):
    for clave, valor in campers.items():
        if isinstance(valor, dict):
            print("") 
            print(f"- Documento : {clave}")
            mostrarcampers(valor, prefijo)
        else:
            print(f"{prefijo}{clave}: {valor}")            
               
            
def ingresarnotas_camper(data):
    print("-----------------------------------------------")
    doc = input("Ingrese el documento del camper al cual desea ingresar sus notas: ")
    camper = data.get(doc, None)
    if camper != None:
        camper["Nota Teorica"] = int(input("Porfavor Ingrese la nota teorica del camper: "))
        camper["Nota Practica"] = int(input("Porfavor Ingrese la nota practica del camper: "))
        if (camper["Nota Teorica"]+camper["Nota Practica"])/2 >= 60 :
            camper["Estado"] = "Aprobado"
            print("EL CAMPER CAMBIO SU ESTADO A APROBADO DEBIDO A SUS NOTAS")
            camper["Ruta De Entrenamiento"] = asignarruta()
            guardar_datos()
        else:
            print("LO SENTIMOS EL CAMPER NO PUDO CAMBIAR SU ESTADO DEBIDO A SUS NOTAS")
    else:
        print("ESTE CAMPER NO SE ENCUENTRA REGISTRADO EN CAMPUSLANDS")
    print("-----------------------------------------------")  

def cambiarestado_camper(data):
    print("-----------------------------------------------")
    doc = input("Ingrese el documento del camper al cual desea actualizar su estado: ")
    camper = data.get(doc, None)
    if camper != None:
        while True:
            print("---------------------------------------------------")
            opc = opciones.menuestado()
            if opc == len(opciones.opc_menuestado)+1:
                print("Saliendo...")
                break    
            elif opc == 1:
                camper["Estado"] = "En proceso de ingreso"
                break
            elif opc == 2:
                camper["Estado"] = "Inscrito"
                break
            elif opc == 3:
                camper["Estado"] = "Aprobado"
                break
            elif opc == 4:
                camper["Estado"] = "Cursando"
                break
            elif opc == 5:
                camper["Estado"] = "Graduado"
                break
            elif opc == 6:
                camper["Estado"] = "Expulsado"
                break
            elif opc == 7:
                camper["Estado"] = "Retirado"   
                break 
        guardar_datos()
        print("------------------------------------------------------")
        print("----- ESTADO DEL CAMPER ACTUALIZADO EXITOSAMENTE -----")
        print("------------------------------------------------------")
    else:
        print("ESTE CAMPER NO SE ENCUENTRA REGISTRADO EN CAMPUSLANDS")
    print("-----------------------------------------------")     

def asignarruta_camper(data):
    print("--------------------------------------------------")
    doc = input("Ingrese el documento del camper que desea asignarle una ruta de entrenamiento: ")  
    camper = data.get(doc, None)
    if camper != None:  
        camper["Ruta De Entrenamiento"] = asignarruta()
        guardar_datos()
    else:
        print("LO SENTIMOS ESTE CAMPER NO ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")     