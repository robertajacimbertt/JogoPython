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

        self.greet_button = Button(master, text="Greet", command=self.next_question)
        self.greet_button.pack()

        # self.close_button = Button(master, text="Close", command)
        # self.close_button.pack()

    def next_question(self):
        print("Proxima pergunta!")
        self.destroy()