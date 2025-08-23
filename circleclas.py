import pygame, random

pygame.init()

WIDTH=1000
HEIGHT=700

#creating screen
icon=pygame.image.load("circlecatchgame.png")
s=pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
pygame.display.set_caption("CircleCatch")
pygame.display.set_icon(icon)
blue=(0,0,255)
green=(0,255,0)
brown=(25,0,0)
#bradius = radius of the circle b_x= center of the ciircle
bradius =50
sradius=25
big_x, big_y= WIDTH//2, HEIGHT//2
small_x, small_y= random.randint(sradius, WIDTH - sradius), random.randint(sradius, HEIGHT - sradius)
speed=1
run=True

while(run):
    bigcirc=pygame.draw.circle(s,green,(big_x,big_y),bradius,3)
    smallcirc=pygame.draw.circle(s,blue,(small_x,small_y),sradius,0)
    pygame.display.flip()
    s.fill(brown)
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            run=False
            pygame.quit()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and big_x - bradius - speed >=0:
        big_x -= speed
    if keys[pygame.K_RIGHT] and big_x + bradius + speed <=WIDTH:
        big_x += speed
    if keys[pygame.K_UP] and big_y - bradius - speed >=0:
        big_y -= speed
    if keys[pygame.K_DOWN] and big_y + bradius + speed <=HEIGHT:
        big_y += speed
    if bigcirc.colliderect(smallcirc):
        small_x, small_y= random.randint(sradius, WIDTH - sradius), random.randint(sradius, HEIGHT - sradius)
    if keys[pygame.K_a] and big_x - bradius - speed >=0:
        big_x -= speed
    if keys[pygame.K_d] and big_x + bradius + speed <=WIDTH:
        big_x += speed
    if keys[pygame.K_w] and big_y - bradius - speed >=0:
        big_y -= speed
    if keys[pygame.K_s] and big_y + bradius + speed <=HEIGHT:
        big_y += speed