from Tkinter import *
import time

jpas = Tk()
jpas.title("Cadastro de senha")

def bt_oksenha():
    p1=str(passwd.get())
    lb["text"] =str("A senha digitada foi {}".format(p1))


def bt_entrar(passw1=None):
    p1=str(passwd.get())
    p2=str(confpas.get())
    if p1 == p2:
        lb["text"] = str("Login Efetuado com Sucesso")
        time.sleep(5)
        jpas.destroy()
    else:
        lb["text"] = str("Senha incorreta")

passwd = Entry(jpas)
passwd.place(x=100, y=100)

confpas = Entry(jpas)
confpas.place(x=100, y=130)

btgravasenha = Button(jpas, text="GRAVA SENHA", width=20, command=bt_oksenha)
btgravasenha.place(x=100, y=170)
btentrar = Button(jpas, text="ENTRAR NO SISTEMA", width=20, command=bt_entrar)
btentrar.place(x=100, y=210)

lb = Label(jpas, text="Senha nao cadastrado")
lb.place(x=100, y=250)

jpas.geometry("500x500+0+0")
jpas.mainloop()

janela = Tk()
janela.title("Meu Programa")

def bt_iniciar():
    janela2 = Tk()
    janela2.title("teste")
    janela2["bg"] = "red"
    janela2.geometry("700x300+0+0")
    janela2.mainloop()

def bt_sair():
    janela.destroy()

btIniciar = Button(janela, text='Iniciar', width=10, command=bt_iniciar)
btIniciar.place(x=0, y=0)

janela.geometry("1024x768+0+0")
janela.mainloop()