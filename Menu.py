# coding=latin-1
# -*- coding: utf-8 -*-
try:
    from Tkinter import *
except:
    from tkinter import *

from Dialog import Dialog
import pandas as pd
import csv
import GameInit

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

        self.game_button = Button(master, text="Jogar", command=self.init_game)
        self.game_button.pack()

        self.ranking_button = Button(master, text="Ranking", command=self.open_ranking)
        self.ranking_button.pack()

        self.close_button = Button(master, text="Sair", command=master.quit)
        self.close_button.pack()

    def init_game(self):
        print("Init Game!")
        user_name=self.entry_name.get()
        if user_name: 
            print("Olá ", user_name)
            game_init_window=Tk()
            GameInit.GameInit(game_init_window)
            game_init_window.mainloop()
        else:
            print("Usuario não digitou o nome")
            self.label_erro['text'] = 'Digite seu nome ou apelido'

    def open_ranking(self):
        print("Ranking!")
        # base = pd.read_csv('perguntas_faceis.csv')
        # pergunta_completa = base[['pergunta']].values
        # print(pergunta_completa)
        base = open('perguntas_faceis.csv', 'r')
        linha_selecionada = []
        try:
            leitor = csv.reader(base)
            i = 0
            ramdom_number = 3
            for linha in leitor:
                # print(i, linha)
                if( i == ramdom_number ):
                    linha_selecionada = linha
                i = i+1
        finally:
            base.close()
            print("Linha escolhida --> ", linha_selecionada)
            self.label_erro['text'] = linha_selecionada[0]

root = Tk()
my_gui = Menu(root)
root.mainloop()