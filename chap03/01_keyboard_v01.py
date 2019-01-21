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
#position X joueur
joueurX=(largeurEcran/2)-(tailleJoueur/2)
#position Y joueur
joueurY=hauteurEcran-tailleJoueur
#deplacement X
deplacementX=1.0
#deplacement Y
deplacementY=0.0
#hauteur d'un saut
hauteurSaut=25.0
#vitesse déplacement
vitesse=1.0
vitesseMaximum=10.0
#gravité
gravite=1.0

#variables clavier
gaucheBas=False
droiteBas=False
saut=False


def deplacer():
	"mise à jour du déplacement"
	global joueurX,joueurY,deplacementX,deplacementY,saut,gravite
	
	#déplacement à gauche
	if gaucheBas:
		#si on se déplace vers la droite, on réinitialise la vitesse et on inverse la direction
		if deplacementX>0:
			deplacementX=-vitesse
		#se déplacer à droite si on ne sort pas à gauche de l'écran
		if joueurX>0:
			joueurX+=deplacementX
 

	#déplacement à droite
	if droiteBas:
		#si on se déplace vers la gauche, on réinitialise la vitesse et on inverse la direction
		if deplacementX<0:
			deplacementX=vitesse
		#se déplacer à droite si on ne sort pas à gauche de l'écran
		if joueurX+tailleJoueur<largeurEcran:
			joueurX+=deplacementX
	
	#gestion du saut

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
				basDroit=True
			if event.key==pygame.K_LEFT:
				basGauche=True
			if event.key==pygame.K_ESCAPE:
				quitterJeu()

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT:
				basDroit=False
				deplacementX=vitesse
			if event.key==pygame.K_LEFT:
				basGauche=False
				deplacementX=vitesse
		
		if event.type==QUIT:
			quitterJeu()

	deplacer()

	pygame.display.update()

