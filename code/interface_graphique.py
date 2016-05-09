import globalVars
from decklist import *
from tkinter import *
from tkinter.filedialog import *

def affiche_cartes(hand,y,cartes):#fonction qui affiche les cartes sur la table
    a=len(hand)                   #y est la hauteur ou l'on affiche les cartes
    for i in range(a):
        carte = hand[i]
        cartes.append( PhotoImage(file = "..\\cartes\\" + carte +".gif") )
        canvas.create_image((10+100*i), y, image = cartes[i], anchor = NW)
        
def affiche_table():#fonction qui affiche les objets de la table
    del cartes_joueur[:]
    del cartes_croupier[:]
    canvas.delete(ALL)#enleve les cartes de la table pour en remettre après
    affiche_cartes(hand_joueur, 300, cartes_joueur)
    affiche_cartes(hand_croupier, 40, cartes_croupier)
    canvas.create_text(50, 500, text = "Vous avez "+str(total(hand_joueur)), fill = "white")# Le total de la main du joueur
    canvas.create_text(50, 20, text = "Le croupier a "+str(total(hand_croupier)), fill = "white")#Le total de la main du croupier
    #afficher le compte et les scores
    textCompte.set("Compte : "+str(globalVars.compte))
    textScore_joueur.set("Votre score : "+str(globalVars.Scores[0]))
    textScore_croupier.set("Score du croupier : "+str(globalVars.Scores[1]))
    fenetre.update_idletasks()

def rejouer():#fonction du bouton rejouer
    #remet les mains et le total des mains à 0
    del hand_croupier[:]
    del hand_joueur[:]
    #distribue des nouvelles cartes et les affiche
    tirer(hand_croupier,1)
    tirer(hand_joueur,  2)
    affiche_table()
    bouton_rejouer.config(state=DISABLED)
    bouton_carte.config(state=ACTIVE)
    bouton_rester.config(state=ACTIVE)
    if total(hand_joueur) >= 21:
        bouton_carte.config(state=DISABLED)
        rester()



def carte():#fonction du bouton carte
    tirer(hand_joueur,1)
    if total(hand_joueur) >= 21:
        bouton_carte.config(state=DISABLED)
        rester()
    affiche_table()

def rester():#fonction du bouton rester
    croupier(hand_croupier)
    gagnant(total(hand_joueur),total(hand_croupier),globalVars.Scores)
    affiche_table()
    bouton_rejouer.config(state=ACTIVE)
    bouton_carte.config(state=DISABLED)
    bouton_rester.config(state=DISABLED)
    winner = gagnant(total(hand_joueur),total(hand_croupier),globalVars.Scores)
    print(winner)
    if winner == 0:
        canvas.create_text(260,260, text = "ÉGALITÉ" , fill="white")
    elif winner == 0.5:
        canvas.create_text(260,260, text = "GAGNÉ" , fill="white")
    else:
        canvas.create_text(260,260, text = "PERDU" , fill="white")
    fenetre.update_idletasks()

def button_aide():
    new_window=Tk()
    cnv = Canvas(new_window,width=900, height=400)
    cnv.pack()
    labl = Label(new_window,text="Aide")
    labl.pack()
    tableau = PhotoImage(file = "tabstrat1.gif", master= cnv)
    cnv.create_image(1,1,image=tableau,anchor = NW)
    new_window.mainloop()

hand_croupier = []
hand_joueur = []

cartes_joueur = []
cartes_croupier = []

fenetre = Tk()  #fenetre principale
textCompte = StringVar()
textScore_joueur = StringVar()
textScore_croupier = StringVar()

champ_label = Label(fenetre, text="Jeu de Blackjack")
champ_label.pack()

table = Frame(fenetre, width=1, height=1, borderwidth=0, bg="#1D702D")#cadre ou il y aura les cartes
table.pack(side = RIGHT)

bouton_carte = Button(fenetre, text="Carte", command=carte)#bouton pour piocher une carte
bouton_rester = Button(fenetre, text="Rester", command=rester)#bouton pour s'arrêter
bouton_carte.config(state=DISABLED)
bouton_rester.config(state=DISABLED)
bouton_carte.pack(pady=10)
bouton_rester.pack(pady=10)

message1 = Label(fenetre, textvariable = textScore_joueur)#Scores
message1.pack(pady=10)
message2 = Label(fenetre, textvariable = textScore_croupier)
message2.pack(pady=10)
message3 = Label(fenetre, textvariable = textCompte)#compte des cartes
message3.pack(pady=10)

canvas = Canvas(table ,width = 500, height = 520, bg = "#1D702D")#emplacement des cartes
canvas.pack()

bouton_rejouer = Button(fenetre, text="Jouer" , command = rejouer)#bouton rejouer
bouton_rejouer.pack(side="top")

boutton_aide = Button(fenetre,text="Aide", command = button_aide )
boutton_aide.pack(side="bottom")

bouton_quitter = Button(fenetre, text="Quitter", command = fenetre.destroy)#bouton quitter
bouton_quitter.pack(side="bottom")

fenetre.mainloop()
