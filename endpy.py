import pygame

WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)

# Actors
bag=pygame.image.load("bag.png")
bin=pygame.image.load("recyclebin.png")
rbag=pygame.image.load("rubberbag.png")
background=pygame.image.load("healback.png")
box=pygame.image.load("smallbox.png")
#Sprites
bagRECT=bag.get_rect()
binRECT=bin.get_rect()
rbagRECT=rbag.get_rect()
box=box.get_rect()
#Variables
run=True
score=0
background=pygame.transform.scale(pygame.image.load("healback.png"),(600,600))
screen.blit(background,(0,0))
#Loop
while(run):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            run=False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                if binRECT.y >= 0:
                    binRECT.y += 2
            if events.key == pygame.K_s:
                if binRECT.y <= HEIGHT:
                    binRECT.y -= 2
            if events.key == pygame.K_a:
                if binRECT.x <= 0:
                    binRECT.x -= 2
            if events.key == pygame.K_d:
                if binRECT.x <= WIDTH:
                    binRECT.x += 2
        