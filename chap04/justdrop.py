import pygame, sys, random, time
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
        testCouleurX,testCouleurY=0,0        
        #debug      
        #print("avant déplacement : x={} y={}".format(self.x,self.y))
        
        #vérifier si sur une platteforme, sinon tombe
        
        
           
        #On vérifie les coordonnées du pixel à tester pour éviter de sortir de l'écran
        testCouleurDroiteX=self.x+self.largeur
        if testCouleurDroiteX==largeurEcran:
            testCouleurDroiteX=largeurEcran-1
        testCouleurGaucheX=self.x
        if testCouleurGaucheX<0:
            testCouleurGaucheX=0
        testCouleurY=self.y+self.hauteur
        if testCouleurY==hauteurEcran:
            testCouleurY=hauteurEcran-1
        elif testCouleurY<0:
            testCouleurY=0
        #debug
        #print("testgauchex:{} testdroitex : {} testy: {}".format(testCouleurGaucheX,testCouleurDroiteX,testCouleurY))      
        if (ecran.get_at((testCouleurGaucheX,testCouleurY))==(0,0,0,255) and ecran.get_at((testCouleurDroiteX,testCouleurY))==(0,0,0,255)):
            self.tombe=True
        else :
            self.tombe=False
            #se positionner sur le dessus de la platteforme
            try:
                while (ecran.get_at((self.x,testCouleurY))==couleurPlatteforme or ecran.get_at((testCouleurX,testCouleurY))==couleurPlatteforme):
                    self.y=self.y-1
                    testCouleurY=self.y+self.hauteur-1
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
            return 0 #gameover
        
        if self.y+self.hauteur > hauteurEcran:
            self.y=hauteurEcran-self.hauteur
            self.tombe=False
    
        #vérifier si limites écran
        if (self.x+self.largeur)>largeurEcran:
            self.x=largeurEcran-self.largeur
        elif self.x <0:
            self.x=0

        return 1 #game is not over, go on ...                  
        
        


class Platteforme:
    #variables de classe
    dernierePlatteformeA=0
    delaiPlatteforme=1000
    
    def __init__(self,x,y,vitesse,couleur,moteur):
        self.vitesse=vitesse
        self.couleur=couleur
        self.x=x
        self.y=y
        self.hauteur=10
        self.positionTrou=0
        self.moteur=moteur
        self.creer_trou()
        Platteforme.dernierePlatteformeA=pygame.time.get_ticks()
        

               
    def dessiner(self):
        
            
        pygame.draw.rect(ecran,self.couleur,(self.x,\
            self.y,largeurEcran,self.hauteur))
        
        pygame.draw.rect(ecran,(0,0,0),(self.positionTrou,\
            self.y,40,self.hauteur))

    def creer_trou(self):
                       
        self.positionTrou=random.randint(0,hauteurEcran-40)

        
        
    def deplacer(self):
        pass



class MoteurJeu:
    
    def __init__(self):
        #self.largeurEcran=largeurEcran
        #self.hauteurEcran=hauteurEcran
        #self.ecran=None
        self.joueur=None
        self.platteformes=[]
        self.demarrageA=0
        self.dernierTickA=0
        self.jeuDemarre=False
        self.gameover=False

        
    def initialisation_jeu(self):
        self.joueur=Joueur(x=int(largeurEcran/2),y=int(hauteurEcran/2),dx=5,dy=5,\
                     largeur=25,hauteur=40,couleur=(255,0,0),moteur=self,tombe=False)
        self.platteformes.clear()
        platteforme=Platteforme(vitesse=2,x=0,y=int(hauteurEcran*2/3),couleur=couleurPlatteforme,moteur=self)
        self.platteformes.append(platteforme)
        self.demarrageA=pygame.time.get_ticks()
        self.dernierTickA=self.demarrageA
        self.clock=pygame.time.Clock()
        self.maintenant=0  


    def quitterJeu(self):
        pygame.quit()
        sys.exit()

    def menu_gameover(self):
        font=pygame.font.SysFont("arialblack",25)
        text=font.render("Gameover! <ESPACE> pour continuer",True,(255,0,0))
        
        ecran.fill((0,0,0))
        ecran.blit(text,((largeurEcran-text.get_width())//2,(hauteurEcran-text.get_height())//2))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        return
                        
                    if event.key==pygame.K_ESCAPE:
                        self.quitterJeu()
                       
                if event.type==pygame.QUIT:
                    self.quitterJeu()
        
    def menu_demarrage(self):
        font=pygame.font.SysFont("arialblack",25)
        text=font.render("Just drop ! <ESPACE> pour commencer",True,(0,255,0))
        
        ecran.fill((0,0,0))
        ecran.blit(text,((largeurEcran-text.get_width())//2,(hauteurEcran-text.get_height())//2))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        self.jeuDemarre=True
                        return
                        
                    if event.key==pygame.K_ESCAPE:
                        self.quitterJeu()
                       
                if event.type==pygame.QUIT:
                    self.quitterJeu()
                   
            
    def verifier_ajout_platteforme(self):                        
            
        self.maintenant=pygame.time.get_ticks()
        if self.maintenant-Platteforme.dernierePlatteformeA>Platteforme.delaiPlatteforme:
            #créer nouvelle platteforme
            #print("tick création platteforme: {}".format(self.maintenant))
            
            platteforme=Platteforme(vitesse=2,x=0,y=hauteurEcran+50,couleur=couleurPlatteforme,moteur=self)
            self.platteformes.append(platteforme)
                 
    def deplacer_platteformes(self):
        for idx,platteforme in enumerate(self.platteformes):
            platteforme.y-=platteforme.vitesse
            if platteforme.y<-10:
                self.platteformes.pop(idx)
                
    def dessiner_platteformes(self):
        for platteforme in self.platteformes:
            platteforme.dessiner()
        
            


    def boucle_principale(self):
        self.initialisation_jeu()        
        
        while True:
            ecran.fill((0,0,0))
        
            if self.jeuDemarre:
                self.verifier_ajout_platteforme()
                self.deplacer_platteformes()
                self.dessiner_platteformes()
                #dessiner platteformes avant déplacer joueur car test couleur pixel en-dessous du joueur
                self.gameover=not(self.joueur.deplacer())
                if self.gameover:
                    self.jeuDemarre=False
                self.joueur.dessiner()
            elif self.gameover:
                self.jeuDemarre=False
                self.menu_gameover()
                self.gameover=False
                
            else:
                self.menu_demarrage()
                self.jeuDemarre=True
                self.initialisation_jeu()
                
                        
            pygame.display.update()
        
            #test touches
            for event in pygame.event.get():
            
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction=-1
                        #print('déplacement gauche')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction=1
                        #print('déplacement droite')
                    if event.key==pygame.K_ESCAPE:
                        self.quitterJeu()

                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT:
                        self.joueur.direction=0
                        #print('pas de déplacement')
                    if event.key==pygame.K_RIGHT:
                        self.joueur.direction=0
                        #print('pas de déplacement')
                            
                if event.type==pygame.QUIT:
                    self.quitterJeu()

            #control fps       
            self.tempsPasse=self.clock.tick(60)



#démarrage du module
if __name__=="__main__":
    
    largeurEcran=800
    hauteurEcran=600
    couleurPlatteforme=(0,0,255)
    
    pygame.init()
    
    ecran=pygame.display.set_mode((largeurEcran,hauteurEcran))
    pygame.display.set_caption("Justdrop !")
    
    monMoteurJeu=MoteurJeu()        
    monMoteurJeu.boucle_principale()






            

    



