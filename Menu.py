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
        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()
        size = tuple(int(pos) for pos in master.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        master.geometry("%dx%d+%d+%d" % (size + (x, y)))

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
            return True
        else:
            self.label_erro['text'] = 'Digite seu nome ou apelido'
            return False
    
root = Tk()
my_gui = Menu(root)
root.mainloop()
