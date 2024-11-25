import pygame
import random

# Inicializace Pygame
pygame.init()

# Velikost okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simulace sněžení s obrázky vloček')

# Definice barev
BLACK = (0, 0, 0)

# Načtení obrázku vločky (musí být PNG s průhledností)
snowflake_image = [
    pygame.image.load('./basics/workspace/small_snowflake_8x8a.png'),
    pygame.image.load('./basics/workspace/small_snowflake_8x8b.png'),
    pygame.image.load('./basics/workspace/small_snowflake_10x10a.png'),
    pygame.image.load('./basics/workspace/small_snowflake_10x10b.png'),
    pygame.image.load('./basics/workspace/small_snowflake_12x12a.png'),
    pygame.image.load('./basics/workspace/small_snowflake_12x12b.png')
]

# Třída pro vločky s obrázkem
class Snowflake:
    def __init__(self):
        self.image = snowflake_image[random.randint(0, len(snowflake_image)-1)]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(-SCREEN_HEIGHT, 0)
        self.speed_y = random.uniform(1, 3)  # Rychlost pádu
        self.wind = random.uniform(-1, 1)  # Horizontální vítr

    def update(self, wind_speed):
        self.rect.y += self.speed_y
        self.rect.x += self.wind + wind_speed  # Přidání vlivu větru
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randint(-50, -10)
            self.rect.x = random.randint(0, SCREEN_WIDTH)
        if self.rect.x > SCREEN_WIDTH or self.rect.x < 0:
            self.rect.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Seznam vloček
snowflakes = [Snowflake() for _ in range(300)]  # Vytvoříme 100 vloček

# Hlavní smyčka
running = True
clock = pygame.time.Clock()

# Parametr větru
wind_speed = 0

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ovládání větru pomocí šipek vlevo a vpravo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        wind_speed -= 0.01  # Vítr doleva
    if keys[pygame.K_RIGHT]:
        wind_speed += 0.01  # Vítr doprava

    # Aktualizace a vykreslení vloček
    for snowflake in snowflakes:
        snowflake.update(wind_speed)
        snowflake.draw(screen)

    # Aktualizace obrazovky
    pygame.display.flip()

    # Nastavení FPS (počet snímků za sekundu)
    clock.tick(60)

# Ukončení Pygame
pygame.quit()
