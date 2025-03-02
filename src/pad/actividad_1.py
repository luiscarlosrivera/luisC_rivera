import json
import requests
import sys
import os
from pathlib import Path

class Actividad_1():
    def __init__(self):
        ruta_actual = str(Path.cwd())

        self.ruta_static="{}/src/pad/static/".format(ruta_actual)
        self.ruta_json="{}/src/pad/static/json/".format(ruta_actual)
        directorio = os.path.dirname(self.ruta_json)
        if not os.path.exists(directorio):
            os.makedirs(directorio)
        sys.stdout.reconfigure(encoding='utf-8')
        
    def leer_api(self, url):
        response = requests.get(url)
        return response.json()
    
    def escribir_json(self, datos, nombre_archivo):
        ruta_json = self.ruta_static+nombre_archivo
        ruta_json = "{}json/{}".format(self.ruta_static,nombre_archivo)
        with open(ruta_json, 'w') as file:
            json.dump(datos, file, indent=4)
        return True 



ingestion = Actividad_1()
datos_json =ingestion.leer_api("https://stephen-king-api.onrender.com/api/shorts")
escribir_json = ingestion.escribir_json(datos_json, "datos.json")

print("esta es la ruta statica",ingestion.ruta_static)
print("estos son los datos",datos_json)