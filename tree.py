from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps


class Tree(ttk.Treeview):
    def __init__(self, parent, *args, **kw):
        super(Tree, self).__init__(master=parent, *args, **kw)
        self.parent = parent
        self._configTree()

    def _configTree(self):
        self.ROWS_DATA = []
        self.IXS = []
        cols = {
            # "IMAGEN":120,
            "IMAGEN":142,
            "ID":20,
            "TIEMPO":80,
            "TAGS":"",
        }
        # h = int(cols["IMAGEN"] / (16/9))-12
        self.setColumnsTitles(cols)
        # self.bind("<<TreeviewSelect>>", self.itemClick)


    def setColumnsTitles(self, dtitles:dict):
        """set titles: dtitles-> dict{title:width}"""
        titles = tuple(dtitles.keys())
        self.config(columns=titles[1:])
        self.heading("#0", text=titles[0])
        w0 = dtitles.get(titles[0])
        self.column("#0", width=w0, minwidth=w0, stretch=False, anchor="w")
        for title in titles[1:]:
            self.heading(title, text=title)
            if dtitles.get(title):
                w = dtitles.get(title)
                self.column(title, width=w, minwidth=w, stretch=False)
        # self.tag_configure("ID", foreground="orange")
        # self.set()
        
    def setRow(self, li:list):
        """li: [Image[PIL], **values]"""
        # self.ROWS_DATA = [{"img":"", "values":[], "img_tk":""}]
        imagetk = li[0]
        # img = image.resize((100,55))
        if isinstance(imagetk, ImageTk.PhotoImage):
            # img_tk= ImageTk.PhotoImage(img)
            ix = self.insert(parent="", index=tk.END, values=li[1:], image=imagetk)
            self.ROWS_DATA.append({"values":li[1:], "imagetk":imagetk})
            self.IXS.append(ix)

    def clearRows(self):
        for item in self.get_children():
            self.delete(item)

    def itemClick(self, e=None) -> tuple:
        """return ('1', '00:12:14.514', 'Marcador 1')"""
        idx = self.selection()
        res = self.item(idx, option="values")
        return res

        


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('600x220')
    wg = Tree(vn)
    wg.grid(row=0, column=0, sticky='wens')
    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()