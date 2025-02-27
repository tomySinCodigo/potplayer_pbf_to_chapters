from pathlib import Path
import tkinter as tk
from tkinter import ttk
from ventana_tk2 import VentanaTk
from mi_tree import MiTree
from chapters import Chapters


class MiVentana(VentanaTk):
    def __init__(self, **kw):
        super(MiVentana, self).__init__(**kw)
        self._configMiVentana()

    def _configMiVentana(self):
        self.setIconAll("ty.png")
        self.bar.setBg("#383838")

        self.wg_tree = MiTree(self)
        self.wg_tree.grid(row=1, column=0, sticky='wens')
        self.rowconfigure(1, weight=1)

        bg = "black"
        self.addGrip(bg)
        self.setBg(bg)
        self.bar.lb_menu.cnfLabelMenu(text="PBF CHAPTERS")
        self.setSize(600, 350)

        self.getStyle()
        # self.test_archivo()

    def getStyle(self):
        self.s = ttk.Style()
        # self.s.theme_use('classic')
        self.s.theme_use('default')
        # self.s = self.wg_tree.s
        bg3 = "gray10"
        self.s.configure(
            "mi.Treeview",
            background=bg3,
            foreground="azure",
            font="Consolas 9 bold",
            fieldbackground=bg3,
            bordercolor=bg3,
            borderwidth=0,
            bd=0,
            relief="flat",
            border=0,
            highlightthickness=0,
        )
        self.s.map(
            "mi.Treeview",
            background=[("active", "skyblue")]
        )
        self.s.configure(
            "mi.Treeview.Heading",
            background=bg3,  # Fondo de los encabezados
            foreground="azure",    # Texto blanco
            font=("Consolas", 8, "bold"),  # Fuente del encabezado
            relief="flat"
        )
        self.s.map(
            "mi.Treeview.Heading",
            background=[("active", "black")]  # Fondo más claro al pasar el mouse
        )
        self.s.map(
            "mi.Treeview",
            background=[("selected", "black")],
            foreground=[("selected", "lightgreen")],
            # fieldbackground=[("selected", "yellow")]
        )
        # s.configure("mi.Treeview", rowheight=h, indicatorsize=0, indent=0)
        self.wg_tree.config(style="mi.Treeview")
        self.grip.config(bg=bg3)

        scroll_bg = "black"
        scroll_fg = "gray20"
        self.s.configure(
            "tree.Vertical.TScrollbar",
            gripcount=0,
            background=scroll_fg,
            darkcolor=scroll_bg,
            lightcolor=scroll_bg,
            troughcolor=scroll_fg,
            bordercolor=scroll_bg,
            relief='flat',
            borderwidth=0,
            bd=0,
            highlightthickness=0,
        )
        self.s.map(
            "tree.Vertical.TScrollbar",
            background=[("!active", scroll_bg), ("active", scroll_bg)],
            arrowcolor=[("active", scroll_bg), ("!active", scroll_fg)]
        )
        self.s.layout("Vertical.Scrollbar", [
            ("Vertical.Scrollbar.trough", {"children": [("Vertical.Scrollbar.thumb", {"expand": 1, "sticky": "nswe"})]}),
            ("Vertical.Scrollbar.button1", {"side": "top", "sticky": ""}),
            ("Vertical.Scrollbar.button2", {"side": "bottom", "sticky": ""}),
        ])
        self.wg_tree.scroll.config(style="tree.Vertical.TScrollbar")

    def test_archivo(self):
        archivo = "test.pbf"
        self.wg_tree.setPbfFile(archivo)
        h = self.wg_tree.H
        self.s.configure("mi.Treeview", rowheight=h, indicatorsize=0)

    def getDrop(self, e):
        li = super().getDrop(e)
        archivo = li[0]
        if archivo.endswith(".pbf"):
            self.wg_tree.setPbfFile(archivo)
            h = self.wg_tree.H
            self.s.configure("mi.Treeview", rowheight=h, indicatorsize=0)
            # chap = Chapters()
            
        


if __name__ == '__main__':
    wg = MiVentana()
    wg.mainloop()