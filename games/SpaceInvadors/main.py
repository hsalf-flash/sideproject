import pygame
import random

pygame.init()
# create screen use tuple to initialize the size of the screen
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
# title and icon
pygame.display.set_caption("Space Invaders")
# create the variable to load the image and then use the image
icon = pygame.image.load('technology.png')
pygame.display.set_icon(icon)
# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 750)
enemyY = random.randint(50, 200)
enemyX_change = 4
enemyY_change = 40

# Bullet

# Ready state means you can fire now
# Fire state bullet is already moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = 'ready'

# initialzing the player
playerImg = pygame.image.load('player.png')
# initialize the position
playerX = 370
playerY = 480
playerX_change = 0.0
playerY_change = 0.1


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 16))


def player_movemnet(player_X, player_Y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("Left arrow pressed")
            playerX_change = -5

        if event.key == pygame.K_RIGHT:
            playerX_change = 5
            print("Right arrow pressed")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("Keystroke has been released ")
            playerX_change = 0


running = True
while running:
    screen.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    enemy(enemyX, enemyY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # adding keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # Establishing boundaries for both enemy and player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 768:
        playerX = 768

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 768:
        enemyX_change = -3
        enemyY += enemyY_change

    #Movement of bullet
    if bulletY<=0:
        bulletY = 480
        bullet_state = 'ready'
    if bullet_state== "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    # necessary in order to update the screen else it will show previous data only
    pygame.display.update()
