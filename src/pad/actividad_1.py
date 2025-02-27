import json
import requests
import sys


class Actividad_1():
    def __init__(self):
        self.ruta_static="src/pad/static/"
        sys.stdout.reconfigure(encoding='utf-8')
        
    def leer_api(self, url):
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self, datos, nombre_archivo):
        ruta_json = self.ruta_static+nombre_archivo
        ruta_json = "{}/json/{}".format(self.ruta_static,nombre_archivo)
        with open(ruta_json, 'w') as file:
            json.dump(datos, file, indent=4)
        return True 


ingestion = Actividad_1()
datos_json =ingestion.leer_api("https://api.github.com/users/hadley/orgs")
escribir_json = ingestion.escribir_json(datos_json, "datos.json")

print("esta es la ruta statica",ingestion.ruta_static)
print("estos son los datos",datos_json)