#My Glossary Project

try:
	from tkinter import *
except:
	from Tkinter import *

##### main:
window = Tk()
window.title("Jogo Quiz")
window.configure(background ="black")

#create label
Label (window, text="Vamos Jogar?", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

#create a text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=6, column=0, sticky=W)

def openGamePage():
	gamePage = Tk()
	gamePage.title('Jogo')
	gamePage.configure(background="black")
	nomeText = Entry(gamePage, width=20, bg="white")
	nomeText.grid(row=1, column=0, sticky=w)

#add a submit button
Button(window, text="Jogar!", width=6, command=openGamePage) .grid(row=2, column=0, sticky=W)

#create another label
Label (window, text="Ver o Ranking", bg="black", fg="white", font="none 12 bold") .grid(row=3, column=0, sticky=W)

def openRanking():
	rankingPage = Tk()
	rankingPage.title('Ranking')

#add a submit button
Button(window, text="Ranking", width=6, command=openRanking) .grid(row=4, column=0, sticky=W)

#create a text box
# output = Text(window, width=75, height=6, wrap=WORD, background="white")
# output.grid(row=5, column=0, columnspan=2, sticky=W)
#the dictionary

#####run the main loop
window.mainloop()