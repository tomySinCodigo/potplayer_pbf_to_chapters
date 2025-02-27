import tkinter as tk
from tkinter import ttk
from mi_tree import MiTree


class TestOne(MiTree):
    def __init__(self, parent, *args, **kw):
        super(TestOne, self).__init__(parent=parent, *args, **kw)
        self.parent = parent
        self._configTestOne()

    def _configTestOne(self):
        s = ttk.Style()
        s.theme_use('alt')
        s.configure(
            "mi.Treeview",
            background="gray10",
            foreground="azure",
            font="Consolas 9 bold",
            fieldbackground="red",
            bordercolor="green",
            borderwidth=2,
        )
        s.configure(
            "mi.Treeview.Heading",
            background="gray10",  # Fondo de los encabezados
            foreground="azure",    # Texto blanco
            font=("Arial", 12, "bold"),  # Fuente del encabezado
            relief="flat"
        )
        s.map(
            "mi.Treeview.Heading",
            background=[("active", "#555555")]  # Fondo más claro al pasar el mouse
        )
        s.map(
            "mi.Treeview",
            background=[("selected", "skyblue")]
        )

        self.config(style="mi.Treeview")



if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry('400x220')
    wg = TestOne(vn)
    wg.grid(row=0, column=0, sticky='wens')
    vn.columnconfigure(0, weight=1)
    vn.rowconfigure(0, weight=1)
    vn.mainloop()