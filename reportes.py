from campers import *
from rutas import *

def listarcampersinscritos(campers,prefijo="- "):
   for clave, valor in campers.items():
     if valor["Estado"] == "Inscrito":
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")

def listarcampersaprobados(campers,prefijo="- "):
   for clave, valor in campers.items():
     if valor["Estado"] == "Aprobado":
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")

def listartrainers(trainers,prefijo="- "):
   for clave, valor in trainers.items():
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")

def listarcamperbajorendimiento(campers,prefijo="- "):
   for clave, valor in campers.items():
     if valor["Riesgo"] == True:
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")

def listarcampers(campers,prefijo="- "):
   global rut
   rut = asignarruta()
   for clave, valor in campers.items():
      if valor["Ruta De Entrenamiento"] == rut:
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")  

def listartrainers(trainers,prefijo="- "):
   for clave, valor in trainers.items():
      if valor["Ruta De Entrenamiento"] == rut:
       if isinstance(valor, dict):
           print("")
           print(f"- Documento : {clave}")
           mostrarcampers(valor, prefijo)
       else:
           print(f"{prefijo}{clave}: {valor}")  

