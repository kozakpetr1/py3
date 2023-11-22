import pygame
import sys
import random
import math
import os


class Snowfall:
    
    def __init__(self, **kwargs):

        pygame.init()

        pygame.mixer.init()
        pygame.mixer.music.load(f"{os.path.dirname(os.path.realpath(__file__))}\\sound\\Magenta Six - Christmas 2.mp3")
        pygame.mixer.music.play()

        # self.__monitors = get_monitors()
        self.__info = pygame.display.Info()
        self.__width = kwargs['width'] if 'width' in kwargs else self.__info.current_w
        self.__height = kwargs['height'] if 'height' in kwargs else self.__info.current_h
        self.__snowflakes_amount = kwargs['snowflakes_amount'] if 'snowflakes_amount' in kwargs else self.__width * self.__height // 2000
        self.__snowflakes_to_add = kwargs['snowflakes_to_add'] if 'snowflakes_to_add' in kwargs else self.__width // 20
        self.__bg_image = kwargs['bg_image'] if 'bg_image' in kwargs else ("forest.jpg", "tree.jpg", "portrait.jpg", "road.jpg", "snowman.jpg", "church.jpg", "crystal.jpg", "nature.jpg", "sleigh.jpg", "prague.jpg", "santa.jpg", "woman.jpg", "ginger.jpg", "pinus.jpg")
        self.__white = kwargs['white'] if 'white' in kwargs else ((250, 250, 250, 10),(240,240,240, 10),(230, 230, 230, 10))
        self.__caption = kwargs['caption'] if 'caption' in kwargs else "Snowfall Screensaver"
        self.__speed = kwargs['speed'] if 'speed' in kwargs else 30
        self.__interval = kwargs['interval'] if 'interval' in kwargs else self.__width // 20
        
        self.__snowflakes = []

        self.__surface = pygame.display.set_mode((self.__width, self.__height), pygame.SRCALPHA, pygame.RESIZABLE)
        pygame.display.set_caption(self.__caption)
        self.__bg = pygame.image.load(f"{os.path.dirname(os.path.realpath(__file__))}\\img\\{self.__bg_image[random.randint(0, len(self.__bg_image) - 1)]}")
        self.__bg = pygame.transform.scale(self.__bg, (self.__width, self.__height))
        # pygame.mouse.set_visible(0)
        pygame.display.flip()
        
    def clearSnowflakes(self):
        self.__snowflakes = []

    def generateSnowflakes(self):
        for _ in range(self.__snowflakes_amount):
            self.__snowflakes.append(Snowflake(random.randint(0, self.__width), random.randint(0, self.__height), self.__width, self.__height))        
    
    def addSnowflakes(self):
        for _ in range(self.__snowflakes_to_add):
            x1 = (self.__pos[0] - self.__interval) if (self.__pos[0] - self.__interval) > 0 else 0
            x2 = (self.__pos[0] + self.__interval) if (self.__pos[0] + self.__interval) < self.__width else self.__width
            y1 = (self.__pos[1] - self.__interval) if (self.__pos[1] - self.__interval) > 0 else 0
            y2 = (self.__pos[1] + self.__interval) if (self.__pos[1] + self.__interval) < self.__width else self.__height
            self.__snowflakes.append(Snowflake(random.randint(x1, x2), random.randint(y1, y2), self.__width, self.__height))        

    def removeSnowflakes(self):
        for _ in range(self.__snowflakes_to_add):
            if len(self.__snowflakes) > 0:
                self.__snowflakes.pop(random.randint(0, len(self.__snowflakes)-1))

    def go(self):
        
        self.generateSnowflakes()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and (len(self.__snowflakes) < self.__width): 
                        self.__pos = pygame.mouse.get_pos()
                        self.addSnowflakes()
                    if event.button == 2:
                        if len(self.__snowflakes) == 0:
                            self.generateSnowflakes()
                        else:
                            self.clearSnowflakes()
                    if event.button == 3: 
                        self.__pos = pygame.mouse.get_pos()
                        self.removeSnowflakes()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and self.__width == self.__info.current_w:
                        self.__width = self.__info.current_w // 2
                        self.__height = self.__info.current_h // 2
                        self.__snowflakes_amount //= 4
                        self.clearSnowflakes()
                        self.generateSnowflakes()
                        self.__surface = pygame.display.set_mode((self.__width, self.__height), pygame.SRCALPHA, pygame.RESIZABLE)
                        self.__bg = pygame.transform.scale(self.__bg, (self.__width, self.__height))
                        pygame.display.flip()

            # self.__surface.fill((0,0,0))
            self.__surface.blit(self.__bg, (0,0))  

            for snowflake in self.__snowflakes:
                snowflake.fall(self.__width, self.__height)
                snowflake.draw(self.__surface, self.__white)

            pygame.display.flip()
            pygame.time.Clock().tick(self.__speed)  

class Snowflake:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__size = random.randint(2, 5)
        self.__wind = random.randint(-1,1)
        self.__color = random.randint(0, 2)

    def fall(self, width, height):
        self.__y += self.__size

        if self.__wind == -1:
            self.__x += math.sin(self.__y/90)
        elif self.__wind == 1:
            self.__x += math.cos(self.__y/90)           

        if self.__y > height:
            self.__y = 0
            self.__x = random.randint(0, width)
            self.__size = random.randint(2, 5)
            self.__wind = random.randint(-1,1)
            self.__color = random.randint(0, 2)

    def draw(self, surface, white):
        pygame.draw.circle(surface, white[self.__color], (self.__x, self.__y), self.__size)

snow = Snowfall()

"""
snow = Snowfall(\
    caption = "Vánoce",\
    width = 900,\
    height = 600,\
    speed = 50,\
    snowflakes_amount = 250,\
    snowflake_to_add = 50,\
    interval = 25, \
    bg_image = ("santa.jpg",),\
    white = ((255, 0, 0, 10),(0, 255, 0, 10),(0, 0, 255, 10))
)
"""
snow.go()