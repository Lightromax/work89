import pygame, random

WIDTH=800
HEIGHT=800

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))

bee=pygame.image.load("honeybee.png").convert_alpha()
bee_rect=bee.get_rect()
bee_rect.center=(WIDTH//2,HEIGHT//2)
bee_speed=5
flower=pygame.image.load("flower.png").convert_alpha()
flow_rect=flower.get_rect()
flow_rect.x=random.randint(0, WIDTH - flow_rect.width)
flow_rect.y=random.randint(0, HEIGHT - flow_rect.height)
game_on=True
score=0
while(game_on):
    screen.fill(("red"))
    screen.blit(bee,(bee_rect))
    screen.blit(flower,(flow_rect))
    pygame.display.flip()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            pygame.quit()
            game_on=False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_UP:
                if bee_rect >= 0:
                    bee_rect -=bee_speed
            if events.key == pygame.K_DOWN:
                if   bee_rect >= 0:
                    bee_rect +=bee_speed
            if events.key == pygame.K_LEFT:
                if bee_rect >= 0:
                    bee_rect -=bee_speed
            if events.key == pygame.K_RIGHT:
                if bee_rect >= 0:
                    bee_rect +=bee_speed
    if bee_rect.left < 0:
        bee_rect.left=0
    if bee_rect.right > WIDTH:
        bee_rect.right=WIDTH
    if bee_rect.top < 0:
        bee_rect.top=0
    if bee_rect.bottom > HEIGHT:
        bee_rect.bottom=HEIGHT
    if bee_rect.colliderect(flow_rect):
        score + 1
        flow_rect.x=random.randint(0, WIDTH - flow_rect.width)
        flow_rect.y=random.randint(0, HEIGHT - flow_rect.height)