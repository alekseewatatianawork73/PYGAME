# подключаем библиотеки
import random
import pygame
pygame.init()

# создаём таймер для установки частоты смены кадров
clock = pygame.time.Clock()

# создаём игровое окно и задаём фон экрана
w, h = 800, 586
screen = pygame.display.set_mode((w, h))
bg = pygame.image.load('images/road.png')

# картинки для машин
CARS = ('images/car1.png', 'images/car2.png')
# список для хранения существующих машин
CARS_SURF = []
for i in range(len(CARS)):
    CARS_SURF.append(pygame.image.load(CARS[i]))


# класс машин-спрайтов
class Car(pygame.sprite.Sprite):
    def __init__(self, y, surf, group):
        super().__init__()
        self.image = surf
        # прямоугольник, в котором находится машинка
        self.rect = self.image.get_rect(center=(w-10, y))
        # добавляем в группу
        self.add(group)
        self.add(all_cars)
        # у машин будет разная скорость
        self.speed = random.randint(7, 11)

    # метод для движения машинок
    def update(self):
        if self.rect.x < w:
            # двигаемся влево
            self.rect.x -= self.speed
        else:
            # удаляем из всех групп
            self.kill()


class MyCar(pygame.sprite.Sprite):
    def __init__(self, surf):
        super().__init__()
        self.image = surf
        # прямоугольник, в котором находится машинка
        self.rect = self.image.get_rect(center=(w / 2 - 50, h / 2))
        self.add(all_cars)

    # метод для движения машинки
    def update(self):
        p = pygame.key.get_pressed()
        if p[pygame.K_UP]:
            self.rect.y -= 5
        if p[pygame.K_DOWN]:
            self.rect.y += 5


# группа для машин-спрайтов
cars = pygame.sprite.Group()
all_cars = pygame.sprite.Group()

pl = pygame.image.load('images/my_car.png')
pl2 = pygame.image.load('images/my_car_2.png')
pl2 = pygame.transform.flip(pl2, True, False)
player = MyCar(pl)

# добавляем первую машину, которая появляется сразу
Car(random.randint(10, h), CARS_SURF[random.randint(0, 1)], cars)

# установка пользовательских событий
DISTANCE = pygame.USEREVENT + 1
pygame.time.set_timer(pygame.USEREVENT, 500)
pygame.time.set_timer(DISTANCE, 500)

f_end = pygame.font.SysFont(name='Arial', size=30, bold=True, italic=True)
game_over = f_end.render('GAME OVER', True, (0, 0, 0))

cls = 0
meters = 0
res = None

run = True
close = False
while run:
    screen.blit(bg, (0, 0))

    clls = f_end.render(f'Collisions: {cls}/5', True, (0, 0, 0))
    mtr = f_end.render(f'Distance: {meters} m', True, (0, 0, 0))
    cl = clls.get_rect(topleft=(w - 250, 0))
    screen.blit(clls, cl)
    mt = mtr.get_rect(topleft=(10, 0))
    screen.blit(mtr, mt)

    # обработка завершения игры при проигрыше
    while close:
        r1 = game_over.get_rect(center=(w / 2, h / 2 - 150))
        r2 = res.get_rect(center=(w/2, h / 2))
        screen.blit(game_over, r1)
        screen.blit(res, r2)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = False
                run = False

    if not run:
        break

    if cls == 5:
        res = f_end.render(f'YOUR RESULT: {meters} M', True, (0, 0, 0))
        close = True

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # каждые две секунды появляется новая машинка
        if event.type == pygame.USEREVENT:
            Car(random.randint(10, h), CARS_SURF[random.randint(0, 1)], cars)

        if event.type == DISTANCE:
            meters += 10

    # отображаем все машинки из группы cars
    all_cars.draw(screen)

    pygame.display.update()
    clock.tick(60)

    if pygame.sprite.spritecollide(player, cars, True):
        cls += 1

    # двигаем машины влево
    all_cars.update()
pygame.quit()



