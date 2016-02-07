# nombre = valeurs que peuvent prendre une carte
nombre = [1,2,3,4,5,6,7,8,9,10,11]
# deck = ensemble de cartes du jeu
deck = ['ascoeur','2coeur','3coeur','4coeur','5coeur','6coeur','7coeur','8coeur','9coeur','10coeur','valetcoeur','damecoeur','roicoeur','ascarreau','2carreau','3carreau','4carreau','5carreau','6carreau','7carreau','8carreau','9carreau','10carreau','valetcarreau','damecarreau','roicarreau','astrefle','2trefle','3trefle','4trefle','5trefle','6trefle','7trefle','8trefle','9trefle','10trefle','valettrefle','dametrefle','roitrefle','aspique','2pique','3pique','4pique','5pique','6pique','7pique','8pique','9pique','10pique','valetpique','damepique','roipique']

import random
import math

# mélanger le deck
random.shuffle(deck)

# fonction permettant de retirer la carte du haut du deck
def tirer():
    main=[]
    # vérifier que le deck n'est pas vide

    # si ok, retirer la première carte et la renvoyer
    main=[deck.pop(0)]
    return main

print( tirer )
input( "tapez n'importe quelle touche" )
for i in range(1, 55):
    carte_croupier = tirer()
    print( i, ": ", carte_croupier )

#def main_du_croupier():
#    main_croupier = []
 #   tirer(carte)
  #  if sum(nombre_main)<17:
  #      tirer(carte)
   #     main_croupier.extend(carte)
    #    else:
     #       stop
   # calculer_main()


