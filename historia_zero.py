# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

import quiz_um

class Historia:
    def __init__(self, master):
        self.master = master
        master.title("Parte 1 - O objetivo de conquista")

        self.label = Label(master, text="Parte 1 - O objetivo de conquista")
        self.label.pack()

        self.greet_button = Button(master, text="Próximo", command=self.next)
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def next(self):
        jogo_um=Tk()
        quiz_um.Quiz(jogo_um)
        jogo_um.mainloop()

# root = Tk()
# my_gui = GameInit(root)
# root.mainloop()
