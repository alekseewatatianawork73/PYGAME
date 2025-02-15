import pygame
pygame.init()

# определение RGB-цветов в кортежах
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


'''
Создадим главное игровое окно 900х505. Дадим название окну My Game.
Размеры окна лучше задавать в отдельных переменных, чтобы в дальнейшем использовать их в программе
'''
w, h = 900, 505
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('My Game')

screen.fill(WHITE)  # заливка фона белым цветом


'''
Сайт с png-картинками: pngwing.com
Загрузим в программу картинки с помощью функции load(). Для этого сначала внутри нашего проекта создадим
папку images, в которой будут храниться все используемые картинки. А затем в функции load() в качестве
аргумента укажем путь к нужной картинке.
'''
bg = pygame.image.load('images/bg.png')  # картинка для фона, размер: 900х505 (как w и h)
bee = pygame.image.load('images/bee.png')  # размер: 100x92
fox = pygame.image.load('images/fox.png')  # размер: 111x200


'''
С помощью класса pygame.Surface можно создавать дополнительные поверхности. После этого отрисовывать их на основной, 
которая создается методом pygame.display.set_mode(), или друг на друге. Отрисовка выполняется с помощью метода blit().
Если не принимать во внимание функции модуля pygame.draw, то все, что рисуется на поверхностях, 
делается с помощью метода blit().
'''
area = pygame.Surface((200, 200))  # создали квадратную поверхность 200х200
area.fill(BLACK)
pygame.draw.circle(area, RED, (100, 100), 50)  # рисуем на поверхности area красный круг

area.set_alpha(200)  # делаем поверхность area полупрозрачной (коэффициент прозрачности 0<=k<=255)

rct = pygame.Surface((500, 100))  # создали прямоугольную поверхность 500х100
rct.fill(GREEN)

screen.blit(rct, (w/2 - 250, h/2 - 50))  # отображаем зелёную непрозрачную прямоугольную поверхность
screen.blit(area, (w/2 - 100, h/2 - 100))  # отображаем черную полупрозрачную квадратную поверхность


'''
Картинки в Pygame также являются поверхностями, то есть объектами класса Surface, поэтому для отображения картинок
тоже используется метод blit(). Отобразим картинку fox с лисой на основном экране screen в самом верхнем углу. В методе 
blit() в качестве второго аргумента указываются координаты левого верхнего угла картинки.
'''
screen.blit(fox, (0, 0))


'''
Модуль pygame.transform содержит функции для изменения поверхностей. Некоторые трансформации (например, 
изменение размера) приводят к ухудшению изображения из-за потери части пикселей.
Функции модуля transform, которые изменяют поверхности, возвращают новые. Первым аргументом им передается 
изменяемая поверхность Surface. Рассмотрим на примере картинки с пчелой.
'''
new_bee1 = pygame.transform.scale(bee, (200, 184))  # изменяем размер пчелы на 200х184

new_bee2 = pygame.transform.flip(bee, False, True)  # поворачиваем пчелу по оси Oy (зеркально отображаем сверху вниз)
new_bee3 = pygame.transform.flip(bee, True, False)  # поворачиваем пчелу по оси Ox (зеркально отображаем слева направо)

new_bee4 = pygame.transform.rotate(bee, 90)  # поворачиваем пчелу влево на 90 градусов
new_bee5 = pygame.transform.rotate(bee, -90)  # поворачиваем пчелу вправо на 90 градусов


bg.blit(bee, (w/2 - 50, h/2 - 46))  # располагаем пчелу посередине на поверхности bg (поверх фоновой картинки)

# зададим фон игрового окна (размеры игрового окна и картинки для фона должны быть одинаковыми)
screen.blit(bg, (0, 0))

# обновляем игровое окно для отображения всех изменений (можно использовать update())
pygame.display.flip()

# игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
