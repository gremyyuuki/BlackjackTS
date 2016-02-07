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


def tirer(x):
    # vérifier que le deck n'est pas vide

    for i in range(x):
        hand=[carte.pop(0)]
        hand=hand+[carte.pop(0)]
    return hand
print(tirer(2))

def total(hand):
    ass=hand.count(11)
    t=sum(hand)
    while ass>0 and t>21:
        t-=10
        ass-=1
        return t

def hand_du_croupier():
    hand_croupier = []
    hand=[carte.pop(0)]
    if sum(nombre_hand)<17:
        hand=hand+[carte.pop(0)]
        hand_croupier.extend(carte)
    else:
            stop
    calculer_hand()

#Fonction qui compare le score de chaque joueur et affiche le nombre de victoires
Victoires_joueur=0
Victoires_croupier=0

def gagnant():
    total_hand()
    if hand_croupier == 21:
        print("Blackjack du croupier")
        print("PERDU")
        Victoires_croupier +=1
    elif hand_joueur == 21:
        print("Blackjack !")
        print("GAGNÉ")
        Victoires_joueur +=1
    elif hand_joueur > 21:
        print("Flambé")
        print("PERDU")
        Victoires_croupier +=1
    elif hand_croupier > 21:
        print("Le casino est flambé")
        print("GAGNÉ")
        Victoires_joueur +=1
    elif hand_croupier < hand_joueur:
        print("GAGNÉ")
        Victoires_joueur +=1
    elif hand_croupier > hand_joueur:
        print("PERDU")
        Victoires_croupier +=1
   # else hand_croupier == hand_joueur:
    #    print("ÉGALITÉ")
    print(Victoire_croupier,Victoire_joueur)

