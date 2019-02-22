import pygame, sys, random
from pygame.locals import *
import pygame.event
import  pygame.time


class Joueur:
    def __init__(self,x,y,dx,dy,largeur,hauteur,couleur,moteur,tombe=False):
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.largeur=largeur
        self.hauteur=hauteur
        self.couleur=couleur
        self.moteur=moteur
        self.direction=0
        self.tombe=tombe
                
    def dessiner(self):
        pygame.draw.rect(ecran,self.couleur,(self.x,self.y,self.largeur,self.hauteur))

    def deplacer(self):
                
        #debug      
        #print("avant déplacement : x={} y={}".format(self.x,self.y))
        
        #vérifier si sur une platteforme, sinon tombe
        
        
        #debug
        #print("avant check color : x={} y={}".format(self.x,self.y))
    
        #avant de vérifier couleur en-dessous du joueur, vérifier que l'on n'a pas atteint le fond de l'écran
        if self.y+self.hauteur<hauteurEcran:
            
            if (ecran.get_at((self.x,self.y+self.hauteur))==(0,0,0,255) and ecran.get_at((self.x+self.largeur,self.y+self.hauteur))==(0,0,0,255)):
                self.tombe=True
            else :
                self.tombe=False
                #se positionner sur le dessus de la platteforme
                try:
                    while (ecran.get_at((self.x,self.y+self.hauteur-1))==couleurPlatteforme or ecran.get_at((self.x+self.largeur-1,self.y+self.hauteur-1))==couleurPlatteforme):
                        self.y=self.y-1
                except IndexError:
                    print("{},{}".format(self.x,self.y))
                       
        
        
        #si n'est pas en train de tomber, tenir compte de la direction
               
        if not(self.tombe):
            self.x+=self.direction*self.dx
        #si tombe, incrémenter y
        else:
            self.y+=self.dy
        
        #si on sort de l'écran, on met fin au jeu
        if self.y<0:
            moteur.gameover()
            
        if self.y+self.hauteur > hauteurEcran:
            self.y=hauteurEcran-self.hauteur
            self.tombe=False
    
        #vérifier si limites écran
        if (self.x+self.largeur)>largeurEcran:
            self.x=largeurEcran-self.largeur
        elif self.x <0:
            self.x=0

                                    
        
        #debug                          
        #print("après déplacement : x={} y={}".format(self.x,self.y))


class Platteforme:
    #variables de classe
    dernierePlatteformeA=0
    delaiPlatteforme=5
    
    def __init__(self,x,y,vitesse,couleur,moteur):
        self.vitesse=vitesse
        self.couleur=couleur
        self.x=x
        self.y=y
        self.hauteur=10
        self.positionTrou=0
        self.moteur=moteur
        self.creer_platteforme()
        

               
    def dessiner(self):
        
            
        pygame.draw.rect(ecran,self.couleur,(self.x,\
            self.y,largeurEcran,self.hauteur))
        
        pygame.draw.rect(ecran,(0,0,0),(self.positionTrou,\
            self.y,40,self.hauteur))

    def creer_platteforme(self):
                       
        self.positionTrou=random.randint(0,hauteurEcran-40)

        Platteforme.dernierePlatteformeA=pygame.time.get_ticks()



class MoteurJeu:
    
    def __init__(self):
        #self.largeurEcran=largeurEcran
        #self.hauteurEcran=hauteurEcran
        #self.ecran=None
        self.joueur=None
        self.platteformes=[]
        self.continuerJeu=True
        self.demarrageA=0
        self.derniereMAJEcranA=0
        self.dernierePlatteformeA=0

        
    def initialisation_jeu(self):
        self.joueur=Joueur(x=int(largeurEcran/2),y=int(hauteurEcran/2),dx=5,dy=5,\
                     largeur=25,hauteur=40,couleur=(255,0,0),moteur=self,tombe=False)
        platteforme=Platteforme(vitesse=2,x=0,y=int(hauteurEcran*2/3),couleur=couleurPlatteforme,moteur=self)
        self.platteformes.append(platteforme)
        self.demarrageA=pygame.time.get_ticks()
        self.dernierePlatteformeA=pygame.time.get_ticks()    
        self.clock=pygame.time.Clock()
        self.tempsPasse=0
           


    def quitterJeu(self):
        pygame.quit()
        sys.exit()

    def gameover(self):
        self.continuerJeu=False


    def boucle_principale(self):

        while self.continuerJeu:
                
            ecran.fill((0,0,0))
            

            for event in pygame.event.get():
            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction=-1
                        #print('déplacement gauche')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction=1
                        #print('déplacement droite')
                    if event.key==pygame.K_ESCAPE:
                        quitterJeu()

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction=0
                        #print('pas de déplacement')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction=0
                        #print('pas de déplacement')
                            
                if event.type==pygame.QUIT:
                    self.quitterJeu()


                   
            #gérer platteformes
            
            #déplacer platteformes
            for idx,platteforme in enumerate(self.platteformes):
                platteforme.y-=platteforme.vitesse
                if platteforme.y<-10:
                    self.platteformes.pop(idx)
                
            for platteforme in self.platteformes:
                platteforme.dessiner()
            
            #gérer joueur APRES platteformes (ne traverse pas platteforme sur base couleur)
            self.joueur.deplacer()
            self.joueur.dessiner()
                
            
            
            
            '''
            #to do : création de nouvelles platteformes en fonction du temps écoulé
            '''
            
            
            #to do : control fps       
            self.tempsPasse=self.clock.tick(60)
            
            pygame.display.update()



#démarrage du module

if __name__=="__main__":
    
    largeurEcran=800
    hauteurEcran=600
    couleurPlatteforme=(0,0,255)
    
    pygame.init()
    
    ecran=pygame.display.set_mode((largeurEcran,hauteurEcran))
    pygame.display.set_caption("Justdrop !")
    
    monMoteurJeu=MoteurJeu()        
    monMoteurJeu.initialisation_jeu()
    monMoteurJeu.boucle_principale()






            

    



