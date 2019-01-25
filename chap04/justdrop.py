import pygame, sys, random
from pygame.locals import *
import pygame.event
import  pygame.time

pygame.init()

title_image=pygame.image.load("images/title_screen.png")
gameover_image=pygame.image.load("images/gameover.png")

largeurEcran=800
largeurEcran=600

ecran=pygame.display.set_mode((largeurEcran,largeurEcran))

pygame.display.set_caption("Traversez les platteformes pour ne pas vous faire écraser au plafond !")

#variables globales
gauche=False
droite=False

jeuDemarre=False
jeuTermine=False
moment_demarrage=0

platteformes=[]
vitessePlatteforme=1
delaiPlatteforme=2000
tempsDernierePlatteforme=0
platteformesTraversees=-1
couleurPlatteforme=(0,0,255)

tombe=False
plafondPlatteformeTrouve=False

temps_precedent=0
temps=0

joueur={
"x":int(largeurEcran/2),
"y":0,
"longueur":10,
"largeur":25,
"vitesseY":5,
"vitesseX":5,
"couleur":(255,0,0)
}

def dessiner_joueur():
	pygame.draw.rect(ecran,joueur["couleur"],(joueur["x"],joueur["y"],joueur["longueur"],\
	joueur["largeur"]))


def deplacer_joueur():

	global platteformesTraversees,tombe

	if ecran.get_at((int(joueur["x"]),int(joueur["y"]+joueur["largeur"])))==(0,0,0,255):
		joueurSurPlatteformeGauche=False
	if ecran.get_at((int(joueur["x"]+joueur["largeur"]),int(joueur["y"]+joueur["largeur"])))==(0,0,0,255):
		joueurSurPlatteformeDroite=False

	if not(joueurSurPlatteformeGauche or joueurSurPlatteformeDroite):
	#joueur dans un trou, chute
		joueur["y"]+=joueur["vitesseY"]
		if joueur["y"]+joueur["largeur"]>largeurEcran:
			joueur["y"]=largeurEcran-joueur["largeur"]

		if not(tombe):
			tombe=True
			platteformesTraversees+=1
	else:
	#joueur sur platteforme, le positionner au-dessus de la platteforme
		plafondPlatteformeTrouve=False
		tombe=False
		#décrémenter y jusqu'à ce que l'on retombe sur une couleur d'arrière-plan
		#ou que l'on sorte de l'écran		
		while (not(plafondPlatteformeTrouve) and joueur["y"]>0):
			player["y"]-=1
			if ecran.get_at((int(joueur["x"]),int(joueur["y"]+joueur["largeur"])))==(0,0,0,255):
				plafondPlatteformeTrouve=True
		#si on sort de l'écran, on met fin au jeu
		if joueur["y"]<0:
			gameover()
		
									
	if gauche:
		joueur["x"]-=joueur["vitesseX"]
		if joueur["x"]<0:
			joueur["x"]=0

	if droite:
		joueur["x"]+=joueur["vitesseX"]
		if joueur["x"]>largeurEcran:
			joueur["x"]=largeurEcran-joueur["longueur"]


def creer_platteforme():
	global tempsDernierePlatteforme,delaiPlatteforme
	
	platteformeY=largeurEcran
	positionTrou=random.randint(0,largeurEcran-40)

	platteformes.append({"pos":[0,platteformeY],"trou":positionTrou})

	tempsDernierPlatteforme=pygame.time.get_ticks()

	

def deplacer_platteformes():
	for idx,platteforme in enumerate(platteformes):
		platteforme["pos"][1]-=vitessePlatteforme
		if platteforme["pos"][0]<-10:
			platteformes.pop(idx)

def dessiner_platteformes():
	for platteforme in platteformes:
		pygame.draw.rect(ecran,couleurPlatteforme,(platteforme["pos"][0],\
		platteforme["pos"][1],largeurEcran,10))
		pygame.draw.rect(ecran,(0,0,0),(platteforme["trou"],\
		platteforme["pos"][1],40,10))


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
	if temps-tempsDernierePlatteforme>delaiPlatteforme:
		creer_platteforme()
		tempsDernierePlatteforme=temps

	pygame.display.update()


			

	



