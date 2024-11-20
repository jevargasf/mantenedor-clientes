import requests
import json

def consultar():
    respuesta = requests.get("http://elprofemiguel.com/APIS_JSON/requisitos_formacion_api.json")

    data = respuesta.json() # aquí la variable dd ya se convierte en un diccionario de python y se puede iterar

    return data["listado_requisitos_formacion"]
    

