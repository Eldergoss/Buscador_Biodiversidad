import json



class Wikificha:
    def __init__(self, data):
        # Guardamos el diccionario completo
        self.data = data

    # métodos
    def nombre(self):
        return self.data.get("extract")

    def imagen(self):
        return self.data.get("thumbnail", {}).get("source", "Sin imagen")

"""
nombre_cientifico = "Panthera pardus"

def wikidata(nombre cientifico)

url = f"https://es.wikipedia.org/api/rest_v1/page/summary/{nombre_cientifico.replace(' ', '_')}"

headers = {
    'User-Agent': 'BetaTaxonomiaBot/1.0 (david@ejemplo.com)'
}

response = requests.get(url, headers=headers)

responsive = response.json()

# inicializamos la clase
schedule = Wikificha(responsive)

print(schedule.nombre())
print()
print(schedule.imagen())
"""
