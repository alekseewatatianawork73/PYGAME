import pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)

# загрузка нового изображения для курсора
cur = pygame.image.load('images/pencil.png')
# создаём объект-курсор
cursor = pygame.cursors.Cursor((30, 20), cur)
# устанавливаем объект в качестве нового курсора
pygame.mouse.set_cursor(cursor)

'''
Для работы со звуком можно использовать модуль pygame.mixer. Есть два основных типа объектов: Sound (для коротких
звуковых эффектов) и Music (для длительных музыкальных треков).
'''
circle_sound = pygame.mixer.Sound('sounds/circle.wav')
pygame.mixer.music.load('sounds/main.mp3')
'''
С помощью функции music.play() файл начинает проигрываться. Если требуется зациклить композицию, то в play() 
передается число -1. Положительный аргумент указывает на количество повторов + одно дополнительное. То есть, 
если надо проиграть композицию 2 раза, то в функцию передается число 1.
'''
pygame.mixer.music.play(-1)  # проигрываем композицию постоянно

run = True
drw = False
while run:
    pygame.display.flip()

    # рисуем круг в месте нажатия на кнопку мыши
    pos = pygame.mouse.get_pos()
    p = pygame.mouse.get_pressed()
    if p[0]:
        pygame.draw.circle(screen, BLUE, pos, 20)
        circle_sound.play()  # при нажатии на кнопку мыши включаем короткий звуковой эффект

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

pygame.mixer.music.stop()  # останавливаем музыку перед завершением игры
pygame.quit()
