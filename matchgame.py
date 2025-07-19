import pygame,fontTools

pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill((255,255,245))
pygame.display.update()

LG=pygame.image.load("ludo.png")
CC=pygame.image.load("ccGame.jpg")
SS=pygame.image.load("ssGame.png")
TR=pygame.image.load("trGame.png")

screen.blit(TR,(150,200))
screen.blit(LG,(150,300))
screen.blit(SS,(150,400))
screen.blit(TR,(150,500))
text=pygame.font.SysFont("Times New Roman",35,bold=True)
S0S=text.render("SubwaySurfers",True,(71,40,255))
T0R=text.render("TempleRun",True,(71,40,255))
L0G=text.render("Ludo",True,(71,40,255))
C0C=text.render("CandyCrush",True,(71,40,255))
screen.blit(S0S,(500,200))
screen.blit(L0G,(500,300))
screen.blit(C0C,(500,400))
screen.blit(T0R,(500,500))
pygame.display.update()