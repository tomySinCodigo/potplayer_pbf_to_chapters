import tkinter as tk
from tkinter import ttk
from tree import Tree
from pbf_read import PbfRead


class MiTree(Tree):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.parent = parent
        self._config_MiTree()

    def _config_MiTree(self):
        self._setScroll()
        self.DATA_PBF = None
        self.H = 20

    def _setScroll(self):
        self.scroll = ttk.Scrollbar(self, orient="vertical", command=self.yview)
        self.configure(yscrollcommand=self.scroll.set)
        # scroll.place(anchor="nw", in_=self, relheight=1, relwidth=0.03, width=6)
        self.scroll.pack(side="left", fill="y", pady=3, padx=2)

    def setPbfFile(self, file_pbf:str, w:int=120, ar:float=16/9, modh=10):
        self.PBF = PbfRead(file_pbf)
        self.DATA_PBF = self.PBF.getData()
        h = int(w/ar) + modh
        self.H = h
        self.clearRows()

        for i, d in enumerate(self.DATA_PBF):
            row = [
                d.get("img").getImageTk(wh=(w,h)),
                str(i+1),
                d.get("tiempo"),
                d.get("tag")
            ]
            self.setRow(row)


        # self.s.configure("mi.Treeview", rowheight=h, indicatorsize=0)
        #     background="red"
        # )
        # self.config(style="mi.Treeview")

    def itemClick(self, e=None):
        tp = super().itemClick(e)
        indice = int(tp[0])-1
        print(self.DATA_PBF[indice])

