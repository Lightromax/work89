import pygame
import random
import sys

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Game")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 200, 255)
GREEN = (0, 255, 0)

# Bird
bird_x = 50
bird_y = HEIGHT // 2
bird_radius = 15
bird_velocity = 0
gravity = 0.5
flap_strength = -8

# Pipe
pipe_width = 60
pipe_gap = 150
pipe_x = WIDTH
pipe_height = random.randint(100, 400)

# Game loop
running = True
while running:
    screen.fill(BLUE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Bird flap
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_velocity = flap_strength

    # Bird movement
    bird_velocity += gravity
    bird_y += bird_velocity

    # Draw bird
    pygame.draw.circle(screen, WHITE, (bird_x, int(bird_y)), bird_radius)

    # Pipe movement
    pipe_x -= 4
    if pipe_x + pipe_width < 0: 
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)

    # Draw pipes
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, pipe_width, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + pipe_gap, pipe_width, HEIGHT))

    # Collision
    if (bird_y - bird_radius <= 0 or bird_y + bird_radius >= HEIGHT or
        (pipe_x < bird_x + bird_radius < pipe_x + pipe_width and
        (bird_y < pipe_height or bird_y > pipe_height + pipe_gap))):
        print("Game Over")
        pygame.time.delay(1000)
        bird_y = HEIGHT // 2
        bird_velocity = 0
        pipe_x = WIDTH
        pipe_height = random.randint(100, 400)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
