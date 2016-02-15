# nombre = valeurs que peuvent prendre une carte
nombre = [1,2,3,4,5,6,7,8,9,10,11]
#valeur = {'ascoeur':1,'2coeur':2,'3coeur':3,'4coeur':4,'5coeur':5,'6coeur':6,'7coeur':7,'8coeur':8,'9coeur':9,'10coeur':10,'valetcoeur':10,'damecoeur':10,'roicoeur':10,'ascarreau':1,'2carreau':2,'3carreau':3,'4carreau':4,'5carreau':5,'6carreau':6,'7carreau':7,'8carreau':8,'9carreau':9,'10carreau':10,'valetcarreau':10,'damecarreau':10,'roicarreau':10,'astrefle':1,'2trefle':2,'3trefle':3,'4trefle':4,'5trefle':5,'6trefle':6,'7trefle':7,'8trefle':8,'9trefle':9,'10trefle':10,'valettrefle':10,'dametrefle':10,'roitrefle':10,'aspique':1,'2pique':2,'3pique':3,'4pique':4,'5pique':5,'6pique':6,'7pique':7,'8pique':8,'9pique':9,'10pique':10,'valetpique':10,'damepique':10,'roipique':10}
# deck = ensemble de cartes du jeu
# _RC_ 20160214 expliquer différences entre deck et DECK
# _RC_ 20160214 il vaut mieux changer de nom que de différencier seulement sur la casse
DECK = ['ascoeur','2coeur','3coeur','4coeur','5coeur','6coeur','7coeur','8coeur','9coeur','10coeur','valetcoeur','damecoeur','roicoeur','ascarreau','2carreau','3carreau','4carreau','5carreau','6carreau','7carreau','8carreau','9carreau','10carreau','valetcarreau','damecarreau','roicarreau','astrefle','2trefle','3trefle','4trefle','5trefle','6trefle','7trefle','8trefle','9trefle','10trefle','valettrefle','dametrefle','roitrefle','aspique','2pique','3pique','4pique','5pique','6pique','7pique','8pique','9pique','10pique','valetpique','damepique','roipique']
deck = list(DECK)
#famille = ('coeur', 'trefle', 'pique', 'carreau')
#carte = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
#valeur = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
#from random import choice as rc
#import sys
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
        print("Flambé")
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

