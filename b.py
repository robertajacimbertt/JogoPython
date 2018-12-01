from Tkinter import *
class Janela1:
    def __init__(self,toplevel):
        self.fr1 = Frame(toplevel)
        self.fr1.pack()
        self.botao = Button(self.fr1, text='Abrir!', background='green')
        self.botao.bind("<Button-1>",self.abre)
        self.botao.pack()

    def abre(self,event):
        raiz=Tk()
        
        
raiz=Tk()
Janela1(raiz)
raiz.mainloop()