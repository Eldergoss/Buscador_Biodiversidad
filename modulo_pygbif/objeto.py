from pygbif import species
import json

#clase usada para instaciar una ficha para data de gbif

class Ficha:
    def __init__(self, data):
        # Guardamos el diccionario completo
        self.data = data

    # Los métodos deben mantener el mismo nivel de indentación que el __init__
    def nombre(self):
        return self.data.get("usage", {}).get("name")

    def familia(self):
        classification = self.data.get("classification", [])

        if classification:
            return classification[3].get("name")

    def reino(self):
        classification = self.data.get("classification", [])

        if classification:
            return classification[0].get("name")

    def orden(self):
        classification = self.data.get("classification", [])

        if classification:
            return classification[2].get("name")

    def Idtaxon(self):
        return self.data.get("usage", {}).get("key")
