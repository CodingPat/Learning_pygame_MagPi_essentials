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
pygame.display.set_caption("Pygame test clavier - raquette")

#variables carré
#taille côté
tailleJoueurX=80
tailleJoueurY=20
#couleur
couleur=(255,0,0)
#position de départ X joueur
joueurX=(largeurEcran/2)-(tailleJoueurX/2)
#position de départ Y joueur
joueurY=hauteurEcran-tailleJoueurY-10
#deplacement X
deplacementX=1.0
#deplacement Y
deplacementY=0.0
#vitesse déplacement
vitesse=1.0
vitesseMaximum=10.0

#variables clavier
gauche=False
droite=False



def deplacer():
	"mise à jour du déplacement"
	global joueurX,joueurY,deplacementX,deplacementY
	
	#déplacement à gauche
	if gauche:
		#si on se déplace vers la droite, on réinitialise la vitesse au minimum et on inverse la direction
		if deplacementX>0:
			deplacementX=-vitesse
		#se déplacer à gauche 
		joueurX+=deplacementX
		#si nouvelle coordonnée X sort à gauche de l'écran, réinitialiser à zéro
		if joueurX<0:	
			joueurX=0
			
 

	#déplacement à droite
	if droite:
		#si on se déplace vers la gauche, on réinitialise la vitesse et on inverse la direction
		if deplacementX<0:
			deplacementX=vitesse
		#se déplacer à droite 
		joueurX+=deplacementX
		# si on sort à droite de l'écran, 
		if joueurX+tailleJoueurX>largeurEcran:
			joueurX=largeurEcran-tailleJoueurX

		
	#accélération jusqu'à atteindre la vitesse maximum
	if(gauche or droite):
		if (abs(deplacementX)<abs(vitesseMaximum)):
			deplacementX*=1.005


def quitterJeu():
	"quitter le jeu"
	pygame.quit()
	sys.exit()


#boucle principale
while True:
	#effacer écran
	ecran.fill((0,0,0))

	#dessiner joueur
	pygame.draw.rect(ecran,couleur,(joueurX,joueurY,tailleJoueurX,tailleJoueurY))

	#traiter les événements
	for event in pygame.event.get():
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_RIGHT:
				droite=True
			if event.key==pygame.K_LEFT:
				gauche=True
			if event.key==pygame.K_ESCAPE:
				quitterJeu()

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				droite=False
				deplacementX=vitesse
			if event.key==pygame.K_LEFT:
				gauche=False
				deplacementX=vitesse
					
		
		if event.type==QUIT:
			quitterJeu()

	deplacer()

	pygame.display.update()

