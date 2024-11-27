import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Bee Game')

bg = pygame.image.load('images/bg.png')  # установка фона
bee = pygame.image.load('images/bee.png')  # размер: 100x92

x, y = w/2 - 50, h/2 - 46
x_step, y_step = 0, -1
bee_new = pygame.image.load('images/bee.png')

run = True
while run:
    x += x_step
    y += y_step
    if x > w or y > h or x < 0 or y < 0:
        run = False

    screen.blit(bg, (0, 0))
    screen.blit(bee_new, (x, y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_step = -1
                y_step = 0
                bee_new = pygame.transform.rotate(bee, 90)
            if event.key == pygame.K_RIGHT:
                x_step = 1
                y_step = 0
                bee_new = pygame.transform.rotate(bee, -90)
            if event.key == pygame.K_UP:
                x_step = 0
                y_step = -1
                bee_new = bee
            if event.key == pygame.K_DOWN:
                x_step = 0
                y_step = 1
                bee_new = pygame.transform.rotate(bee, 180)

        if event.type == pygame.QUIT:
            run = False

pygame.quit()
