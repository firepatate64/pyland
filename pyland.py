##imports/variables
from tkinter import*
from tkinter.messagebox import *
import tkinter.font as tkFont
import random
import os
from pypresence import Presence # The simple rich presence client in pypresence
import time
client_id = "847471521790033923"  # Put your Client ID in here
RPC = Presence(client_id)  # Initialize the Presence client
RPC.connect()
RPC.update(state="Joue à Pyland.exe", large_image="unknown", details="Construction d'une ile en cours...", start=200, end=100,buttons=[{"label": "Télecharger", "url": "https://bit.ly/34n2YGv"}], party_size=[1,1])
root = Tk()
canvas = Canvas(root, bg='sky blue', width=980, height=980)
width = 980
height = 980
pasplein = True
grille = []
for i in range(50):
    grille.append([0]*50)
grille[25][25] = 2
grille[24][25] = 2
grille[26][25] = 2
grille[25][26] = 2
grille[25][24] = 2
grille[26][26] = 1
grille[24][24] = 1
grille[27][25] = 1
grille[25][27] = 1
grille[25][23] = 1
grille[23][25] = 1
grille[26][24] = 1
grille[24][26] = 1

scorevar = 20
type = 0
event100 = False
event200 = False
event500 = False
event1000 = False
event2000 = False
event5000 = False
aunbato = False
auneusine = False
oujensuis = 0

try:
    fichier = open("data.sauv", "r")
    grille = eval(fichier.read())
    fichier.close()
    fichier = open("score.sauv", "r")
    scorevar = eval(fichier.read())
    fichier.close()
    fichier = open("event.sauv", "r")
    oujensuis = eval(fichier.read())
    fichier.close()
except:
    fichier = open("data.sauv", "x")
    fichier.write(str(grille))
    fichier.close()
    fichier = open("score.sauv", "x")
    fichier.write(str(scorevar))
    fichier.close()
    fichier = open("event.sauv", "x")
    fichier.write(str(oujensuis))
    fichier.close()
##fonctions


def screenbase():
    global oujensuis
    global aunbato
    global auneusine
    i1 = 0
    i2 = 0
    for a in grille:
        for i in a:
            x2 = i2-i1*50
            if i == 0:
                pass
            elif i == 1:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='yellow')
            elif i == 2:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
            elif i == 4 or i == 8:
                grille[i1] = 4
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='dark green')
                arbre(i1,x2)
            elif i == 3 or i == 6:
                grille[i1] = 3
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='yellow')
                canvas.create_rectangle(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='green')
                cactusgrand(i1,x2)
            elif i == 20 or i == 40:
                grille[i1] = 20
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='spring green')
                pommiermure(i1,x2)
            elif i == 25 or i == 60:
                grille[i1] = 25
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='spring green')
                citronmure(i1,x2)
            elif i == 50:
                poissonerie(i1*20,x2*20)
                createpoisson(i1,x2)
            elif i == 100:
                armada(i1*20,x2*20)
                aunbato = True
            elif i == 200:
                createusine(i1*20,x2*20)
                auneusine = True
            i2 = i2+1
        i1 = i1+1
        score['text'] = scorevar
        eventbase(oujensuis)
