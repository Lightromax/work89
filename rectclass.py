import pygame

screen = pygame.display.set_mode((900,800))

class rect:
    def __init__(self,color, dimensions):
        self.color = color
        self.dimensions = dimensions
        self.screen = screen
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.dimensions)
        
blackrect = rect((113,0,113),(50,50,500,500))        
bluerect = rect((0,0,255),(100,200,200,300))
greenrect = rect((0,255,0),(100,400,400,90))
purplesquare = rect((255,0,255),(50,200,200,90))
purplesquare2 = rect((255,0,255),(350,200,200,90))
eyerect = rect((200,0,200),(80,200,100,90))
eyerect2 = rect((192,0,192),(390,200,100,90))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(("black"))
    bluerect.draw()
    blackrect.draw()
    greenrect.draw()
    purplesquare.draw()
    purplesquare2.draw()
    eyerect.draw()
    eyerect2.draw()
    pygame.display.update()

pygame.quit()