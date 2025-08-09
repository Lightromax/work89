import pygame, random, fontTools, sys

WIDTH=800
HEIGHT=800
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

mousepos = pygame.mouse.get_pos()
GS=pygame.image.load("goodshot.png")
GSrect=GS.get_rect()
GSrect.x=random.randint(0, WIDTH - GSrect.width)
GSrect.y=random.randint(0, HEIGHT - GSrect.height)
text=pygame.font.Font(None,70)
goodshot=text.render("Good Shot",True,(0,25,5))
gs_rect=goodshot.get_rect(center=(400,400))

score=0
showgs=False
run=True
while(run):
    mousepos=pygame.mouse.get_pos()
    screen.fill((255,255,255))
    screen.blit(GS,(GSrect))
    pygame.display.flip()
    for pygame.events in pygame.event.get():
        if pygame.events.type == pygame.MOUSEBUTTONDOWN and pygame.events.button == 1:
            mousepos=pygame.events.pos
            if GSrect.collidepoint(mousepos):
                GSrect.x=random.randint(0, WIDTH - GSrect.width)
                GSrect.y=random.randint(0, HEIGHT - GSrect.height)
                score += 1
                #showgs=True
            #if showgs == True:
                screen.blit(goodshot,gs_rect)
                pygame.display.flip()  
                pygame.display.update()
        if pygame.events.type == pygame.QUIT:
            run=False
            pygame.quit()
            print(score)
