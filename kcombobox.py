from tkinter import ttk
import tkinter as tk


class KCombobox(ttk.Combobox):
    def __init__(self, parent=None, fg='black', bg='white', *args, **kw):
        super().__init__(master=parent, *args, **kw)
        self.parent = parent
        self.bg = bg
        self.fg = fg
        self.ELEMENTOS = []
        self._config_KCombobox()

    def _config_KCombobox(self):
        bg, fg = self.bg, self.fg
        self.scb = ttk.Style()
        self.scb.theme_use('default')
        self.scb.configure(
            'scb.TCombobox',
            foreground=fg,
            background=bg,
            bordercolor=bg,
            borderwidth=0,
            arrowcolor=fg,
            relief='flat',
            selectbackground=bg,
            selectforeground=fg,
            takefocus=False,
            fieldbackground=bg
        )
        self.scb.map('scb.TCombobox',fieldbackground=[('readonly',bg)])
        self.option_add('*TCombobox*Listbox.selectBackground', fg)
        self.option_add('*TCombobox*Listbox.selectForeground', bg)
        # self.config(style='scb.TCombobox', state='readonly', font=('Consolas',12,'bold'))
        self.config(style='scb.TCombobox', font=('Consolas',12,'bold'))

        # Configurar el layout del Combobox
        self.scb.layout("scb.TCombobox", [
            ("Combobox.field", {
                "children": [
                    ("Combobox.downarrow", {"side": "right"}),  # Flecha desplegable
                    ("Combobox.padding", {
                        "children": [
                            ("Combobox.textarea", {"sticky": "nswe"})  # Campo de entrada (Entry)
                        ]
                    })
                ]
            })
        ])
        

    @property
    def items(self):
        return self.ELEMENTOS

    @items.setter
    def items(self, lista):
        self.ELEMENTOS = lista
        self.config(values=self.ELEMENTOS)

    @property
    def elegido(self):
        return self.get()

    @elegido.setter
    def elegido(self, elem):
        self.set(elem)

    @property
    def indice(self):
        return self.current()

    @indice.setter
    def indice(self, i):
        self.current(i)

    def elemento_agrega(self, elem):
        valores = list(self['values'])
        valores.append(str(elem))
        self['values'] = valores

    def asigna_metodo(self, metodo):
        self.bind('<<ComboboxSelected>>', metodo)


if __name__=='__main__':
    rz = tk.Tk()
    rz.geometry('260x25')
    wg = KCombobox(fg='RoyalBlue1')
    wg.grid(row=0, column=0, sticky='wens')
    wg.items = ['', 'active', 'disabled', 'readonly', 'normal']
    rz.columnconfigure(0, weight=1)
    rz.rowconfigure(0, weight=1)
    rz.title('KCombobox')
    rz.mainloop()
