from campers import *

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