# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Success:
    def __init__(self, master):
        self.master = master
        master.title("Sucesso!")

        self.label = Label(master, text="Olha só, você acertou!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=lambda:self.next_question(master))
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command)
        # self.close_button.pack()

    def next_question(self, master):
        # self.label['text'] = 'Digite seu nome ou apelido aquie'
        print("Proxima pergunta!")
        master.destroy()
        master.quit()