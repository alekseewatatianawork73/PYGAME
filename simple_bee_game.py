import pygame
pygame.init()

# определение RGB-цветов в кортежах
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('My game')

bee = pygame.image.load('images/bee.png')
new_bee = pygame.image.load('images/bee.png')
bg = pygame.image.load('images/bg.png')

x, y = w/2 - 50, h/2 - 46
x_step, y_step = -1, 0

run = True
while run:
    x, y = x + x_step, y + y_step
    screen.blit(bg, (0, 0))
    screen.blit(new_bee, (x, y))


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_step = -1
                new_bee = pygame.transform.rotate(bee, 90)
            if event.key == pygame.K_RIGHT:
                x_step = 1
                new_bee = pygame.transform.rotate(bee, -90)

        if event.type == pygame.QUIT:
            run = False
pygame.quit()
