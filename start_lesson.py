import pygame  # импортируем библиотеку pygame

pygame.init()  # перед использованием функций Pygame необходимо инициализировать библиотеку

screen = pygame.display.set_mode((700, 500))  # создаём окно с размерами 700х500 пикселей
# pygame.display.set_mode(size, flags=0, depth=0, display=0, vsync=0)

run = True  # переменная для выхода из цикла (чтобы не было зависания)
while run:
    # обработка событий
    for event in pygame.event.get():  # получаем список событий

        if event.type == pygame.KEYDOWN:  # проверяем, что нажата кнопка на клавиатуре
            if event.key == pygame.K_SPACE:  # проверяем конкретную кнопку - пробел
                print('Нажат пробел.')
            else:
                print('Нажата кнопка на клавиатуре')

        if event.type == pygame.MOUSEBUTTONDOWN:  # проверяем, что нажата кнопка мыши
            if event.button == 1:
                print("Левая кнопка мыши нажата.")
            if event.button == 5:
                print('Колесо мыши прокручивается вверх')
            if event.button == 4:
                print('Колесо мыши прокручивается вниз')
            if event.button == 3:
                print("Правая кнопка мыши нажата.")

        if event.type == pygame.MOUSEMOTION:  # проверяем, что двигается курсор
            print("Курсор мыши двигается.")

        if event.type == pygame.QUIT:  # проверяем, что произошло закрытие окна
            pygame.quit()  # закрываем окно
            run = False  # завершаем цикл

print('Программа работает')
