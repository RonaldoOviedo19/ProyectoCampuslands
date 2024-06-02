from campers import *
from opciones import *

opc_menu = ("1. Para registrar camper","2. Para salir")

opc_estado = ("1. En proceso de ingreso","2. Inscrito","3. Aprobado","4. Cursando","5. Graduado","6. Expulsado","7. Retirado")

def menu():
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menu_principal():
    while True:
        print("---------------------------------------------------")
        opc = menu()
        if opc == len(opc_menu):
            print("Saliendo...")
            break    
        elif opc == 1:
            registrar_camper(campers)
        elif opc == 0:
            mostrar_campers(campers)