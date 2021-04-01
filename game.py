import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Codes Game")
################### загрузка изображений #########################
walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
pygame.image.load('right_4.png'), pygame.image.load('right_5.png'),
pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png'), pygame.image.load('left_5.png'),
pygame.image.load('left_6.png')]

bg = pygame.image.load('bg.png')
playerStand = pygame.image.load('idle_1.png')
##################################################################
clock = pygame.time.Clock()

x = 250
y = 440
widht = 25
height = 25
speed = 20

left = False
right = False
animCount = 0

def drowWindow():       # функция отрисовки игры
    global animCount
    win.blit(bg, (0, 0))

    if animCount + 1 >= 30:
        animCount = 0

    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
       win.blit(walkRight[animCount // 5], (x, y))
       animCount += 1
    else:
        win.blit(playerStand, (x, y))

    #win.blit(playerStand, (x, y))
    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
############################## Перемещение игрока #################################
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 10:
        x -= speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - height:
        x += speed
        left = False
        right = True
    else:
        left = False
        right = False
        animCount = 0
    #if keys[pygame.K_UP]:
    #    y -= speed
    #if keys[pygame.K_DOWN]:
    #    y += speed

    drowWindow()


pygame.quit()
