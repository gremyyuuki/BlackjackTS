DECK = {'ascoeur':11,'2coeur':2,'3coeur':3,'4coeur':4,'5coeur':5,'6coeur':6,'7coeur':7,'8coeur':8,'9coeur':9,'10coeur':10,'valetcoeur':10,'damecoeur':10,'roicoeur':10,'ascarreau':11,'2carreau':2,'3carreau':3,'4carreau':4,'5carreau':5,'6carreau':6,'7carreau':7,'8carreau':8,'9carreau':9,'10carreau':10,'valetcarreau':10,'damecarreau':10,'roicarreau':10,'astrefle':11,'2trefle':2,'3trefle':3,'4trefle':4,'5trefle':5,'6trefle':6,'7trefle':7,'8trefle':8,'9trefle':9,'10trefle':10,'valettrefle':10,'dametrefle':10,'roitrefle':10,'aspique':11,'2pique':2,'3pique':3,'4pique':4,'5pique':5,'6pique':6,'7pique':7,'8pique':8,'9pique':9,'10pique':10,'valetpique':10,'damepique':10,'roipique':10}
# deck = ensemble de cartes du jeu
# _RC_ 20160214 expliquer différences entre deck et DECK
# _RC_ 20160214 il vaut mieux changer de nom que de différencier seulement sur la casse
deck = list(DECK)
import random
import math
import tkinter

Victoires_joueur=0
Victoires_croupier=0

random.shuffle(deck) #Mélange le deck


#Fonction qui tire un nombre de cartes donné.
#En pratique, on tire une ou 2 cartes à la fois.
def tirer(hand,x):
    if x > len(deck):
        print("Pas assez de cartes.")#vérifier que le deck n'est pas vide
        x=len(deck)
    for i in range(x):
        # ne pas utiliser '=', sinon, ne modifie pas la variable passée en paramètre
        hand.append( deck.pop(0) )

def prendre(x):
    y=[]
    for i in range(x):
        tirer(y,1)
    print(y)

prendre(1)



#Fonction qui compte la valeur totale de la main
def total(hand):
    nbrAS=hand.count(11) #Compte le nombre d'as dans la main
    t=sum(hand)
    while nbrAS>0 and t>21:
        t-=10
        nbrAS-=1
    return t

def hand_du_croupier():
    hand=[]
    tirer(hand,1)            #Le croupier commence par tirer une carte
    while total(hand) < 17:
        tirer(hand,1)#Le croupier tire jusqu'a 17 et s'arrete au dessus
    print(hand)
    hand_croupier=total(hand)

def hand_du_joueur():#finir
    x=input("Voulez vous une autre carte ?\nSi oui, tapez h, sinon tapez s:")
    if x == "h":
        tirer(hand,1)
        total(hand)
        if total(hand) <=21:
            hand_du_joueur()
        else:
            gagnant()
    else:
        gagnant()


#Fonction qui compare le score de chaque joueur et affiche le nombre de victoires
def gagnant():
    total(hand)
    # _RC_ OT : hand_croupier est une variable locale à hand_du_croupier()
    # donc non accessible ici
    # de toute façon, hand_croupier est une liste et non un entier
    if hand_croupier == 21:
        print("Blackjack du croupier")
        print("PERDU")
        Victoires_croupier += 1
    elif hand_joueur == 21:
        print("Blackjack !")
        print("GAGNÉ")
        Victoires_joueur += 1
    elif hand_joueur > 21:
        print("Flamby, flambé")
        print("PERDU")
        Victoires_croupier += 1
    elif hand_croupier > 21:
        print("GAGNÉ")
        Victoires_joueur += 1
    elif hand_croupier < hand_joueur:
        print("GAGNÉ")
        Victoires_joueur += 1
    elif hand_croupier > hand_joueur:
        print("PERDU")
        Victoires_croupier += 1
    elif hand_croupier == hand_joueur:
        print("ÉGALITÉ")
    print(Victoire_croupier, Victoire_joueur)


def comptage():
    compte=0
    if hand=='2coeur'or'2trefle'or'2carreau'or'2pique'or'3coeur'or'3trefle'or'3carreau'or'3pique'or'4coeur'or'4trefle'or'4carreau'or'4pique'or'5coeur'or'5trefle'or'5carreau'or'5pique'or'6coeur'or'6trefle'or'6carreau'or'6pique':
        compte +=1
    elif hand=='7coeur'or'7trefle'or'7carreau'or'7pique'or'8coeur'or'8trefle'or'8carreau'or'8pique'or'9coeur'or'9trefle'or'9carreau'or'9pique':
        compte+=0
    elif hand=='10coeur'or'10trefle'or'10carreau'or'10pique'or'valetcoeur'or'valettrefle'or'valetcarreau'or'valetpique'or'damecoeur'or'dametrefle'or'damecarreau'or'damepique'or'roicoeur'or'roitrefle'or'roicarreau'or'roipique':
        compte+=-1
        


