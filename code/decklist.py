DECK = {'ascoeur':11,'2coeur':2,'3coeur':3,'4coeur':4,'5coeur':5,'6coeur':6,'7coeur':7,'8coeur':8,'9coeur':9,'10coeur':10,'valetcoeur':10,'damecoeur':10,'roicoeur':10,'ascarreau':11,'2carreau':2,'3carreau':3,'4carreau':4,'5carreau':5,'6carreau':6,'7carreau':7,'8carreau':8,'9carreau':9,'10carreau':10,'valetcarreau':10,'damecarreau':10,'roicarreau':10,'astrefle':11,'2trefle':2,'3trefle':3,'4trefle':4,'5trefle':5,'6trefle':6,'7trefle':7,'8trefle':8,'9trefle':9,'10trefle':10,'valettrefle':10,'dametrefle':10,'roitrefle':10,'aspique':11,'2pique':2,'3pique':3,'4pique':4,'5pique':5,'6pique':6,'7pique':7,'8pique':8,'9pique':9,'10pique':10,'valetpique':10,'damepique':10,'roipique':10}
# deck = ensemble de cartes du jeu
# _RC_ 20160214 expliquer différences entre deck et DECK
# _RC_ 20160214 il vaut mieux changer de nom que de différencier seulement sur la casse
deck = list(DECK) #DECK est un dictionnaire, il faut donc le transformer en liste pour ne garder que les cartes dans deck

import random
import math
#import tkinter

random.shuffle(deck) #Mélange le deck


#Fonction qui tire un nombre de cartes donné.
#En pratique, on tire une ou 2 cartes à la fois.
def tirer(hand,x):
    if x > len(deck): #vérifier que le deck n'est pas vide
        print("Pas assez de cartes.")
        # alors, remélanger les cartes
        # _RC_ le deck est vide, donc ça ne sert à rien de le mélanger, il faut commencer par **mettre** des cartes dedans
        random.shuffle(deck)
    for i in range(x):
        # ne pas utiliser '=', sinon, ne modifie pas la variable passée en paramètre
        hand.append( deck.pop(0) )

#Fonction qui compte la valeur totale de la main
def total(hand):
    t     = 0
    nbrAS = 0
    nbrCartes = len(hand)
    for i in range(nbrCartes):
        carte  = hand[ i ]
        valeur = DECK.get(carte)
        if valeur == 11:#Compte le nombre d'as dans la main
            nbrAS += 1
        t      = t + valeur
    while nbrAS>0 and t>21:
        t     -= 10
        nbrAS -= 1
    return t

def croupier(hand_croupier):
    #Le croupier a déjà une ou plusieurs cartes
    while total(hand_croupier) < 17: #Le croupier tire jusqu'a 17 et s'arrete au dessus
        tirer(hand_croupier,1)
        print(hand_croupier)
    print("Score du croupier : " + str(total(hand_croupier)) )

def joueur(hand_joueur):
    x=input("Voulez vous une autre carte ?\nSi oui, tapez h, sinon tapez sur Entrée:")
    while x == "h":
        tirer(hand_joueur,1)
        print("Votre score : " + str(total(hand_joueur)) )
        print(hand_joueur)
        if total(hand_joueur) >= 21:
            break
        x=input("Voulez vous une autre carte ?\nSi oui, tapez h, sinon tapez sur Entrée:")

Victoires_joueur   = 0
Victoires_croupier = 0

#Fonction qui compare le score de chaque joueur et affiche le nombre de victoires
# _RC_ a et b sont des références
# à la sortie de la fonction, Victoires_croupier et Victoires_joueur font toujours référence à leurs valeurs initiales
# il faut donc passer des objets "mutables"
# 3 solutions
# - créer une classe représentant un joueur (croupier ou joueur), avec des attributs comme la main, le score, le nom, etc.
# - utiliser une liste de scores (par ex: premier élément pour le croupier et deuxième élément pour le joueur)
# - faire en sorte que gagnant retourne deux valeurs (Victoires_croupier, Victoires_joueur = gagnant( x, y )
def gagnant(x,y,a,b):
    #x est le total de la main du joueur
    #y est le total de la main du croupier
    #a est le nbr de victoires du joueur
    #b est le nbr de victoires du croupier
    if y == 21:
        print("Blackjack du croupier")
        print("PERDU")
        b = 1+b
    elif x == 21:
        print("Blackjack !")
        print("GAGNÉ")
        a = 1+a
    elif x > 21: # _RC_ que se passe-t-il si le joueur ET le croupier font plus de 21 ? Ici, c'est le joueur qui perd en premier
        print("Flambé")
        print("PERDU")
        b = 1+b
    elif y > 21:
        print("GAGNÉ")
        a = 1+a
    elif y < x:
        print("GAGNÉ")
        a = 1+a
    elif y > x:
        print("PERDU")
        b = 1+b
    elif y == x:
        print("ÉGALITÉ")
    print("Victoire du croupier :"+ str(b),"\nVictoires du joueur :" + str(a))

#Fonction qui compte les cartes pour "prédire" s'il faut tirer ou pas
def comptage():# FINIR !!!
    compte=0
    if hand=='2coeur'or'2trefle'or'2carreau'or'2pique'or'3coeur'or'3trefle'or'3carreau'or'3pique'or'4coeur'or'4trefle'or'4carreau'or'4pique'or'5coeur'or'5trefle'or'5carreau'or'5pique'or'6coeur'or'6trefle'or'6carreau'or'6pique':
        compte += 1
    elif hand=='7coeur'or'7trefle'or'7carreau'or'7pique'or'8coeur'or'8trefle'or'8carreau'or'8pique'or'9coeur'or'9trefle'or'9carreau'or'9pique':
        compte = compte
    elif hand=='10coeur'or'10trefle'or'10carreau'or'10pique'or'valetcoeur'or'valettrefle'or'valetcarreau'or'valetpique'or'damecoeur'or'dametrefle'or'damecarreau'or'damepique'or'roicoeur'or'roitrefle'or'roicarreau'or'roipique'or'ascoeur'or'aspique'or'ascarreau'or'astrefle':
        compte -= 1

#Programme principal
#print(deck)
#Problème 1 : lorqsu'il n'y a plus de de cartes, le programme bugge.
#Problème 2 : le compteur de victoires ne marche pas.

r="r"
while r=="r":
    #Initialiser les mains
    hand_joueur   = []
    hand_croupier = []
    #Tirer une carte pour le croupier
    tirer(hand_croupier,1)
    print("main croupier  = ", hand_croupier)
    print("score croupier = ", total(hand_croupier))
    #Tirer deux cartes pour le joueur
    tirer(hand_joueur,2)
    print("main joueur  = ", hand_joueur)
    print("score joueur = ", total(hand_joueur))
    #Le joueur joue
    joueur(hand_joueur)
    #Le croupier joue
    croupier(hand_croupier)
    #Comparaison des scores
    gagnant( total(hand_joueur), total(hand_croupier), Victoires_croupier, Victoires_joueur )
    #Question pour rejouer ou quitter
    r=input("Voulez vous rejouer ?\nSi oui, tapez r, sinon tapez sur entrer:")

print("Merci d'avoir joué.\nAu revoir")

