import json

campers = {}

ruta_archivo = "informacion.json"

def guardar_datos():
    global campers
    global ruta_archivo
    try:
        contenido = json.dumps(campers, indent=4)
        with open(ruta_archivo, "w") as file:
            file.write(contenido)
    except Exception:
        print("ERROR AL GUARDAR DATOS")

def cargar_datos():
    global campers
    global ruta_archivo
    try:
        file = open(ruta_archivo)
        campers = json.load(file)
    except Exception:
        print("ERROR AL CARGAR DATOS")

