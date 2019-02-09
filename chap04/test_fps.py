import pygame,sys
my_clock=pygame.time.Clock()

pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("test frames per second")
my_delay=0
count=0

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

            
    
    my_delay+=my_clock.tick()
    
    if my_delay>=33:
        count+=1
        #print(my_delay)
        print('*'*int(count/10))
        my_delay=0
    
    
