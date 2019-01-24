import pygame, sys, random
from pygame.locals import *
import pygame.event
import  pygame.time

pygame.init()

title_image=pygame.image.load("images/title_screen.png")
gameover_image=pygame.image.load("images/gameover.png")

largeurEcran=800
hauteurEcran=600

ecran=pygame.display.set_mode((largeurEcran,hauteurEcran))

pygame.display.set_caption("Traversez les platteformes pour ne pas vous faire écraser au plafond !")

gauche=False
droite=False

jeuDemarre=False
jeuTermine=False
moment_demarrage=0

platteformes=[]
vitesse_platteformes=3
delai_platteforme=2000
temps_derniere_platteforme=0
platteformes_traversees=-1

chute=False

temps_precedent=0
temps=0

joueur={
"x":largeurEcran/2,
"y":0,
"longueur":10,
"largeur":25,
"vitessey":5,
"couleur":(255,0,0)
}

def dessiner_joueur():
	pygame.draw.rect(ecran,joueur["couleur"],(joueur["x"],joueur["y"],joueur["longueur"],\
	joueur["largeur"]))


def deplacer_joueur():
	pass

def creer_platteforme():
	pass

def deplacer_platteformes():
	pass

def dessiner_platteformes():
	pass

def gameover():
	pass

def redemarrerJeu():
	global platteformes,joueur,momentDemarrage,platteformesTraversees,delaiPlatteforme
	platteformes=[]
	joueur["x"]=largeurEcran/2
	joueur["y"]=0
	moment_demarrage=pygame.time.get_ticks()
	platteformesTraversees=-1
	delaiPlatteforme=2000


def quitterJeu():
	pygame.quit()
	sys.exit()


#boucle principale

while True:
	
	ecran.fill((0,0,0))

	for event in pygame.event.get():
	
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				gauche=True
			if event.key==pygame.K_RIGHT:
				droite=True
			if event.key==pygame.K_ESCAPE:
				quitterJeu()

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT:
				gauche=False
			if event.key==pygame.K_RIGHT:
				droite=False
			if event.key==pygame.K_SPACE:
				print("barre espace relâchée")
				if jeuDemarre==False:
					redemarrerJeu()
					jeuDemarre=True

		if event.type==QUIT:
			quitterJeu()


	if jeuDemarre:
		
		temps=pygame.time.get_ticks()-temps_precedent
		
		deplacer_platteformes()
		dessiner_platteformes()
		deplacer_joueur()
		dessiner_joueur()
						
	elif jeuTermine:
		ecran.blit(gameover_image,(0,0))

	else:
		ecran.blit(title_image,(0,0))

			
	temps=pygame.time.get_ticks()				
	if temps-temps_derniere_platteforme>delai_platteforme:
		creer_platteforme()
		temps_derniere_platteforme=temps

	pygame.display.update()


			

	



