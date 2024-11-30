import pygame
import random
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 500))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGNETA = (255, 0, 255)
colors = [RED, WHITE, BLACK, BLUE, MAGNETA, YELLOW, GREEN]

screen.fill(WHITE)
col1, col2 = True, True

run = True  # переменная для выхода из цикла (чтобы не было зависания)
while run:
    clock.tick(60)
    surf = pygame.draw.circle(screen, random.choice(colors), (700 / 2, 500 / 2), 100)
    surf1 = pygame.Rect((0, 0, 700/2, 500))
    surf2 = pygame.Rect((700/2, 0, 700/2, 500))
    if col1:
        pygame.display.update(surf1)
    if col2:
        pygame.display.update(surf2)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                col1 = True
                col2 = False
            if event.key == pygame.K_RIGHT:
                col1 = False
                col2 = True
            if event.key == pygame.K_DOWN:
                col1 = True
                col2 = True
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
