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
            ramdom_number = randint(1,9)
            for linha in leitor:                
                if( i == ramdom_number ):
                    return linha
                i = i+1
        finally:
            base.close()
    
    def conferirResposta(self, pergunta_sorteada, resposta):
        print(pergunta_sorteada[4])
        indice_resposta_certa = int(pergunta_sorteada[4])
        print("Indice da resposta certa ", pergunta_sorteada[indice_resposta_certa])
        if(pergunta_sorteada[indice_resposta_certa] == resposta):
            self.score += 10
            self.quantidade_de_perguntas_respondidas += 1
            print("voce ganhou", self.quantidade_de_perguntas_respondidas)
            if(self.quantidade_de_perguntas_respondidas >= 5):
                # abrir a tela de historia do proximo nivel
                print("oi")
                self.master.destroy()
            else:
                new_line = self.sortearPergunta() 
                self.updateQuestion(new_line)
                success_window=Tk()
                success.Success(success_window)
                success_window.mainloop()
        else:
            print("Voce perdeu, sorry")
            # teste.config("Voce perdeu, sorry")

    def updateQuestion (self, linha):
        self.label['text'] = linha[0]
        self.answer1['command'] = lambda: self.conferirResposta(linha, linha[1])
        self.answer1['text'] = linha[1]
        self.answer2['command'] = lambda: self.conferirResposta(linha, linha[2])
        self.answer2['text'] = linha[2]
        self.answer3['command'] = lambda: self.conferirResposta(linha, linha[3])
        self.answer3['text'] = linha[3]

# root = Tk()
# my_gui = Quiz(root)
# root.mainloop()