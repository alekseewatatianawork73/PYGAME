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
        self.speed = random.randint(3, 9)

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
player = MyCar(pl)

# добавляем первую машину, которая появляется сразу
Car(random.randint(10, h), CARS_SURF[random.randint(0, 1)], cars)

'''Cоздаём пользовательское событие pygame.USEREVENT, которое будет происходить каждые две секунды. 
Это можно сделать при помощи модуля time.'''
pygame.time.set_timer(pygame.USEREVENT, 500)

run = True
while run:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        # каждые две секунды появляется новая машинка
        elif event.type == pygame.USEREVENT:
            Car(random.randint(10, h), CARS_SURF[random.randint(0, 1)], cars)

    # отображаем все машинки из группы cars
    all_cars.draw(screen)

    pygame.display.update()
    clock.tick(60)

    if pygame.sprite.spritecollideany(player, cars):
        run = False

    # двигаем машины влево
    all_cars.update()
pygame.quit()
