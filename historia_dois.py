# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Historia:
    def __init__(self, master):
        self.master = master
        master.title("Parte 3 - Você leva jeito...")

        self.label = Label(master, text="Parte 3 - Você leva jeito...")
        self.label.pack()

        self.greet_button = Button(master, text="Próximo", command= lambda: self.next(master))
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command=master.quit)
        # self.close_button.pack()

    def next(self, master):
        master.destroy()
        import quiz_tres
        jogo_tres=Tk()
        quiz_tres.Quiz(jogo_tres)
        jogo_tres.mainloop()
        return True

# root = Tk()
# my_gui = GameInit(root)
# root.mainloop()
