from pathlib import Path
import tkinter as tk
from tkinter import ttk
from ventana_tk2 import VentanaTk
from ventana_tk2.mi_tree import MiTree
from chapters import Chapters
from ventana_tk2.ktexto import KText


class MiVentana(VentanaTk):
    def __init__(self, **kw):
        super(MiVentana, self).__init__(**kw)
        self._configMiVentana()

    def _configMiVentana(self):
        self.PBF_FILE = None
        self.setIconAll("video16.png")
        self.bar.setBg("#383838")

        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.pw = tk.PanedWindow(
            self, orient=tk.HORIZONTAL,
            sashwidth=5, sashrelief="flat", bg="black"
        )
        self.pw.grid(row=1, column=0, sticky='wens')
        self.wg_tree = MiTree(self.pw)
        self.wg_tree.grid(row=0, column=0, sticky='wens')
        self.texw = KText(self.pw)

        bg = "black"
        self.addGrip(bg)
        self.setBg(bg)
        self.bar.lb_menu.cnfLabelMenu(text="PBF CHAPTERS")

        chap = Chapters()
        sk = chap.readFileToml('skin')
        self.setSize(*sk.get('size'))
        self.setStyle()
        # self.test_archivo()

        self.bar.menuItem("genera chapters OGG", self.genFileTextoOGG)
        self.bar.menuItem("genera chapters modo 1", self.genFileModoDos)
        self.bar.menuItem("genera chapters modo 2", self.genFileModoTres)
        # self.bar.menuItem("obten titulos", self.)
        # self.wg_tree.setCurrentRow(2)
        self.wg_tree.bind("<Double-Button-1>", self.doble)
        self.texw.setScroll(self.s)
        self.msgn("PBF TO CHAPTERS: ")
        self.msgn("arrastra un archivo .pbf\n", num=2)

        # self.bind("<<TreeviewSelect>>", self.itemSelect)
        self.wg_tree.bind('<<TreeviewSelect>>', self.itemSelect)

        # self.pw.add(self.wg_tree, minsize=300, stretch='always', width=450)
        wp1 = sk.get('panel1')
        self.pw.add(self.wg_tree, minsize=300, width=wp1)
        self.pw.add(self.texw)
        # self.test_archivo()
        self.msgn('-- EJEMPLO CHAPTERS --\n')
        self.msgn("OGG:\n", 6)
        self.msgn("CHAPTER01=00:00:00.000\nCHAPTER01NAME=01 name chapter\n", 7)
        self.msgn("MODO 1:\n", 6)
        self.msgn('1 name chapter 00:00:00.000\n', 7)
        self.msgn("MODO 2:\n", 6)
        self.msgn('00:00:00.000 --> 00:01:30.000\n', 7)
        self.msgn('1 intro\n', 7)
        self.msgn('-'*30  + '\n')

        # "dos":"{i} {tag} {tiempo}\n",
        # "tres":"{tiempo_i} --> {tiempo_f}\n{i} {tag}\n"

    def msg(self, texto, **kw):
        self.texw.msg(texto, **kw)

    def msgn(self, texto:str, num:int=0, **kw):
        self.texw.msgNum(texto, num, **kw)

    def genFileTextoOGG(self):
        li = self.wg_tree.getRows()
        d = self.wg_tree.DATA_PBF
        chap = Chapters()
        # txt = "CHAPTER01=00:00:00.000\nCHAPTER01NAME=01\n"
        txt = chap.tipoUno(tiempo="00:00:00.000", tag="", indice=0)
        for i, e in enumerate(li):
            _, ts, tag = e
            t, ms = d[i].get("t"), d[i].get("mseg")
            txt += chap.tipoUno(ts, tag, i+1)
        contenido = txt.strip("\n")
        if self.PBF_FILE:
            self.makeFileChapter(contenido)

    def _genFileTextoDos(self, metodo, txt="", **kw):
        li = self.wg_tree.getRows()
        for i, e in enumerate(li):
            _, ts, tag = e
            txt += metodo(ts, tag, i+1)
        contenido = txt.strip("\n")
        if self.PBF_FILE:
            self.makeFileChapter(contenido)

    def genFileModoDos(self):
        chap = Chapters()
        txt = chap.tipoDos(tiempo="00:00:00.000", tag="", indice=0)
        self._genFileTextoDos(chap.tipoDos, txt)

    def genFileModoTres(self):
        chap = Chapters()
        li = self.wg_tree.getRows()
        ti = "00:00:00.000"
        txt = ""
        for i, item in enumerate(li):
            _, ts, tag = item
            txt += chap.tipoTres(ti, ts, tag, i)
            ti = ts
        contenido = txt.strip("\n")
        if self.PBF_FILE:
            self.makeFileChapter(contenido)

    def getTreeChapters(self):
        li = self.wg_tree.getRows()
        d = self.wg_tree.DATA_PBF
        chap = Chapters()
        txt = ""
        for i, e in enumerate(li):
            _, ts, tag = e
            t, ms = d[i].get("t"), d[i].get("mseg")
            txt += chap.tipoUno(ts, tag, i+1)
        contenido = txt.strip("\n")
        if self.PBF_FILE:
            self.makeFileChapter(contenido)

    def makeFileChapter(self, txt:str):
        r = Path(self.PBF_FILE)
        with open(f"{r.stem}.txt", "w") as file:
            file.write(txt)
        self.msgn(f"\n\nArchivo creado: {r.stem}.txt\n", 6, font="Consolas 9")
        self.texw.see()
        self.msgn(f'{txt}\n', num=1)

    def setStyle(self):
        self.s = ttk.Style()
        self.s.theme_use('default')
        bg3 = "gray10"
        self.s.configure(
            "mi.Treeview",
            background=bg3,
            foreground="#B8B3A4",
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
            foreground="#20B2AA",    # Texto blanco
            font=("Consolas", 8, "bold"),  # Fuente del encabezado
            relief="flat"
        )
        self.s.map(
            "mi.Treeview.Heading",
            background=[("active", "black")]  # Fondo más claro al pasar el mouse
        )
        self.s.map(
            "mi.Treeview",
            background=[("selected", "#27151B")],
            foreground=[("selected", "white")],
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
            self.PBF_FILE = archivo
            self.wg_tree.setPbfFile(archivo)
            h = self.wg_tree.H
            self.s.configure("mi.Treeview", rowheight=h, indicatorsize=0)
            _ = Path(self.PBF_FILE)

            self.msgn('[', 7)
            self.msgn(f' {self.wg_tree.getNumChapters()} ', 6)
            self.msgn('Chapters ] ', 7)
            self.msgn(_.parent.as_posix() + "/", 4, font="Consolas 10")
            self.msgn(_.name + "\n", 3, font="Consolas 10")
            self.texw.see()
            
    def doble(self, e):
        self.wg_tree.itemDoubleClick(e)
        self.setStyle()

    def itemSelect(self, e=None):
        indice, d = self.wg_tree.itemSelect(e)
        self.bar.clearTextTitle()
        self.bar.msg(f"CHAPTER[{indice+1}]  ({d.get('mseg')}) : {d.get('tiempo')}", tag='infobar')


if __name__ == '__main__':
    wg = MiVentana()
    wg.mainloop()