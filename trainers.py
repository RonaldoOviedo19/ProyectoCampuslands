from rutas import *

trainers = {
    "123" : {"Nombre" : "Prueba","Edad":25,"Tel Celular":"3125698874"}
}

def registrar_trainer(data):
    print("--------------------------------------------------")
    trainer = {}
    doc = input("Ingrese el documento del trainer que desea registrar: ")    
    if data.get(doc, None) == None:
        trainer["Nombre"] = input("Ingrese los nombres del trainer a registrar: ")
        trainer["Edad"] = int(input("Ingrese la edad del trainer a registrar: "))
        trainer["Tel Celular"] = int(input("Ingrese el numero celular del trainer a registrar: "))
        data[doc] = trainer
        print("-------------------------------------------")
        print("----- TRAINER REGISTRADO EXITOSAMENTE -----")
        print("-------------------------------------------")
    else:
        print("LO SENTIMOS ESTE TRAINER YA ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")

def asignarruta_trainer(data):
    print("--------------------------------------------------")
    doc = input("Ingrese el documento del trainer que desea asignarle una ruta de entrenamiento: ")  
    trainer = data.get(doc, None)
    if trainer != None:  
        trainer["Ruta De Entrenamiento"] = asignarruta()
    else:
        print("LO SENTIMOS ESTE TRAINER NO ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")    

def mostrartrainers(trainers, prefijo="- "):
    for clave, valor in trainers.items():
        if isinstance(valor, dict):
            print("") 
            print(f"- Documento : {clave}")
            mostrartrainers(valor, prefijo)
        else:
            print(f"{prefijo}{clave}: {valor}") 