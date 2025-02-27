class Chapters:
    def tipoUno(self, tiempo, tag, indice):
        # CHAPTER01=00:00:00.000
        # CHAPTER01NAME=01 01 inicio
        i = int(indice)+1
        plantilla = 'CHAPTER{i:02d}={tiempo}\nCHAPTER{i:02d}NAME={i:02d} {tag}\n'
        return plantilla.format(i=i, tiempo=tiempo, tag=tag)

    def tipoDos(self, tiempo, tag, indice):
        i = int(indice)+1
        plantilla = '{i} {tag} {tiempo}\n'
        return plantilla.format(i=i, tiempo=tiempo, tag=tag)
    
    def tipoTres(self, tiempo_i:str, tiempo_f:str, tag, indice):
        i = int(indice)+1
        plantilla = '{tiempo_i} --> {tiempo_f}\n{i} {tag}\n'
        return plantilla.format(tiempo_i=tiempo_i, tiempo_f=tiempo_f, tag=tag, i=i)
    

if __name__ == '__main__':
    chap = Chapters()
    # print(chap.tipoUno("00:01:24.000", "mi tag", "0"))
    # print(chap.tipoDos("00:01:24.000", "mi tag", "0"))
    print(chap.tipoTres("00:00:15.000", "00:01:24.000", "mi tag", "0"))