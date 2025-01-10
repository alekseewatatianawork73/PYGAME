import pygame
import random
pygame.init()

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 1200, 672
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Bird Game')


# основной игрок - птичка
class Bird(pygame.sprite.Sprite):
    def __init__(self, surf):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(150, h / 2))
        self.add(all_players)

    def update(self):
        p = pygame.key.get_pressed()
        if p[pygame.K_UP]:
            self.rect.y -= 7
        if p[pygame.K_DOWN]:
            self.rect.y += 7


# снаряды-ракеты (враги)
class Core(pygame.sprite.Sprite):
    def __init__(self, y, surf, group):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(w-10, y))
        self.add(group)
        self.add(all_players)
        self.speed = random.randint(3, 9)

    def update(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
        else:
            self.kill()


# яблоки (еда)
class Crcl(pygame.sprite.Sprite):
    def __init__(self, y, surf, group):
        super().__init__()
        self.image = surf
        self.rect = self.image.get_rect(center=(w-10, y))
        self.add(group)
        self.add(all_players)
        self.speed = 5

    def update(self):
        if self.rect.x > 0:
            self.rect.x -= self.speed
        else:
            global close
            close = True
            self.kill()


# загрузка всех изображений
bg = pygame.image.load('images/bg_sky.png')  # установка фона
bird = pygame.image.load('images/bird.png')  # размер: 100x92
core = pygame.image.load('images/core.png')  # размер: 90x90
surf = pygame.image.load('images/circle.png')

# создание групп спрайтов
cores = pygame.sprite.Group()
circles = pygame.sprite.Group()
all_players = pygame.sprite.Group()

# создание объектов-игроков
player = Bird(bird)
Core(random.randint(10, h), core, cores)
Crcl(random.randint(10, h), surf, circles)

# подбор шрифта и текста для события окончания игры
f_end = pygame.font.SysFont(name='Arial', size=35, bold=True, italic=True)
game_over = f_end.render('GAME OVER', True, BLACK)

# начальные данные
scr = 0
lvs = 3
x, y = 50, h/2 - 46

# установка пользовательских событий для появления ракет и яблок
ADDAPPLE = pygame.USEREVENT + 1
pygame.time.set_timer(pygame.USEREVENT, 3000)
pygame.time.set_timer(ADDAPPLE, 2000)

# игровой цикл
close = False
run = True
while run:
    clock.tick(60)

    # обработка завершения игры при проигрыше
    while close:
        r = game_over.get_rect(center=(w / 2, h / 2))
        screen.blit(game_over, r)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
                run = False

    # отображение на экране счёта и количества жизней
    screen.blit(bg, (0, 0))
    score = f_end.render(f'Score: {scr}', True, BLACK)
    lives = f_end.render(f'Lives: {lvs}', True, BLACK)
    sc = score.get_rect(topleft=(0, 0))
    lv = lives.get_rect(topleft=(w - 150, 0))
    screen.blit(score, sc)
    screen.blit(lives, lv)

    if lvs == 0:
        close = True

    # обновляем положение спрайтов на экране и отображаем их
    all_players.update()
    all_players.draw(screen)

    pygame.display.flip()

    for event in pygame.event.get():
        # обработка появления на экране новых яблок и ракет
        if event.type == pygame.USEREVENT:
            new_core = True
            Core(random.randint(10, h), core, cores)
        if event.type == ADDAPPLE:
            Crcl(random.randint(10, h), surf, circles)

        if event.type == pygame.QUIT:
            run = False

    # обработка столкновений
    spr_circle = pygame.sprite.spritecollide(player, circles, True)
    if spr_circle:
        scr += 1
    spr_cores = pygame.sprite.spritecollide(player, cores, True)
    if spr_cores:
        lvs -= 1

pygame.quit()
