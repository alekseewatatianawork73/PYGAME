import pygame, gif_pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

w, h = 500, 269
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Game')

bg = gif_pygame.load('images/sea.gif')  # загружаем gif-картинку

'''
Классы Font и SysFont находятся в модуле pygame.font и предназначены для работы со шрифтами и текстом.
От классов pygame.font.Font и pygame.font.SysFont создаются объекты-шрифты. 
Второй класс берет системные шрифты, поэтому конструктору достаточно передать название шрифта. 
Классу Font надо передавать имя файла шрифта.
'''
f1 = pygame.font.SysFont('Arial', 25, True, False)
f2 = pygame.font.SysFont('Helvetica', 40, False, True)
f3 = pygame.font.Font('fonts/beauty.ttf', 70)

'''
В pygame есть шрифт по умолчанию. Чтобы использовать его, вместо имени файла в конструктор класса надо передать объект None.
'''
f_none = pygame.font.Font(None, 24)

'''
Метод render() создает поверхность (Surface), на которой написан заданный первым аргументом текст тем шрифтом, 
к которому применяется метод. Вторым аргументом указывается сглаживание, третьим – цвет текста. 
Четвертым аргументом можно указать цвет фона (необязательно).
'''
text = 'Hello!'
msg = f1.render(text, True, WHITE)
screen.blit(msg, (w / 2, h / 2))

'''
Узнать, какие шрифты есть в системе, можно с помощью функции get_fonts(). 
Также можно узнать адрес конкретного шрифта, используя match_font()
'''
print(pygame.font.get_fonts())
# => ['arial', 'arialblack', 'bahnschrift', 'calibri', 'cambria', 'cambriamath', 'candara', ...]
print(pygame.font.match_font('verdana'))
# => C:\Windows\Fonts\verdana.ttf

run = True
while run:
    # отображаем картинку в цикле, чтобы она постоянно менялась (чтобы сохранялась анимация)
    bg.render(screen, (0, 0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
