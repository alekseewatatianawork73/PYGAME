import random
import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (128, 128, 128)

# главное окно
WIDTH, HEIGHT = 1200, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Спрайты, повторяющиеся события")
clock = pygame.time.Clock()
# шрифт в игре
font = pygame.font.SysFont('bookmanoldstyle', 30, True)

start_time = pygame.time.get_ticks()  # время начала игры


# класс главного персонажа
class Player(pygame.sprite.Sprite):
    # конструктор
    def __init__(self, x, y, image, *groups):
        super().__init__(*groups)  # вызываем метод добавления в группу из родительского класса
        image = pygame.transform.scale(image, (120, 120))
        self.image = pygame.transform.rotate(image, -90)
        self.rect = self.image.get_rect(center=(x, y))  # x, y - координаты центра персонажа
        self.speed = 3  # скорость движения персонажа

    # обновление положения
    def update(self):
        p = pygame.key.get_pressed()  # список событий на клавиатуре
        if p[pygame.K_UP]:
            self.rect.y -= self.speed
        if p[pygame.K_DOWN]:
            self.rect.y += self.speed
        # проверка на выход за границы экрана
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    # метод draw() не нужен, он есть в группе спрайтов и общий для всех


# класс метеоритов
class Meteor(pygame.sprite.Sprite):
    def __init__(self, image, speed, *groups):
        super().__init__(*groups)
        self.image = image
        self.rect = self.image.get_rect()  # x, y - левый верхний угол
        self.rect.x = WIDTH  # создаём метеорит за правой границей экрана
        self.rect.y = random.randint(0, HEIGHT - self.rect.height)
        self.speed = speed

    # все метеориты двигаются влево
    def update(self):
        self.rect.x -= self.speed
        # если метеорит добрался до левой границы, удаляем его из игры и увеличиваем счёт на 1
        if self.rect.right < 0:
            self.kill()
            global score
            score += 1

    # метод draw() не нужен, он есть в группе спрайтов и общий для всех


# загружаем картинку для фона и приводим её к размерам главного окна
bg = pygame.image.load('images/bg_space.jpg')
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

# загружаем картинки ракеты и метеорита и удаляем фон на картинках
player_image = pygame.image.load('images/space_rocket.png')
player_image.set_colorkey(WHITE)
meteor_image = pygame.image.load('images/meteorit.png')
meteor_image.set_colorkey(WHITE)

all_sprites = pygame.sprite.Group()  # группа для всех объектов
meteorites = pygame.sprite.Group()  # группа только для метеоритов

player = Player(WIDTH // 2, HEIGHT // 2, player_image, all_sprites)  # создаём игрока
meteor_speed = 8  # скорость метеоритов в пикселях
Meteor(meteor_image, meteor_speed, meteorites, all_sprites)  # создаём первый метеорит

# создаём событие - появление нового метеорита на экране
NEW_METEOR = pygame.event.custom_type()
# указываем, что событие будет повторяться каждые 2 секунды (2000 миллисекунд)
time_meteor = 2000
pygame.time.set_timer(NEW_METEOR, time_meteor)

# создаём событие - ускорение игры
INCREASE_SPEED = pygame.event.custom_type()
# указываем, что событие будет повторяться каждые 10 секунд (10 000 миллисекунд), но только два раза!
pygame.time.set_timer(INCREASE_SPEED, 10000, 2)

run = True
game_over = False  # конец игры
win = False  # победа (играли 35 секунд)
bg_x = 0  # координата фона (имитация движения)
game_speed = 5  # скорость игры (перемещения фона) в пикселях
score = 0  # счёт игры

# игровой цикл
while run:
    clock.tick(60)  # таймер (60 кадров в секунду)
    # если прошло 35 секунд с начала игры, значит, победа - игра завершается
    if pygame.time.get_ticks() - start_time >= 35 * 1000:
        win = True

    if not game_over and not win:
        # имитация движения: рисуем два фона друг за другом и двигаем их на 5 пикселей за кадр по оси x (справа налево)
        screen.blit(bg, (bg_x, 0))
        screen.blit(bg, (WIDTH + bg_x, 0))
        bg_x -= game_speed
        # когда второй фон полностью заменил первый, возвращаем их в исходное положение
        if bg_x <= -WIDTH:
            bg_x = 0

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # проверяем, что произошло событие NEW_METEOR (которое происходит каждые 2 секунды)
        if event.type == NEW_METEOR:
            # создаём новый метеор
            Meteor(meteor_image, meteor_speed, meteorites, all_sprites)
        # проверяем, что произошло событие INCREASE_SPEED (которое происходит каждые 10 секунд)
        if event.type == INCREASE_SPEED:
            game_speed += 2  # увеличиваем скорость движения фона
            player.speed += 2  # увеличиваем скорость игрока
            meteor_speed += 2  # увеличиваем скорость движения метеоритов
            time_meteor -= 700  # увеличиваем частоту появления метеоритов (на 700 мс чаще)
            pygame.time.set_timer(NEW_METEOR, time_meteor)

    # отображаем надпись про счёт игры в координатах (10, 10)
    mssg_score = font.render(f'Счёт игры: {score}', True, BLACK)
    screen.blit(mssg_score, (10, 10))

    if not game_over and not win:
        # обновляем положение всех спрайтов
        all_sprites.update()

    # проверяем, сталкивается ли игрок с метеоритами (dokill=True - удаляем метеорит при столкновении)
    if pygame.sprite.spritecollide(player, meteorites, True):
        game_over = True  # игра завершается - проиграли

    # отрисовываем сразу все спрайты
    all_sprites.draw(screen)

    # если победили или проиграли, отображаем сообщения об этом на неподвижном фоне
    if win or game_over:
        screen.blit(bg, (0, 0))
        txt_win = font.render(f'Вы дошли до конца игры! Победа!\nВаш счёт {score}.', True, BLACK)
        txt_over = font.render(f'Вы проиграли :(', True, BLACK)
        mssg = txt_win if win else txt_over
        rect_mssg = mssg.get_rect(center=(WIDTH // 2, 300))
        screen.blit(mssg, rect_mssg)
        screen.blit(mssg, rect_mssg)

    pygame.display.flip()  # обновляем кадр на экране

pygame.quit()  # закрываем окно игры

# САМОСТОЯТЕЛЬНОЕ ЗАДАНИЕ:
# 1. Обработайте столкновение игрока-ракеты с метеоритом - в этом случае метеорит должен удаляться с экрана
# (используйте в игровом цикле метод spritecollide)
# 2. Добавьте в игру жизни - игра заканчивается не при первом столкновении с метеоритом, а после третьего
# (три жизни - нужна переменная счётчик до цикла)
# 3. Добавьте бонусы, при столкновении с которыми будет увеличиваться счёт (нужен новый класс для бонусов).
