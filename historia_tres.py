# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Historia:
    def __init__(self, master):
        self.master = master
        master.title("Parte 4 - Está quase lá, falta pouco")

        self.label = Label(master, text="Parte 4 - Está quase lá, falta pouco")
        self.label.pack()

        self.greet_button = Button(master, text="Próximo", command= lambda: self.next(master))
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def next(self, master):
        master.destroy()
        import quiz_quatro
        jogo_quatro=Tk()
        quiz_quatro.Quiz(jogo_quatro)
        jogo_quatro.mainloop()

# root = Tk()
# my_gui = GameInit(root)
# root.mainloop()
