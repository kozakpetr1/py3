import pygame
import sys
import random
import math
import os

pygame.init()

width, height, snowflakes_amount = 800, 600, 250
white = ((250, 250, 250, 10),(240,240,240, 10),(230, 230, 230, 10))
# bg_image = ("tree.jpg", "snowman.jpg", "church.jpg", "crystal.jpg", "nature.jpg", "sleigh.jpg", "prague.jpg", "santa.jpg", "woman.jpg")

surface = pygame.display.set_mode((width, height), pygame.SRCALPHA)
pygame.display.set_caption("Snowfall Screensaver")
# bg = pygame.image.load(f"{os.path.dirname(os.path.realpath(__file__))}\\img\\sleigh.jpg")

pygame.mouse.set_visible(0)
pygame.display.flip()

snowflakes = []

class Snowflake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
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
            self.size = random.randint(2, 5)
            self.wind = random.randint(-1,1)
            self.color = random.randint(0, 2)

    def draw(self):
        pygame.draw.circle(surface, white[self.color], (self.x, self.y), self.size)

for _ in range(snowflakes_amount):
    snowflakes.append(Snowflake(random.randint(0, width), random.randint(0, height)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    surface.fill((0,0,0))
    # surface.blit(bg, (0,0))  

    for snowflake in snowflakes:
        snowflake.fall()
        snowflake.draw()

    pygame.display.flip()
    pygame.time.Clock().tick(30)  
