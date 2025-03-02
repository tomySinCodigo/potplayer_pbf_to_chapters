import json
import toml


class Chapters:
    def tipoUno(self, tiempo, tag, indice):
        # CHAPTER01=00:00:00.000
        # CHAPTER01NAME=01 01 inicio
        i = int(indice)+1
        # plantilla = 'CHAPTER{i:02d}={tiempo}\nCHAPTER{i:02d}NAME={i:02d} {tag}\n'
        # plantilla = self.leePlantilla("uno")
        plantilla = self.readFileToml("plantillas").get("uno")
        return plantilla.format(i=i, tiempo=tiempo, tag=tag)

    def tipoDos(self, tiempo, tag, indice):
        i = int(indice)+1
        # plantilla = '{i} {tag} {tiempo}\n'
        # plantilla = self.leePlantilla("dos")
        plantilla = self.readFileToml("plantillas").get("dos")
        return plantilla.format(i=i, tiempo=tiempo, tag=tag)
    
    def tipoTres(self, tiempo_i:str, tiempo_f:str, tag, indice):
        i = int(indice)+1
        # plantilla = '{tiempo_i} --> {tiempo_f}\n{i} {tag}\n'
        # plantilla = self.leePlantilla("tres")
        plantilla = self.readFileToml("plantillas").get("tres")
        return plantilla.format(tiempo_i=tiempo_i, tiempo_f=tiempo_f, tag=tag, i=i)
    
    def makePlantilla(self):
        archivo = "titulos.json"
        d = {
            "uno":"CHAPTER{i:02d}={tiempo}\nCHAPTER{i:02d}NAME={i:02d} {tag}\n",
            "dos":"{i} {tag} {tiempo}\n",
            "tres":"{tiempo_i} --> {tiempo_f}\n{i} {tag}\n"
        }
        with open(archivo, "w") as file:
            json.dump(d, file, indent=4)

    def leePlantilla(self, nom:str):
        archivo = "plantillas.json"
        with open(archivo, "r") as file:
            d = json.load(file)
        return d.get(nom)
    
    def makeFileToml(self):
        archivo = "config.toml"
        d = {
            "plantillas":{
                "uno":"CHAPTER{i:02d}={tiempo}\nCHAPTER{i:02d}NAME={i:02d} {tag}\n",
                "dos":"{i} {tag} {tiempo}\n",
                "tres":"{tiempo_i} --> {tiempo_f}\n{i} {tag}\n"
            },
            "titulos":{
                "seleccionado":"basico",
                "basico":[
                    "inicio","opening","pausa","fin pausa","ending","avanze"
                ]
            }
        }
        with open(archivo, "w") as file:
            toml.dump(d, file)

    def readFileToml(self, nom:str):
        archivo = "config.toml"
        with open(archivo, "r") as file:
            d = toml.load(file)
        return d.get(nom)







if __name__ == '__main__':
    chap = Chapters()
    # chap.makePlantilla()
    # chap.makeFileToml()

    print(chap.tipoUno("00:01:24.000", "mi tag", "0"))
    print(chap.tipoDos("00:01:24.000", "mi tag", "0"))
    print(chap.tipoTres("00:00:15.000", "00:01:24.000", "mi tag", "0"))