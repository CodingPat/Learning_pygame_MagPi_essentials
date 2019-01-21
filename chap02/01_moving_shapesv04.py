import pygame, sys, random
from pygame.locals import *
import pygame.event


#faire varier la série aléatoire
random.seed()
 
#initialisation de pygame
pygame.init()

#déterminer la mesure de la fenêtre
fenetreLargeur=800
fenetreHauteur=600

#définir variable couleur
couleur=(255,255,255)

#dimension et coordonnées d'un carré placé au milieu de l'écran
carre_cote=20
carre_x=fenetreLargeur/2-carre_cote/2
carre_y	=fenetreHauteur/2-carre_cote/2

#définir variables direction
dir_x=0
dir_y=0

#définir variables accélération
v_x=0
v_y=0


#créer la fenêtre
fenetre=pygame.display.set_mode((fenetreLargeur,fenetreHauteur))
# donner un titre à la fenêtre
pygame.display.set_caption("Faire bouger des formes !")

def direction_aleatoire():
	dir_x=random.choice([-1,1])
	dir_y=random.choice([-1,1])
	return dir_x,dir_y
	

def acceleration_aleatoire():
	v_x=random.choice([0.1,0.3,0.5,0.7])
	v_y=random.choice([0.1,0.3,0.5,0.7])
	return v_x,v_y

def couleur_aleatoire():
	rouge=random.randint(0,255)
	vert=random.randint(0,255)
	bleu=random.randint(0,255)

	return (rouge,vert,bleu)


couleur=couleur_aleatoire()
dir_x,dir_y=direction_aleatoire()
v_x,v_y=acceleration_aleatoire()
#l'accélération doit aller dans le même sens que la direction
if dir_x>0:
	v_x=abs(v_x)
else:
	v_x=-v_x
if dir_y>0:
	v_y=abs(v_y)
else:
	v_y=-v_y



while True:
	#tout effacer en remplissant l'écran de noir
	#fenetre.fill((0,0,0)) 
	
	#dessiner un rectangle avec des coordonnées aléatoire
	pygame.draw.rect(fenetre,couleur,(carre_x,carre_y,carre_cote,carre_cote))
	
	#déplacer le carré
	carre_x+=dir_x
	carre_y+=dir_y
	#accélérer le déplacement pour la prochaine fois
	dir_x+=v_x
	dir_y+=v_y

	#vérifie si le carré ne sort pas de la fenêtre
	if (carre_x+carre_cote > fenetreLargeur):
		#replacer le carré dans la fenêtre		
		carre_x=fenetreLargeur-carre_cote
		#inverser la direction x		
		dir_x=-1
		#pour plus de variations, la direction y est redéterminée aléatoirement
		valeur_inutile,dir_y=direction_aleatoire()
		#les accélérations sont redéterminées aléatoirement
		v_x,v_y=acceleration_aleatoire()
		#v_x doit suivre dir_x (négatif)
		v_x=-v_x
		#couleur refixée aléatoirement
		couleur=couleur_aleatoire()
		continue 

	elif (carre_x<0):
		carre_x=0		
		dir_x=1
		valeur_inutile,dir_y=direction_aleatoire()
		v_x,v_y=acceleration_aleatoire()
		couleur=couleur_aleatoire() 
	
		continue

			
	if (carre_y+carre_cote > fenetreHauteur):
		carre_y=fenetreHauteur-carre_cote	
		dir_y=-1
		dir_x,valeur_inutile=direction_aleatoire()
		v_x,v_y=acceleration_aleatoire()
		v_y=-v_y
		couleur=couleur_aleatoire()
		

		continue
	elif (carre_y<0):
		carre_y=0		
		dir_y=1
		dir_x,valeur_inutile=direction_aleatoire()
		v_x,v_y=acceleration_aleatoire()
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

