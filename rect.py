import pygame
pygame.init()
WHITE = (255, 255, 255)

w, h = 900, 505
screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)

'''
Картинки ограничены экземплярами класса Rect, как и любые другие поверхности, поэтому мы можем работать с расположением
картинок при помощи различных атрибутов и методов данного класса.
'''
fox = pygame.image.load('images/fox.png')  # размер: 111x200
screen.blit(fox, (0, 0))
rct = fox.get_rect()
print(rct)  # => <rect(0, 0, 111, 200)>
print(rct.center)  # => (55, 100)
print(rct.bottom)  # => 200
print(rct.right)  # => 111
print(rct.left)  # => 0
print(rct.bottomright)  # => (111, 200)

# смещение прямоугольной области rct из положения (0, 0) в положение (100, 100)
rct_new = rct.move(100, 100)
print(rct_new)  # => <rect(100, 100, 111, 200)>

# пример
rect1 = pygame.Rect((0, 0, 30, 30))
rect2 = pygame.Rect((30, 30, 30, 30))

rect2.move_ip(20, 20)
print(rect2)  # => <rect(50, 50, 30, 30)>
rect3 = rect2.union(rect1)
print(rect3)  # => <rect(0, 0, 80, 80)>



pygame.display.flip()

# игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