def eventbase(sc):
    sc = int(sc)
    global scorevar
    global event100
    global event200
    global event500
    global event1000
    global event2000
    global event5000
    global oujensuis
    global aunbato
    global auneusine
    if(sc>=50 and not event100):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item cactus. Pour information, les cactus rapportent plus que les arbres mais ils possent moins vite et ils se plantent uniquement sur le sable, le prochain item sera débloqué à 200 points.')):
            boutoncactus = Button(root1,text="Planter des cactus",command = cactus, bg='green3',width=42,height=2)
            boutoncactus.pack()
            event100=True
    if(sc>=200 and not event200):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item pommier. Pour information, les pommiers rapportent autant que les arbres et quand on recupère les pommes, le pommier reste. Ils se plantent sur l\'herbe, le prochain item sera débloqué à 500 points.')):
            boutoncactus = Button(root1,text="Planter des pommiers",command = pommier, bg='spring green',width=42,height=2)
            boutoncactus.pack()
            event200=True
    if(sc>=500 and not event500):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item poisson. Pour information, les poissons se mettent dans la mer afin qu\'ils se reproduisent et qu\'on puisse les vendrent, le prochain item sera débloqué à 1000 points.')):
            boutoncactus = Button(root1,text="Acheter un poisson",command = poisson, bg='blue',width=42,height=2)
            boutoncactus.pack()
            event500=True
    if(sc>=1000 and not event1000):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item pêcheur. Pour information, le bateau de pêche se met sur l\'océan et pêche les poissons pour votre compte, le prochain item sera débloqué à 2000 points.')):
            event1000=True
            if(not aunbato):
                boutoncactus = Button(root1,text="Pêcher des poissons",command = pechetout, bg='grey',width=42,height=2)
                boutoncactus.pack()
            else:
                boutoncactus = Button(root1,text="Acheter un navire de pêche",command = peche, bg='cornflower blue',width=42,height=2)
                boutoncactus.pack()
    if(sc>=2000 and not event2000):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item citronnier. Pour information, les citronniers se met sur l\'herbe et rapportent plus que les pommiers mais ne poussent que si ils sont placés sur le bord de mer, le prochain item sera débloqué à 5000 points')):
            boutoncactus = Button(root1,text="Acheter citronnier",command = citron, bg='yellow',width=42,height=2)
            boutoncactus.pack()
            event2000=True
    if(sc>=5000 and not event5000):
        if(True or showinfo(title='Évennement',message='Vous avez débloqué l\'item ferme à fruit. Pour information, la ferme se met sur l\'herbe et ressemble au bateau de pêche mais pour les plantes.')):
            boutoncactus = Button(root1,text="Acheter ferme",command = ferme, bg='ivory3',width=42,height=2)
            boutoncactus.pack()
            event5000=True

def screen(evt):
    global scorevar
    global type
    global aunbato
    global auneusine
    i1 = 0
    i2 = 0
    x = evt.x//20
    y = evt.y//20
    pousseoupas =True
    if(type==4 and grille[x][y] != 2):
        pousseoupas = False
    if(type==50 and grille[x][y] != 0):
        pousseoupas = False
    if(type==100 and grille[x][y] != 0):
        pousseoupas = False
    if(type==100 and aunbato):
        pousseoupas = False
    if(type==200 and auneusine):
        pousseoupas = False
    if(type==200 and grille[x][y] != 2):
        pousseoupas = False
    if(type==25 and grille[x][y] != 2):
        pousseoupas = False
    if(type==3 and grille[x][y] != 1):
        pousseoupas = False
    if(type==999 and grille[x][y] == 8):
        pousseoupas = False
        grille[x][y] = 2
        scorevar = scorevar+8
        score['text'] = scorevar
        canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='green')
    if(type==999 and grille[x][y] == 12):
        pousseoupas = False
        grille[x][y] = 1
        scorevar = scorevar+10
        score['text'] = scorevar
        canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='yellow')
    if(type==999 and grille[x][y] == 40):
        pousseoupas = False
        grille[x][y] = 20
        scorevar = scorevar+8
        score['text'] = scorevar
        canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='spring green')
        root.after(20000,lambda: pommiermure(x,y))
    if(type==999 and grille[x][y] == 60):
        pousseoupas = False
        grille[x][y] = 25
        scorevar = scorevar+15
        score['text'] = scorevar
        canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='spring green')
        root.after(10000,lambda: citronmure(x,y))
    if(type==999 and grille[x][y] == 50):
        pousseoupas = False
        grille[x][y] = 0
        canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='sky blue')
        scorevar = scorevar+25
        score['text'] = scorevar
    if(scorevar-type>=0  and pousseoupas and type!=0 and type!=999):
        if(grille[x+1][y]!=0 or grille[x-1][y]!=0 or grille[x][y+1]!=0 or grille[x][y-1]!=0):
            if(grille[evt.x//20][evt.y//20] != type):
                scorevar = scorevar-type
                score['text'] = scorevar
                print('yellow : ',i1,i2)
            if type == 4:
                root.after(10000,lambda: arbre(x,y))
            if type == 50:
                root.after(20000,lambda: createpoisson(x,y))
            if type == 3:
                root.after(20000,lambda: cactusgrand(x,y))
            if type == 20:
                root.after(20000,lambda: pommiermure(x,y))
            if type == 25:
                root.after(10000,lambda: citronmure(x,y))
            if type == 100 and not aunbato:
                boutoncactus = Button(root1,text="Pêcher des poissons",command = pechetout, bg='grey',width=42,height=2)
                boutoncactus.pack()
                aunbato = True
            if type == 200 and not auneusine:
                boutoncactus = Button(root1,text="Ramasser les fruits",command = ramassetout, bg='grey',width=42,height=2)
                boutoncactus.pack()
                auneusine = True
            grille[evt.x//20][evt.y//20] = type
            i = type
            i1 = x
            x2 = y
            if i == 0:
                pass
            elif i == 1:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='yellow')
            elif i == 2:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
            elif i == 4:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='dark green')
            elif i == 3:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='yellow')
                canvas.create_rectangle(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='green')
            elif i == 20:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='spring green')
            elif i == 25:
                canvas.create_rectangle(i1*20,x2*20,i1*20+20,x2*20+20,fill='green')
                canvas.create_oval(i1*20+5,x2*20+5,i1*20+15,x2*20+15,fill='spring green')
            elif i == 50:
                poissonerie(x*20,y*20)
            elif i == 100:
                armada(x*20,y*20)
            elif i == 200:
                createusine(x*20,y*20)
    print('mouse : ',evt.x,evt.y)
    event(scorevar)
