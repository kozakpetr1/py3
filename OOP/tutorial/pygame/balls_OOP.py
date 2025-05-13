"""""
Objektová verze hry v Pygame: Ovládání míčku a umístění do středu plátna.

Hráč ovládá míček pomocí šipek. Míček se rovnoměrně pohybuje po plátně
a odráží se od okrajů. Cílem je dostat míček do středu plátna (jamka).

Ovládání:
    - Šipka nahoru: pohyb nahoru
    - Šipka dolů: pohyb dolů
    - Šipka doleva: pohyb doleva
    - Šipka doprava: pohyb doprava
"""

import pygame
import sys

# Inicializace Pygame
pygame.init()

# Konstanty
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 15
HOLE_RADIUS = 20
BALL_COLOR = (0, 102, 204)
HOLE_COLOR = (0, 204, 102)
BACKGROUND_COLOR = (255, 255, 255)
SPEED = 5

# Nastavení okna
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Ball Game")


class Ball:
    """ Reprezentace míčku ve hře """
    def __init__(self, x, y):
        self.pos = [x, y]
        self.radius = BALL_RADIUS
        self.color = BALL_COLOR

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos[0] -= SPEED
        if keys[pygame.K_RIGHT]:
            self.pos[0] += SPEED
        if keys[pygame.K_UP]:
            self.pos[1] -= SPEED
        if keys[pygame.K_DOWN]:
            self.pos[1] += SPEED

        # Kolize s okraji
        self.pos[0] = max(self.radius, min(self.pos[0], WIDTH - self.radius))
        self.pos[1] = max(self.radius, min(self.pos[1], HEIGHT - self.radius))

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


class Hole:
    """ Reprezentace jamky ve středu plátna """
    def __init__(self, x, y):
        self.pos = [x, y]
        self.radius = HOLE_RADIUS
        self.color = HOLE_COLOR

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.radius)


# Inicializace objektů
ball = Ball(WIDTH // 2, HEIGHT // 2)
hole = Hole(WIDTH // 2, HEIGHT // 2)

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    ball.move(keys)

    # Vykreslení
    screen.fill(BACKGROUND_COLOR)
    hole.draw(screen)
    ball.draw(screen)
    pygame.display.flip()

