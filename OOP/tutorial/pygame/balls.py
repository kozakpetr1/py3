"""""
Jednoduchá hra v Pygame: Ovládání míčku a umístění do středu plátna.

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

# Výchozí pozice
ball_pos = [WIDTH // 2, HEIGHT // 2]
hole_pos = [WIDTH // 2, HEIGHT // 2]

# Herní smyčka
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detekce stisknutých kláves
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_pos[0] -= SPEED
    if keys[pygame.K_RIGHT]:
        ball_pos[0] += SPEED
    if keys[pygame.K_UP]:
        ball_pos[1] -= SPEED
    if keys[pygame.K_DOWN]:
        ball_pos[1] += SPEED

    # Kolize s okraji
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_pos[0] = max(BALL_RADIUS, min(ball_pos[0], WIDTH - BALL_RADIUS))

    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_pos[1] = max(BALL_RADIUS, min(ball_pos[1], HEIGHT - BALL_RADIUS))

    # Vykreslení
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.circle(screen, HOLE_COLOR, hole_pos, HOLE_RADIUS)
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)
    pygame.display.flip()