def event(sc):
    global scorevar
    global event100
    global event200
    global event500
    global event1000
    global event2000
    global event5000
    global oujensuis
    if(sc>=50 and not event100):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item cactus. Pour information, les cactus rapportent plus que les arbres mais ils possent moins vite et ils se plantent uniquement sur le sable, le prochain item sera débloqué à 200 points.')):
            boutoncactus = Button(root1,text="Planter des cactus",command = cactus, bg='green3',width=42,height=2)
            boutoncactus.pack()
            event100=True
            oujensuis = 100
    if(sc>=200 and not event200):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item pommier. Pour information, les pommiers rapportent autant que les arbres et quand on recupère les pommes, le pommier reste. Ils se plantent sur l\'herbe, le prochain item sera débloqué à 500 points.')):
            boutoncactus = Button(root1,text="Planter des pommiers",command = pommier, bg='spring green',width=42,height=2)
            boutoncactus.pack()
            oujensuis = 200
            event200=True
    if(sc>=500 and not event500):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item poisson. Pour information, les poissons se mettent dans la mer afin qu\'ils se reproduisent et qu\'on puisse les vendrent, le prochain item sera débloqué à 1000 points.')):
            boutoncactus = Button(root1,text="Acheter un poisson",command = poisson, bg='blue',width=42,height=2)
            boutoncactus.pack()
            event500=True
            oujensuis = 500
    if(sc>=1000 and not event1000):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item pêcheur. Pour information, le bateau de pêche se met sur l\'océan et pêche les poissons pour votre compte, le prochain item sera débloqué à 2000 points.')):
            boutoncactus = Button(root1,text="Acheter un navire de pêche",command = peche, bg='cornflower blue',width=42,height=2)
            boutoncactus.pack()
            event1000=True
            oujensuis = 1000
    if(sc>=2000 and not event2000):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item citronnier. Pour information, les citronniers se met sur l\'herbe et rapportent plus que les pommiers mais ne poussent que si ils sont placés sur le bord de mer, le prochain item sera débloqué à 5000 points')):
            boutoncactus = Button(root1,text="Acheter citronnier",command = citron, bg='yellow',width=42,height=2)
            boutoncactus.pack()
            event2000=True
            oujensuis = 2000
    if(sc>=5000 and not event5000):
        if(showinfo(title='Évennement',message='Vous avez débloqué l\'item ferme à fruit. Pour information, la ferme se met sur l\'herbe et ressemble au bateau de pêche mais pour les plantes.')):
            boutoncactus = Button(root1,text="Acheter ferme",command = ferme, bg='ivory3',width=42,height=2)
            boutoncactus.pack()
            event5000=True
            oujensuis = 5000
