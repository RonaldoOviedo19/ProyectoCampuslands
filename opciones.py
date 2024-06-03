from campers import *

opc_menurol = ("1. Camper","2. Trainer","3. Coordinador","4. Para salir")

opc_menucoordi = ("1. Registrar Camper","2. Mostrar los campers registrados","3. Actualizar estado de Camper","4. Salir")

opc_estado = ("1. En proceso de ingreso","2. Inscrito","3. Aprobado","4. Cursando","5. Graduado","6. Expulsado","7. Retirado")

opc_rut_entre = ("1. Ruta NodeJS","2. Ruta Java","3. Ruta NetCore")

def menurol():
    print("Seleccione el rol con el cual desea ingresar a CAMPUSLANDS --->")
    for i in opc_menurol:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def menucoordi():
    print("Seleccione el rol con el cual desea ingresar a CAMPUSLANDS --->")
    for i in opc_menucoordi:
        print(i)
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def estadocamper():
    print("Seleccione ->")
    for i in opc_estado:
        print(i)
    opc = int(input("Ingrese la opción del estado del camper que estas ingresando: "))
    return opc

def menu_principal():
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
                    registrar_camper(campers)
                elif opc == 2:
                    mostrarcampers(campers)
                elif opc == 3:
                    ingresarnotas_camper(campers)  
        



