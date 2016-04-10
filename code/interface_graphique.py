from tkinter import *
from tkinter.filedialog import *
x=1
y=0
c=-2
MJ=12
MC=19

hand_croupier = ['5_coeur', '5_trefle', '4_coeur', '5_carreau']
hand_joueur = ['dame_coeur', '2_pique']

cartes_joueur = []
cartes_croupier = []

fenetre = Tk()  #fenetre principale

champ_label = Label(fenetre, text="Jeu de Blackjack")
champ_label.pack()

table = Frame(fenetre, width=1, height=1, borderwidth=0, bg="#1D702D")#cadre ou il y aura les cartes
table.pack(side = RIGHT)

bouton_Carte = Button(fenetre, text="Carte")#bouton pour piocher une carte
bouton_Carte.pack(pady=10)
bouton_Rester = Button(fenetre, text="Rester")#bouton pour s'arrêter
bouton_Rester.pack(pady=10)
message1 = Label(fenetre, text="Votre score : "+str(y))#Scores
message1.pack(pady=10)
message2 = Label(fenetre, text="Score du croupier : "+str(x))
message2.pack(pady=10)
message3 = Label(fenetre, text="Compte : "+str(c))#compte des cartes
message3.pack(pady=10)

canvas = Canvas(table ,width = 500, height = 520, bg = "#1D702D")#emplacement des cartes
canvas.pack()

def affiche_cartes(hand,y,cartes):#fonction qui affiche les cartes sur la table
    a=len(hand)
    for i in range(a):
        carte = hand[i]
        cartes.append( PhotoImage(file = "..\\cartes\\" + carte +".gif") )
        canvas.create_image((10+100*i), y, image = cartes[i], anchor = NW)

def distribuer():
    affiche_cartes(hand_joueur, 300, cartes_joueur)
    affiche_cartes(hand_croupier, 40, cartes_croupier)
    canvas.create_text(50, 500, text = "Vous avez "+str(MJ), fill = "white")# Le total de la main du joueur
    canvas.create_text(50, 20, text = "Le croupier a "+str(MC), fill = "white")#Le total de la main du croupier

def rejouer():#fonction du bouton rejouer
    del cartes_joueur[:]
    cartes_croupier[:] = []
    mj=0
    mc=0
    canvas.delete(ALL)

    del hand_croupier[:]
    del hand_joueur[:]
    hand_croupier.append('4_coeur')
    hand_joueur.append('roi_coeur')

    distribuer()

bouton_rejouer = Button(fenetre, text="Rejouer" , command = rejouer)#bouton rejouer
bouton_rejouer.pack(side="top")

bouton_quitter = Button(fenetre, text="Quitter", command = fenetre.destroy)#bouton quitter
bouton_quitter.pack(side="bottom")

#Programme principal
distribuer()

fenetre.mainloop()