def sableu():
    global type
    type = 1
    bouton['bg'] = 'yellow'
def herbe():
    global type
    type = 2
    bouton['bg'] = 'green'
def plante():
    global type
    type = 4
    bouton['bg'] = 'dark green'
def pommier():
    global type
    type = 20
    bouton['bg'] = 'spring green'
def citron():
    global type
    type = 25
    bouton['bg'] = 'spring green'
def poissonerie(x,y):
    canvas.create_oval(x+1,y+5,x+11,y+15,fill='blue')
    canvas.create_polygon(x+11,y+10,x+19,y+15,x+19,y+5,fill='blue')
def armada(x,y):
    canvas.create_arc(x,y,x+20,y+20,start=180,extent=180,fill='white')
    canvas.create_polygon(x+7,y+10,x+17,y+10,x+7,y)
def createusine(x,y):
    canvas.create_rectangle(x+5,y+5,x+15,y+15,fill="ivory3")
    canvas.create_polygon(x+5,y+5,x+15,y+5,x+10,y)
def poisson():
    global type
    type = 50
    bouton['bg'] = 'blue'
def peche():
    global type
    type = 100
    bouton['bg'] = 'white'
def ferme():
    global type
    type = 200
    bouton['bg'] = 'ivory3'
def cactus():
    global type
    type = 3
    bouton['bg'] = 'green3'
def pechetout():
    global scorevar
    x=0
    y=0
    ib=0
    for a in grille:
        for i in a:
            if i == 50 and random.choice([True,False]):
                y = ib-50*x
                grille[x][y] = 0
                canvas.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill='sky blue')
                scorevar = scorevar+25
                score['text'] = scorevar
            ib = ib+1
        x = x+1
def rampomme(x,y):
    global scorevar
    grille[x][y] = 20
    canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='spring green')
    scorevar = scorevar+8
    score['text'] = scorevar
    root.after(20000,lambda: pommiermure(x,y))
def ramcitron(x,y):
    global scorevar
    grille[x][y] = 25
    canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='spring green')
    scorevar = scorevar+15
    score['text'] = scorevar
    root.after(10000,lambda: citronmure(x,y))
    event(scorevar)
def ramassetout():
    global scorevar
    x=0
    y=0
    ib=0
    for a in grille:
        for i in a:
            if i == 40 and random.choice([True,False]):
                y = ib-50*x
                rampomme(x,y)
            ib = ib+1
        x = x+1
    x=0
    y=0
    ib=0
    for a in grille:
        for i in a:
            if i == 60 and random.choice([True,False]):
                y = ib-50*x
                ramcitron(x,y)
            ib = ib+1
        x = x+1
    event(scorevar)
def createpoisson(x,y):
    if x<49 and y<49 and x>0 and y>0:
        root.after(20000,lambda: createpoisson(x,y))
        if grille[x][y] == 50 and random.choice([True,False]):
            if grille[x+1][y]==0:
                poissonerie(x*20+20,y*20)
                grille[x+1][y] = 50
                root.after(20000,lambda: createpoisson(x+1,y))
            if grille[x-1][y]==0 and random.choice([True,False]):
                poissonerie(x*20-20,y*20)
                grille[x-1][y] = 50
                root.after(20000,lambda: createpoisson(x-1,y))
            if grille[x][y+1]==0 and random.choice([True,False]):
                poissonerie(x*20,y*20+20)
                grille[x][y+1] = 50
                root.after(20000,lambda: createpoisson(x,y+1))
            if grille[x][y-1]==0 and random.choice([True,False]):
                poissonerie(x*20,y*20-20)
                grille[x][y-1] = 50
                root.after(20000,lambda: createpoisson(x,y-1))
