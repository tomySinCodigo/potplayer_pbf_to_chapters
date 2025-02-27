import tkinter as tk
from tkinter import ttk
from tree import Tree
from pbf_read import PbfRead


class EntryPopup(tk.Entry):
    def __init__(
        self, parent:ttk.Treeview,
        iid:str, col:int, texto:str, **kw
    ):
        super().__init__(parent, **kw)
        self.tv = parent
        self.iid = iid
        self.col = col
        self.texto = texto
        self._config_EntryPopup()

    def _config_EntryPopup(self):
        self.insert(0, self.texto)
        self['exportselection'] = False # previene que el texto sea copiado al clip al perder foco
        self.focus_force()
        self.select_all()
        self.bind("<Return>", self.onReturn)
        self.bind("Control-a", self.select_all)
        self.bind("<Escape>", lambda *ignore: self.destroy())

        bg = "black"
        fg = "#FFC353"
        self.config(
            bg=bg, fg=fg,
            insertbackground=fg,
            selectbackground=fg,
            selectforeground=bg,
            insertborderwidth=6,
            relief="flat",
            font="Arial 10",
            justify="center"
        )


    def onReturn(self, e):
        """inserta texto en el treeview y borra el entry"""
        row_id = self.tv.focus()
        values = self.tv.item(row_id, "values")
        values = list(values)
        values[self.col] = self.get()
        self.tv.item(row_id, values=values)
        self.destroy()

    def select_all(self, *ignore):
        self.icursor(tk.END)
        self.selection_range(0, tk.END)
        return "break"
    

class ComboboxPopup(ttk.Combobox):
    def __init__(self, parent:ttk.Treeview, **kw):
        super().__init__(parent, **kw)



class MiTree(Tree):
    def __init__(self, parent, *args, **kw):
        super().__init__(parent=parent, *args, **kw)
        self.parent = parent
        self._config_MiTree()

    def _config_MiTree(self):
        self._setScroll()
        self.DATA_PBF = None
        self.H = 20
        self.bind("<Double-1>", self.itemDoubleClick)
        self.bind("<Button-1>", self.itemClick)
        # self.bind("<<TreeviewSelect>>", self.itemSelect)


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

    def itemSelect(self, e=None):
        tp = super().itemClick(e)
        # print('tp :: ', tp)
        indice = int(tp[0])-1
        # indice = int(tp[0])
        print(self.DATA_PBF[indice])

        # print(self.getColumn("TIEMPO"))

    def itemClick(self, e=None):
        index = self.identify_row(e.y)
        i = int(index[1:])
        print(f'INDEX::"{index}" -> {self.getRow(index)}', f"i:{i}")

    def itemDoubleClick(self, e):
        """Doble click a item"""
        try:
            self.entryPopup.destroy()
        except AttributeError:
            pass

        row_id = self.identify_row(e.y)
        col_id = self.identify_column(e.x)
        # print(row_id, col_id)

        if not row_id or col_id in ["#0", "#1"]: # si el encabezado se eligio (y para que no se editen las cols 1 y 2)
            return
        
        # obten dimension de la celda
        x, y, width, height = self.bbox(row_id, col_id)
        # print(x, y, width, height)
        print("FIL:COL->", row_id, col_id, "EDIT 2CLICK")
        # print(col_id == "#0", f'"#0"=={col_id}')
        pady = height//2

        col = int(col_id[1:])-1
        texto = self.item(row_id, "values")[col]
        self.entryPopup = EntryPopup(self, row_id, col, texto)
        self.entryPopup.place(
            x=x, y=y+pady,
            width=width, height=height, anchor="w"
        )

    def getColumn(self, colname:str):
        col_values = []
        for id in self.get_children():
            col_values.append(self.item(id, "values")[
                self["columns"].index(colname)
            ])
        return col_values
    
    def getRowN(self, row_num:int):
        print("get_children return value: ", self.get_children())
        return self.item(self.get_children()[row_num], option="values")
    
    def getRow(self, rowindex:str):
        return self.item(rowindex, option="values")
    
    def getRows(self, op:str="values"):
        return [self.item(i, option=op) for i in self.get_children()]


    def setCurrentRow(self, n_row:int):
        self.selection_set(f"I{n_row:03d}")

    def getCurrentRow(self):
        return self.selection()
