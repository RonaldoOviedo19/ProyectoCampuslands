import opciones

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
        while True:
            print("---------------------------------------------------")
            opc = opciones.estadocamper()
            if opc == (len(opciones.opc_estado)+1):
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
        camper["Riesgo"] = False
        data[doc] = camper
        print("----- USUARIO REGISTRADO EXITOSAMENTE -----")
    else:
        print("LO SENTIMOS ESTE CAMPER YA ESTA REGISTRADO EN NUESTRA BASE DE DATOS")
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
    print("**************************************************")
    doc = input("Ingrese el documento del camper al cual desea actualizar su estado: ")
    camper = data.get(doc, None)
    if camper != None:
        camper["Nota Teorica"] = int(input("Porfavor Ingrese la nota teorica del camper: "))
        print("ESTADO DEL CAMPER ACTUALIZADO EXITOSAMENTE")
    else:
        print("Este camper no se encuentra registrado en CAMPUSLANDS")
    print("**************************************************")  