def cactusgrand(x,y):
    if grille[x][y] == 3:
        canvas.create_line(x*20+5,y*20+5,x*20+8,y*20+8)
        canvas.create_rectangle(x*20+8,y*20+8,x*20+18,y*20+18,fill='green')
        grille[x][y] = 12
def arbre(x,y):
    if grille[x][y] == 4:
        canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='brown')
        grille[x][y] = 8
def pommiermure(x,y):
    if grille[x][y] ==20:
        canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='red')
        grille[x][y] = 40
def citronmure(x,y):
    if grille[x][y] ==25:
        if grille[x+1][y] == 0 or grille[x-1][y] == 0 or grille[x][y+1] == 0 or grille[x][y-1] == 0 or grille[x+1][y] == 50 or grille[x-1][y] == 50 or grille[x][y+1] == 50 or grille[x][y-1] == 50:
            canvas.create_oval(x*20+5,y*20+5,x*20+15,y*20+15,fill='yellow')
            grille[x][y] = 60
def vendre():
    global type
    type = 999
    bouton['bg'] = 'grey'
def trucecran():
    global pasplein
    if pasplein:
        root.attributes('-fullscreen', True)
        pasplein = False
        pleinecranbouton['text'] = 'Enlever le mode plein écran'
    else:
        root.attributes('-fullscreen', False)
        pleinecranbouton['text'] = 'Mettre en mode plein écran'
        pasplein = True
def sauv():
    fichier = open("data.sauv", "w")
    fichier.write(str(grille))
    fichier.close()
    fichier = open("score.sauv", "w")
    fichier.write(str(scorevar))
    fichier.close()
    root.destroy()
##grille
for line in range(0, width, 20): # range(start, stop, step)
    canvas.create_line([(line, 0), (line, height)], fill='black', tags='grid_line_w')

for line in range(0, height, 20):
    canvas.create_line([(0, line), (width, line)], fill='black', tags='grid_line_h')
root.title('Pyland 0.5')
canvas.pack(side=LEFT)
root1 = Frame(root,relief=GROOVE)
root1.pack(side=LEFT,padx=200)
helv36 = tkFont.Font(family='Helvetica', size=36, weight='bold')
helv26 = tkFont.Font(family='Helvetica', size=26, weight='bold')
bouton = Button(root1,text="",bg='blue',width=20,height=7)
bouton.pack(side=TOP)
score = Label(root1, text='0',width = 10,bg='grey', font = helv36)
score.pack()
boutonsable = Button(root1,text="Sable",command = sableu, bg='yellow',width=42,height=2,anchor=CENTER)
boutonsable.pack()
boutonherbe = Button(root1,text="Herbe",command = herbe, bg='green',width=42,height=2,anchor=CENTER)
boutonherbe.pack()
boutonplante = Button(root1,text="Planter des arbres",command = plante, bg='dark green',width=42,height=2,anchor=CENTER)
boutonplante.pack()
vendreboutton = Button(root1,text="Vendre",command = vendre, bg='grey',width=42,height=2,anchor=CENTER)
vendreboutton.pack()
pleinecranbouton = Button(root1,text="Mettre en mode plein écran",command = trucecran, bg='grey',width=42,height=2,anchor=CENTER)
pleinecranbouton.pack()

quiterbouton = Button(root1,text="Quitter",command = sauv, bg='grey',width=42,height=2,anchor=CENTER)
quiterbouton.pack()
screenbase()
showinfo(title='Infos',message='Bienvenue sur votre île ! Vous pouvez dès maintenant l\'agrandir et planter des arbres dessus puis les vendrent pour débloquer un nouvel item à 50 points !')
root.bind("<Button-1>", screen)
root.mainloop()