# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Menu:    
    def __init__(self, master):
        self.master = master
        master.title("Bem vindo ao Quiz")

        self.label = Label(master, text="Pronto? Então digite o seu nome para começar!")
        self.label.pack()

        self.entry_name = Entry(master, validate="key")
        self.entry_name.pack()

        self.label_erro = Label(master, text="")
        self.label_erro.pack()

        self.game_button = Button(master, text="Jogar", command= lambda: self.init_game(master))
        self.game_button.pack()

        self.close_button = Button(master, text="Sair", command=master.quit)
        self.close_button.pack()

    def init_game(self, master):
        user_name=self.entry_name.get()
        if user_name: 
            master.destroy()
            import historia_zero
            historia_primeira_parte=Tk()
            historia_zero.Historia(historia_primeira_parte)
            historia_primeira_parte.mainloop()
        else:
            self.label_erro['text'] = 'Digite seu nome ou apelido'
    
root = Tk()
my_gui = Menu(root)
root.mainloop()
