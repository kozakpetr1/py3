import pygame
import sys
import random
import math

pygame.init()

width, height, snowflakes_amount = 800, 600, 250

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snowfall Screensaver")
pygame.display.flip()

white = ((220, 220, 220),(160,160,180),(100, 100, 120))

snowflakes = []

class Snowflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(1, 3)
        self.wind = random.randint(-1,1)
        self.color = random.randint(0, 2)

    def fall(self):
        self.y += self.size
        if self.wind == -1:
            self.x += math.sin(self.y/90)
        elif self.wind == 1:
            self.x += math.cos(self.y/90)           
        if self.y > height:
            self.y = 0
            self.x = random.randint(0, width)
            self.size = random.randint(1, 3)
            self.wind = random.randint(-1,1)
            self.color = random.randint(0, 2)

    def draw(self):
        pygame.draw.circle(screen, white[self.color], (self.x, self.y), self.size)

for _ in range(snowflakes_amount):
    snowflakes.append(Snowflake(random.randint(0, width), random.randint(0, height)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  

    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    pygame.display.flip()
    pygame.time.Clock().tick(40)  
