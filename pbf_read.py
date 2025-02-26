from pathlib import Path
from PIL import Image, ImageTk
import io


class MiTiempo:
    def __init__(self, mseg):
        self.ms = float(mseg)

    def mseg_hmsz(self, milisegundos) -> tuple:
        '''retorna tupla[int] =  h, m, s, z'''
        h, r = divmod(float(milisegundos), 3.6e6)
        m, r = divmod(r, 6e4)
        s, z = divmod(r, 1e3)
        return int(h), int(m), int(s), int(z)

    def getData(self):
        h, m ,s, z = self.mseg_hmsz(self.ms)
        tiempo = f"{h:02d}:{m:02d}:{s:02d}.{z:03d}"
        tm = tiempo[3::] if tiempo.startswith('00:') else tiempo
        t = tm[:tm.index('.')]
        return {
            "tiempo":tiempo,
            "tm":tm,
            "t":t
        }


class MiImagen:
    def __init__(self, str_hex:str):
        self.hex = str_hex
        self.bytes = self._imgx2bytes(self.hex)

    def _imgx2bytes(self, texto:str) -> str:
        if "FFD" in texto:
            indice = texto.index("FFD")
            return bytes.fromhex(texto[indice:])
        
    def save(self, file:str):
        with open(file, "wb") as b:
            b.write(self.bytes)

    def quitBorder(self, img_hex, md=16, wh=(100,60)) -> Image:
        filei = io.BytesIO(img_hex)
        img_pil = Image.open(filei)
        w, h = img_pil.size
        return img_pil.crop((0,md,w,h-md)).resize(wh)
    
    def getImageTk(self, wh=(100,60)) -> ImageTk:
        return ImageTk.PhotoImage(self.quitBorder(self.bytes, wh=wh))


class PbfRead:
    def __init__(self, archivo:str):
        self.ruta_pbf = Path(archivo).as_posix()

    def leePbf(self, ruta) -> list:
        with open(ruta, "r", encoding="utf-16LE") as f:
            lineas = [l.strip("\n") for l in f.readlines()]
            return [l for l in lineas if "*" in l]
        
    def obtenDataLinea(self, linea):
        data = {}
        if "*" in linea:
            _, tg, imgx = linea.split("*")
            data["tag"] = tg
            data["img"] = MiImagen(imgx)
            if  "=" in _:
                indice, n = _.split("=")
                data["indice"] = int(indice)
                data["mseg"] = int(n)
                mit = MiTiempo(n)
                d = mit.getData()
        return {**data, **d}
    
    def getData(self) -> list:
        lineas = self.leePbf(ruta=self.ruta_pbf)
        return [self.obtenDataLinea(linea) for linea in lineas]