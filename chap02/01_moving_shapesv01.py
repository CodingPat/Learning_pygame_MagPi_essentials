import pygame, sys, random
from pygame.locals import *
import pygame.event

#initialisation de pygame
pygame.init()

#déterminer la mesure de la fenêtre
fenetreLargeur=800
fenetreHauteur=600

#créer la fenêtre
fenetre=pygame.display.set_mode((fenetreLargeur,fenetreHauteur))
# donner un titre à la fenêtre
pygame.display.set_caption("Faire bouger des formes !")

while True:
	#tout effacer en remplissant l'écran de noir
	fenetre.fill((0,0,0)) 
	#dessiner un rectangle avec des coordonnées aléatoire
	pygame.draw.rect(fenetre,(255,0,0),(random.randint(0,fenetreLargeur),random.randint(0,fenetreHauteur),20,20))
	
	#vérifier la file des événements
	for event in pygame.event.get():
		if event.type==QUIT:
		# si la fenêtre a été fermée, arrêté pygame et terminer le programme
			pygame.exit()
			sys.exit()
	
	#afficher l'écran
	pygame.display.update()	

