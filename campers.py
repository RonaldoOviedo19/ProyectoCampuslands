campers = {
    "123" : {"Nombres" : "Prueba Prueba","Apellidos":"Prueba Prueba","Direccion":"Cra 22 D # 4 N 60","Acudiente":"Daniela","Tel Celular":"3125698874","Tel Fijo":"6785962","Estado":"","Riesgo":True}
}

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
        camper["Estado"] = input("Ingrese el cargo: ")
        camper["Riesgo"] = False
        data[doc] = camper
    else:
        print("LO SENTIMOS ESTE CAMPER YA ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
    print("--------------------------------------------------")

def mostrar_campers(data):
    print("-----------------------------------------")
    print("Los eventos son:")
    for valor in data:
        print("-",valor("Nombres"))    
    print("**************************************************")