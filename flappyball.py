import pygame,random

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Ball")
timer=pygame.time.Clock()
fps=60
green=(0,255,0)
lightblue=(20,20,255)
yellow=(255,255,0)
#ball variable
ballx=50
ballY=HEIGHT//2
ballrad=17
ballvx=0
gravity=0.5
bounce=-8
#pipe rect varibles
pipelength=60
pipegap=150
pipeheight=random.randint(100,400)
pipex=WIDTH

run=True

while(run):
    screen.fill(lightblue)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run=False
            pygame.quit()