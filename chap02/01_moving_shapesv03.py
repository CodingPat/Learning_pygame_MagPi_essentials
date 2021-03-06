import pygame, sys, random
from pygame.locals import *
import pygame.event

#initialisation de pygame
pygame.init()

#déterminer la mesure de la fenêtre
fenetreLargeur=800
fenetreHauteur=600

#valeurs RGB pour la couleur
ROUGE=(255,0,0)
VERT=(0,255,0)
BLEU=(0,0,255)

#définir variable couleur
couleur=(255,255,255)

#dimension et coordonnées d'un carré placé au milieu de l'écran
carre_cote=20
carre_x=fenetreLargeur/2-carre_cote/2
carre_y	=fenetreHauteur/2-carre_cote/2

#initialiser la direction de départ de manière aléatoire
dir_x=random.choice([-1,1])
dir_y=random.choice([-1,1])

#créer la fenêtre
fenetre=pygame.display.set_mode((fenetreLargeur,fenetreHauteur))
# donner un titre à la fenêtre
pygame.display.set_caption("Faire bouger des formes !")

def couleur_aleatoire():
	rouge=random.randint(0,255)
	vert=random.randint(0,255)
	bleu=random.randint(0,255)

	return (rouge,vert,bleu)


couleur=couleur_aleatoire()

while True:
	#tout effacer en remplissant l'écran de noir
	#fenetre.fill((0,0,0)) 
	
	#dessiner un rectangle avec des coordonnées aléatoire
	pygame.draw.rect(fenetre,couleur,(carre_x,carre_y,carre_cote,carre_cote))
	
	#déplacer le carré
	carre_x+=dir_x
	carre_y+=dir_y

	

	#vérifie si le carré ne sort pas de la fenêtre
	if (carre_x+carre_cote > fenetreLargeur):
		#replacer le carré dans la fenêtre
		carre_x=fenetreLargeur-carre_cote
		#si la coordonnée x sort de la fenêtre, on inverse la direction x
		dir_x=-dir_x
		#pour introduire un peu de variation, la direction y est changée aléatoirement
		dir_y=random.choice([dir_y,-dir_y])
		#changer la couleur de manière aléatoire
		couleur=couleur_aleatoire()
		continue

	elif (carre_x < 0):
		#replacer le carré dans la fenêtre
		carre_x=0
		#si la coordonnée x sort de la fenêtre, on inverse la direction x
		dir_x=-dir_x
		#pour introduire un peu de variation, la direction y est changée aléatoirement
		dir_y=random.choice([dir_y,-dir_y])
		#changer la couleur de manière aléatoire
		couleur=couleur_aleatoire()
		continue

		
	if (carre_y+carre_cote > fenetreHauteur):
		#replacer le carré dans la fenêtre
		carre_y=fenetreHauteur-carre_cote
		#si la coordonnée y sort de la fenêtre, on inverse la direction y
		dir_y=-dir_y
		#pour introduire un peu de variation, la direction x est changée aléatoirement
		dir_y=random.choice([dir_y,-dir_y])
		#changer la couleur de manière aléatoire
		couleur=couleur_aleatoire()
		continue

	elif (carre_y < 0):
		#replacer le carré dans la fenêtre
		carre_y=0
		#si la coordonnée y sort de la fenêtre, on inverse la direction y
		dir_y=-dir_y
		#pour introduire un peu de variation, la direction x est changée aléatoirement
		dir_y=random.choice([dir_y,-dir_y])
		#changer la couleur de manière aléatoire
		couleur=couleur_aleatoire()
		continue


	
	#vérifier la file des événements
	for event in pygame.event.get():
		if event.type==QUIT:
		# si la fenêtre a été fermée, arrêté pygame et terminer le programme
			pygame.exit()
			sys.exit()
	
	#afficher l'écran
	pygame.display.update()	

