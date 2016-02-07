# nombre = valeurs que peuvent prendre une carte
nombre = [1,2,3,4,5,6,7,8,9,10,11]
# deck = ensemble de cartes du jeu
deck = ['ascoeur','2coeur','3coeur','4coeur','5coeur','6coeur','7coeur','8coeur','9coeur','10coeur','valetcoeur','damecoeur','roicoeur','ascarreau','2carreau','3carreau','4carreau','5carreau','6carreau','7carreau','8carreau','9carreau','10carreau','valetcarreau','damecarreau','roicarreau','astrefle','2trefle','3trefle','4trefle','5trefle','6trefle','7trefle','8trefle','9trefle','10trefle','valettrefle','dametrefle','roitrefle','aspique','2pique','3pique','4pique','5pique','6pique','7pique','8pique','9pique','10pique','valetpique','damepique','roipique']
#famille = ('coeur', 'trefle', 'pique', 'carreau')
#carte = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
#valeur = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}
#from random import choice as rc
#import sys
import random
import math
random.shuffle(carte) #Mélange le deck

# _RC_ OT : ajouter description de la fonction
def tirer(x):
    # _RC_ OT : vérifier que le deck n'est pas vide
    # _RC_ OT : ne faut-il pas initialiser hand ?

    for i in range(x):
        # _RC_ OT : il me semble que le code suivant tire 2 cartes
        hand=[carte.pop(0)]
        hand=hand+[carte.pop(0)]
    return hand

# _RC_ OT : à quoi sert la ligne suivante ?
print(tirer(2))

# _RC_ OT : ajouter description de la fonction
def total(hand):
    # _RC_ OT : trouver un meilleur nom de variable
    ass=hand.count(11)
    t=sum(hand)
    while ass>0 and t>21:
        t-=10
        ass-=1
        # _RC_ OT : il me semble que le return est mal placé
        return t

def hand_du_croupier():
    hand_croupier = []
    # _RC_ OT : utiliser la fonction tirer
    hand=[carte.pop(0)]
    # _RC_ OT : if ou while ?
    if sum(nombre_hand)<17:
        hand=hand+[carte.pop(0)]
        hand_croupier.extend(carte)
    else:
            stop
    # _RC_ OT : mettez-vous d'accord sur les noms des fonctions à coder
    calculer_hand()

# _RC_ OT : Description ok mais placer les variables globales ailleurs
#Fonction qui compare le score de chaque joueur et affiche le nombre de victoires
Victoires_joueur=0
Victoires_croupier=0

def gagnant():
    # _RC_ OT : mettez-vous d'accord sur les noms des fonctions à coder
    total_hand()
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
        print("Le casino est flambé")
        print("GAGNÉ")
        Victoires_joueur += 1
    elif hand_croupier < hand_joueur:
        print("GAGNÉ")
        Victoires_joueur += 1
    elif hand_croupier > hand_joueur:
        print("PERDU")
        Victoires_croupier += 1
   # else hand_croupier == hand_joueur:
    #    print("ÉGALITÉ")
    print(Victoire_croupier, Victoire_joueur)

