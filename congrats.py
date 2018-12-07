# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Congrats:
    def __init__(self, master):
        self.master = master
        master.title("Parabens!")

        self.label = Label(master, text="Parabens!")
        self.label.pack()

        self.greet_button = Button(master, text="Próximo", command= lambda: self.next(master))
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def next(self, master):
        master.destroy()
        import Menu
        menu_tela=Tk()
        Menu.Menu(menu_tela)
        menu_tela.mainloop()
        return True

# root = Tk()
# my_gui = GameInit(root)
# root.mainloop()
