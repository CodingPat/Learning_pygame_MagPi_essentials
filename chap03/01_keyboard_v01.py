import pygame,sys
from pygame.locals import *
import pygame.event

#initialisation pygame
pygame.init()

#dimension fenêtre
largeurEcran=800
hauteurEcran=600

#créer fenêtre
ecran=pygame.display.set_mode((largeurEcran,hauteurEcran))
pygame.display.set_caption("Pygame test clavier")

#variables carré
#taille côté
tailleJoueur=20
#couleur
couleur=(255,0,0)
#position de départ X joueur
joueurX=(largeurEcran/2)-(tailleJoueur/2)
#position de départ Y joueur
joueurY=(hauteurEcran/2)-(tailleJoueur/2)
#deplacement X
deplacementX=1.0
#deplacement Y
deplacementY=1.0

#variables clavier
gauche=False
droite=False
haut=False
bas=False


def deplacer():
	"mise à jour du déplacement"
	global joueurX,joueurY,deplacementX,deplacementY
	
	#déplacement à gauche
	if gauche:
		joueurX-=deplacementX
		#si nouvelle coordonnée X sort à gauche de l'écran, réinitialiser à zéro
		if joueurX<0:	
			joueurX=0
		
	#déplacement à droite
	if droite:
		#se déplacer à droite
		joueurX+=deplacementX
		# vérifier qu'on ne sort pas à droite de l'écran 
		if joueurX+tailleJoueur>largeurEcran:
			joueurX=largeurEcran-tailleJoueur

	#déplacement vers le bas
	if bas:
		#se déplacer vers le bas
		joueurY+=deplacementY
		# vérifier qu'on ne sort pas en bas de l'écran 
		if joueurY+tailleJoueur>hauteurEcran:
			joueurY=hauteurEcran-tailleJoueur

	#déplacement vers le haut
	if haut:
		#se déplacer vers le haut
		joueurY-=deplacementY
		# vérifier qu'on ne sort pas en haut de l'écran 
		if joueurY<0:
			joueurY=0

	
	
	

def quitterJeu():
	"quitter le jeu"
	pygame.quit()
	sys.exit()


#boucle principale
while True:
	#effacer écran
	ecran.fill((0,0,0))

	#dessiner joueur
	pygame.draw.rect(ecran,couleur,(joueurX,joueurY,tailleJoueur,tailleJoueur))

	#traiter les événements
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				droite=True
			if event.key==pygame.K_LEFT:
				gauche=True
			if event.key==pygame.K_UP:
				haut=True
			if event.key==pygame.K_DOWN:
				bas=True
			if event.key==pygame.K_ESCAPE:
				quitterJeu()

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				droite=False
			if event.key==pygame.K_LEFT:
				gauche=False
			if event.key==pygame.K_UP:
				haut=False
			if event.key==pygame.K_DOWN:
				bas=False
					
		
		if event.type==QUIT:
			quitterJeu()

	deplacer()

	pygame.display.update()

