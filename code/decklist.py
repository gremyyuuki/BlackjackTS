dictDECK = {'as_coeur':11,'2_coeur':2,'3_coeur':3,'4_coeur':4,'5_coeur':5,'6_coeur':6,'7_coeur':7,'8_coeur':8,'9_coeur':9,'10_coeur':10,'valet_coeur':10,'dame_coeur':10,'roi_coeur':10,'as_carreau':11,'2_carreau':2,'3_carreau':3,'4_carreau':4,'5_carreau':5,'6_carreau':6,'7_carreau':7,'8_carreau':8,'9_carreau':9,'10_carreau':10,'valet_carreau':10,'dame_carreau':10,'roi_carreau':10,'as_trefle':11,'2_trefle':2,'3_trefle':3,'4_trefle':4,'5_trefle':5,'6_trefle':6,'7_trefle':7,'8_trefle':8,'9_trefle':9,'10_trefle':10,'valet_trefle':10,'dame_trefle':10,'roi_trefle':10,'as_pique':11,'2_pique':2,'3_pique':3,'4_pique':4,'5_pique':5,'6_pique':6,'7_pique':7,'8_pique':8,'9_pique':9,'10_pique':10,'valet_pique':10,'dame_pique':10,'roi_pique':10}
# deck = ensemble de cartes du jeu
# dictDECK est le dictionnaire qui permet d'attribuer une valeur aux cartes
deck = list(dictDECK) #dictDECK est un dictionnaire
                      #il faut donc le transformer en liste pour ne garder que les cartes dans deck

import random
import math
#import tkinter

random.shuffle(deck) #Mélange le deck

#Compte les cartes pour "prédire" s'il faut tirer ou pas
Compte = 0

#Fonction qui tire un nombre de cartes donné.
#En pratique, on tire une ou 2 cartes à la fois.
def tirer(hand,x,c):
    if x > len(deck): #vérifier que le deck n'est pas vide
        print("Pas assez de cartes.")
        recharge = list(dictDECK)
        random.shuffle(recharge)# alors, mélanger la recharge
        deck.extend(recharge)
    for i in range(x):
        # ne pas utiliser '=', sinon, ne modifie pas la variable passée en paramètre
        carte = ( deck.pop(0) )
        valeur = dictDECK.get(carte)#compte les cartes pour prédire s'il faut piocher ou pas
        if 2 <= valeur <= 6:
          c +=1
        elif valeur <= 10:
          c -=1
        hand.append(carte)
    print("Le compte est à "+str(c))

#Fonction qui compte la valeur totale de la main
def total(hand):
    t     = 0
    nbrAS = 0
    nbrCartes = len(hand)
    for i in range(nbrCartes):
        carte  = hand[ i ]
        valeur = dictDECK.get(carte)
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
    while total(hand_joueur) < 21:
        x=input("Voulez vous une autre carte ?\nSi oui, tapez h, sinon tapez sur Entrée:")
        if x == "h":
            tirer(hand_joueur,1)
            print("Votre score : " + str(total(hand_joueur)) )
            print(hand_joueur)
        else:
            break

#Comptabilise le nombre de victoires du joueur et du croupier.
Scores = [0,0]

#Fonction qui compare le score de chaque joueur et affiche le nombre de victoires
def gagnant(x,y,s):
    #x est le total de la main du joueur
    #y est le total de la main du croupier
    #s est une liste de scores dont le premier élément est le nombre de victoires du joueur et le second celui du croupier
    if y > 21:
        if x > 21:
            print("ÉGALITÉ")
        else:
            print("GAGNÉ")
            s[0] += 1
    else:
        if x > 21:
            print("PERDU")
            s[1] += 1
        else:
            if y > x:
                print("PERDU")
                s[1] += 1
            else:
                if x == y:
                    print("ÉGALITÉ")
                else:
                    print("GAGNÉ")
                    s[0] += 1

    print("Victoire du joueur :"+ str(s[0]),"\nVictoires du croupier :" + str(s[1]))

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
#Problème: pas d'affichage de "BLACKJACK" dans gagnant()

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
    gagnant( total(hand_joueur), total(hand_croupier), Scores )
    #Question pour rejouer ou quitter
    r=input("Voulez vous rejouer ?\nSi oui, tapez r, sinon tapez sur Entrée:")

print("Merci d'avoir joué.\nAu revoir")

