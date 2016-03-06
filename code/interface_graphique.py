from tkinter import *
from tkinter.filedialog import *
x=1
y=0
fenetre = Tk()  #fenetre principale


champ_label = Label(fenetre, text="Jeu de Blackjack")
champ_label.pack()

cadre = Frame(fenetre, width=1, height=1, borderwidth=2, bg="#1D702D")#cadre ou il y aura les scores et les cartes
cadre.pack(fill=BOTH)

message1 = Label(cadre, text="Votre score : "+str(y), fg="white", bg="#1D702D")#Scores
message1.pack(side="top", fill=X)
message2 = Label(cadre, text="Score du croupier : "+str(x), fg="white", bg="#1D702D")
message2.pack(side="top", fill=X)

#filepath = askopenfilename(title="Ouvrir une image",filetypes=[('gif files','.gif'),('all files','.*')])#affiche une carte
#photo = PhotoImage(file=filepath)                                                                   #a partir d'un dossier
#canvas = Canvas(cadre, width=photo.width(), height=photo.height(), bg="#1D702D")
#canvas.create_image(0, 0, anchor=NW, image=photo)
#canvas.pack()
canvas = Canvas(width = 400, height = 400, bg = "#1D702D")
canvas.pack(fill=BOTH)

gif1 = PhotoImage(file = "..\\cartes\\4_coeur.gif")
canvas.create_image(50, 50, image = gif1, anchor = NW)

bouton_rejouer = Button(cadre, text="Rejouer")
bouton_rejouer.pack()

bouton_quitter = Button(fenetre, text="Quitter", command = fenetre.destroy)
bouton_quitter.pack(side = RIGHT, padx = 0, pady = 0)

fenetre.mainloop()

