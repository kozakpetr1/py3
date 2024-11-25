import pygame
import random
import math

# Inicializace Pygame
pygame.init()

# Velikost okna
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Simulace sněžení s realistickými vločkami')

# Definice barev
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Třída pro realistické sněhové vločky
class Snowflake:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(-SCREEN_HEIGHT, 0)
        self.size = random.randint(4, 6)  # Velikost hvězdičky
        self.speed_y = random.uniform(1, 3)  # Rychlost pádu
        self.wind = random.uniform(-1, 1)  # Horizontální vítr
        self.points = self.create_star(self.size)

    def create_star(self, size):
        """Vytvoří body pro hvězdicovou vločku."""
        points = []
        for i in range(6):  # Šestiúhelník jako základ hvězdičky
            angle = math.pi / 3 * i
            x = math.cos(angle) * size
            y = math.sin(angle) * size
            points.append((x, y))
        return points

    def update(self, wind_speed):
        self.y += self.speed_y
        self.x += self.wind + wind_speed  # Přidání vlivu větru
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-50, -10)
            self.x = random.randint(0, SCREEN_WIDTH)
        if self.x > SCREEN_WIDTH or self.x < 0:
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, screen):
        points = [(self.x + p[0], self.y + p[1]) for p in self.points]
        pygame.draw.polygon(screen, WHITE, points)

# Seznam vloček
snowflakes = [Snowflake() for _ in range(150)]  # Vytvoříme 150 vloček

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
