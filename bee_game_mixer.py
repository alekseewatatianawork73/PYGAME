import pygame
import random
pygame.init()

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Bee Game')

# загружаем картинки
bg = pygame.image.load('images/bg.png')  # установка фона
bee = pygame.image.load('images/bee.png')  # размер: 100x92

# загружаем звуки
circle_sound = pygame.mixer.Sound('sounds/circle.wav')
end_sound = pygame.mixer.Sound('sounds/game_over.wav')
pygame.mixer.music.load('sounds/main.mp3')

pygame.mixer.music.play(-1)  # проигрываем композицию постоянно

x_c, y_c = 100, 50

x, y = w/2 - 50, h/2 - 46
x_step, y_step = 0, -3
bee_new = pygame.image.load('images/bee.png')

f_end = pygame.font.SysFont(name='Arial', size=35, bold=True, italic=True)
game_over = f_end.render('GAME OVER', True, BLACK)
scr = 0

close = False
run = True
while run:
    clock.tick(60)

    while close:
        r = game_over.get_rect(center=(w / 2, h / 2))
        screen.blit(game_over, r)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
                run = False

    x += x_step
    y += y_step

    screen.blit(bg, (0, 0))

    score = f_end.render(f'Score: {scr}', True, BLACK)
    sc = score.get_rect(topleft=(0, 0))
    screen.blit(score, sc)

    surf = pygame.draw.circle(screen, BLACK, (x_c, y_c), 20)
    screen.blit(bee_new, (x, y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_step = -5
                y_step = 0
                bee_new = pygame.transform.rotate(bee, 90)
            if event.key == pygame.K_RIGHT:
                x_step = 5
                y_step = 0
                bee_new = pygame.transform.rotate(bee, -90)
            if event.key == pygame.K_UP:
                x_step = 0
                y_step = -5
                bee_new = bee
            if event.key == pygame.K_DOWN:
                x_step = 0
                y_step = 5
                bee_new = pygame.transform.rotate(bee, 180)
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()  # останавливаем музыку перед завершением игры
            run = False

    if x > w or y > h or x < 0 or y < 0:
        pygame.mixer.music.stop()  # останавливаем музыку перед завершением игры
        end_sound.play(0)  # запускаем звук завершения игры один раз
        close = True

    rct = bee_new.get_rect(topleft=(x, y))  # (x, y, width, height)
    if pygame.Rect.colliderect(surf, rct):
        circle_sound.play()  # при столкновении с шариком включаем короткий звуковой эффект
        scr += 1
        x_c = random.uniform(20, 900 - 20)
        y_c = random.uniform(20, 505 - 20)

pygame.quit()
