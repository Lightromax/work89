import pygame, fontTools,sys

pygame.init()
pygame.display.set_caption("Match the Scrambled")
screen=pygame.display.set_mode((800,800))
screen.fill((30,30,30))
run=True

text=pygame.font.SysFont("Times New Roman",35,bold=True)
cl=text.render("lCpa",True,(71,40,245))
da=text.render("cnDae",True,(71,40,245))
ce=text.render("btoiCleearn",True,(71,40,245))
re=text.render("ssiRenacet",True,(71,40,245))
cla=text.render("Clap",True,(71,40,145))
dan=text.render("Dance",True,(71,40,145))
cel=text.render("Celebration",True,(71,40,145))
res=text.render("Resistance",True,(71,40,145))


while(run):
    screen.blit(cl,(150,200))
    screen.blit(da,(150,300))
    screen.blit(ce,(150,400))
    screen.blit(re,(150,500))
    screen.blit(cla,(500,500))
    screen.blit(dan,(500,400))
    screen.blit(cel,(500,200))
    screen.blit(res,(500,300))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run=False
        if events.type == pygame.MOUSEBUTTONDOWN:
            mousepos=pygame.mouse.get_pos()
            pygame.draw.circle(screen,(255,255,254),(mousepos),20,0)
            pygame.display.update
        elif events.type == pygame.MOUSEBUTTONUP:
            mousepos2=pygame.mouse.get_pos()
            pygame.draw.line(screen,(0,0,255),(mousepos),(mousepos2),5)
            pygame.draw.circle(screen,(0,255,0),(mousepos2),20,0)
            pygame.display.update()
pygame.quit()
sys.exit()