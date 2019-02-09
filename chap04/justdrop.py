import pygame, sys, random
from pygame.locals import *
import pygame.event
import  pygame.time


class Joueur:
	def __init__(self,x,y,dx,dy,largeur,hauteur,couleur,tombe=True):
		self.x=x
		self.y=y
		self.dx=dx
		self.dy=dy
		self.largeur=largeur
		self.hauteur=hauteur
		self.couleur=couleur
		self.direction=''
		self.tombe=True
		

				
	def dessiner(self,ecran):
		pygame.draw.rect(ecran,self.couleur,self.x,self.y,hauteur,largeur)

	def deplacer_joueur(self,ecran,direction,moteur):
		
		#debug		
		print("avant déplacement : x={} y={}".format(joueur["x"],joueur["y"]))
		
		#si n'est pas en train de tomber, tenir compte de la direction
		if not(self.tombe):
			self.x+=direction*self.dx
		#si tombe, incrémenter y
		else:
			self.y-=self.dy

		#vérifier si limites écran
		if (self.x+self.largeur)>ecran.get_width():
			self.x=ecran.get_width()-self.largeur
		elif self.x <0:
			self.x=0

		#vérifier si pas bloqué par plateforme 
		#to do
		#if ecran.get_at((x,y))==(0,0,0,255):
		
					
		#si on sort de l'écran, on met fin au jeu
		if self.y<0:
			moteur.gameover()
		
		#debug							
		print("après déplacement : x={} y={}".format(joueur["x"],joueur["y"]))

'''
class Platteforme:
	def __init__(self,vitesse,couleur):
		self.vitesse=vitesse
		self.couleur=couleur

	def deplacer_platteformes():
	for idx,platteforme in enumerate(platteformes):
		platteforme["pos"][1]-=vitessePlatteforme
		if platteforme["pos"][0]<-10:
			platteformes.pop(idx)

	def dessiner_platteformes():
		for platteforme in platteformes:
			pygame.draw.rect(ecran,couleurPlatteforme,(platteforme["pos"][0],\
			platteforme["pos"][1],hauteurEcran,10))
			pygame.draw.rect(ecran,(0,0,0),(platteforme["trou"],\
			platteforme["pos"][1],40,10))

	def creer_platteforme():
            global tempsDernierePlatteforme,delaiPlatteforme
            
            platteformeY=hauteurEcran
            positionTrou=random.randint(0,hauteurEcran-40)

            platteformes.append({"pos":[0,platteformeY],"trou":positionTrou})

            tempsDernierPlatteforme=pygame.time.get_ticks()

'''

class MoteurJeu:
    
    def __init__(self,largeurEcran,hauteurEcran):
        self.largeurEcran=largeurEcran
        self.hauteurEcran=hauteurEcran
        self.ecran=None
        self.joueur=None
        self.platteformes=[]
        self.temps_demarrage=0
        self.temps_precedent=0
        self.continuerJeu=True

        
    def initialisation_jeu(self):
        pygame.init()
        self.ecran=pygame.display.set_mode((self.largeurEcran,self.hauteurEcran))
        pygame.display.set_caption("Justdrop !")
        self.joueur=Joueur(x=self.largeurEcran/2,y=self.hauteurEcran/2,dx=1,dy=1,\
                     largeur=25,hauteur=40,couleur=(255,0,0),tombe=True)

            

    def demarrerJeu(self):
        joueur["x"]=hauteurEcran/2
        joueur["y"]=0
        self.temps_demarrage=pygame.time.get_ticks()
        


    def quitterJeu(self):
        pygame.quit()
        sys.exit()


    def boucle_principale(self):

        while self.continuerJeu:
                
            self.ecran.fill((0,0,0))

            for event in pygame.event.get():
            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction='g'
                        print('move : g')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction='d'
                        print('move : d')
                    if event.key==pygame.K_ESCAPE:
                        quitterJeu()

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction=''
                        print('move : -')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction=''
                        print('move : -')
                            
                if event.type==pygame.QUIT:
                    self.quitterJeu()

            '''
            if jeuDemarre:
                    
                temps=pygame.time.get_ticks()-temps_precedent
                
                deplacer_platteformes()
                dessiner_platteformes()
                deplacer_joueur()
                dessiner_joueur()
            '''
            
            '''
            to do : control fps       
            temps=pygame.time.get_ticks()				
            if temps-tempsDernierePlatteforme>delaiPlatteforme:
                pass
            '''
            
            pygame.display.update()



#démarrage du module

if __name__=="__main__":
    largeurEcran=800
    hauteurEcran=600
    monMoteurJeu=MoteurJeu(800,600)        
    monMoteurJeu.initialisation_jeu()
    monMoteurJeu.boucle_principale()






			

	



