# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

from random import randint
import csv
import success

numero = 0

class Quiz:
    score = 0
    quantidade_de_perguntas_respondidas = 0
    perguntas_passadas = []

    perguntaSorteada = [] 

    def __init__(self, master):
        self.master = master
        master.title("Bem vindo ao Quiz")
        master.configure(background="white")
        master.geometry("500x500")
        master.resizable(0,0)

        perguntaSorteada = self.sortearPergunta() 

        self.label = Label(master, text=perguntaSorteada[0], bg="white", fg="black", font="none 12 bold")
        self.label.pack()

        self.answer1 = Button(master, text=perguntaSorteada[1], width=14, command= lambda: self.conferirResposta(perguntaSorteada, perguntaSorteada[1])) 
        self.answer1.pack()

        self.answer2 = Button(master, text=perguntaSorteada[2], width=14, command= lambda: self.conferirResposta(perguntaSorteada, perguntaSorteada[2])) 
        self.answer2.pack()

        self.answer3 = Button(master, text=perguntaSorteada[3], width=14, command= lambda: self.conferirResposta(perguntaSorteada, perguntaSorteada[3])) 
        self.answer3.pack()

        # self.close_button = Button(master, text="Sair", command=master.quit)
        # self.close_button.pack()

    def sortearPergunta(self):
        base = open('perguntas_faceis.csv', 'r')
        try:
            leitor = csv.reader(base, delimiter=';')
            i = 0
            ramdom_number = randint(0,9)
            for linha in leitor:                
                if( i == ramdom_number ):
                    return linha
                i = i+1
        finally:
            base.close()
    
    def conferirResposta(self, pergunta_sorteada, resposta):
        print(pergunta_sorteada[4])
        indice_resposta_certa = int(pergunta_sorteada[4])
        if(pergunta_sorteada[indice_resposta_certa] == resposta):
            self.score += 10
            self.quantidade_de_perguntas_respondidas += 1
            print("voce ganhou")
            success_window=Tk()
            success.Success(success_window)
            success_window.mainloop()
            # sortearPergunta()
        else:
            print("voce perdeu")
            # teste.config("Voce perdeu, sorry")

# root = Tk()
# my_gui = Quiz(root)
# root.mainloop()