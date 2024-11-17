import requests
import json

respuesta = requests.get("http://elprofemiguel.com/APIS_JSON/requisitos_formacion_api.json")

data = respuesta.json() # aquí la variable dd ya se convierte en un diccionario de python y se puede iterar

for dato in data["listado_requisitos_formacion"]:
    print(dato)

