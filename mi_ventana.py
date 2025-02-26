import tkinter as tk
from tkinter import ttk
from ventana_tk2 import VentanaTk


class MiVentana(VentanaTk):
    def __init__(self, **kw):
        super(MiVentana, self).__init__(**kw)
        self._configMiVentana()

    def _configMiVentana(self):
        # self.t_ico = tk.PhotoImage(file="tomi_cw.png")
        # self.bar.setIconMenu(image=self.t_ico)
        # self.setIconAll("tomi_cw.png")
        self.setIconAll("ty.png")
        self.bar.setBg("#383838")

        bg = "black"
        self.addGrip(bg)
        self.setBg(bg)
        self.bar.lb_menu.cnfLabelMenu(text="PBF CHAPTERS")
        self.setSize(600, 350)


if __name__ == '__main__':
    wg = MiVentana()
    wg.mainloop()