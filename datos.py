import json

campers = {}
trainers = {}

ruta_archivo = "informacion.json"
ruta_trainer = "infotrainer.json"

def guardar_datostrainer():
    global trainers
    global ruta_trainer
    try:
        contenido = json.dumps(trainers, indent=4)
        with open(ruta_trainer, "w") as file:
            file.write(contenido)
    except Exception:
        print("ERROR AL GUARDAR DATOS")

def cargar_datostrainer():
    global trainers
    global ruta_trainer
    try:
        file = open(ruta_trainer)
        trainers = json.load(file)
    except Exception:
        print("ERROR AL CARGAR DATOS")

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

