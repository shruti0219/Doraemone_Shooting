import pygame
import random
import math
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((500, 600))
run = True

# title logo
pygame.display.set_caption("Fighting Doraemone")
icon = pygame.image.load('doraemon.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('back.jpg')

# player - 128 pixles
pimage = pygame.image.load('icon.png')
playerX = 186
playerY = 422
playerX_change = 0


def player(x, y):
    screen.blit(pimage, (x, y))


# enemy
no_of_enemies = 4
penemy = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
for i in range(no_of_enemies):
    penemy.append(pygame.image.load('mouse.png'))
    enemyX.append(random.randint(10, 452))
    enemyY.append(random.randint(10, 200))
    enemyX_change.append(2)
    enemyY_change.append(50)


def enemy(x, y, i):
    screen.blit(penemy[i], (x, y))


# bullet
bulletimage = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 422
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletimage, (x + 42, y - 30))




def collide(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if distance < 35:
        return True
    else:
        return False


# score
score = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf', 28)


def show_score(x, y):
    sh = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(sh, (x, y))


over_font = pygame.font.Font('freesansbold.ttf', 64)

def gameover():
    gv = over_font.render("GAME OVER" , True,(255,255,255))
    sh = font.render("Your Score : " + str(score), True, (255, 255, 255))
    screen.blit(gv,(50,200))
    screen.blit(sh, (150, 280))

while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_UP:
                if bullet_state == 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change

    # player movement
    if playerX >= 372:
        playerX = 372
    if playerX <= 10:
        playerX = 10

    player(playerX, playerY)

    # enemy movement
    for i in range(no_of_enemies):
        if enemyX[i] >= 452:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] <= 10:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]

        enemyX[i] += enemyX_change[i]
        enemy(enemyX[i], enemyY[i], i)

        collision = collide(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = mixer.Sound('impact.wav')
            collision_sound.play()
            bulletY = 422
            bullet_state = 'ready'
            score += 1
            enemyX[i] = random.randint(10, 452)
            enemyY[i] = random.randint(10, 200)

        #game over
        if enemyY[i] >= 390:
            for j in range(no_of_enemies):
                enemyY[j] = 20000
            gameover()
            break


    # bullet movement
    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    if bulletY <= 0:
        bulletY = 422
        bullet_state = 'ready'

    show_score(textX, textY)
    pygame.display.update()
