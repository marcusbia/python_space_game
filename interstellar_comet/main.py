import pygame
from pygame import *
import random
import os



# all colors of the window
black = (0, 0, 0)


(width, height) = (450, 450)
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("interstellar comet")


# menu
menu_IMG = pygame.image.load("IMG/play_button.png")
menu_IMG = pygame.transform.scale(menu_IMG, (200, 30))

exit_IMG = pygame.image.load("IMG/exit_button.png")
exit_IMG = pygame.transform.scale(exit_IMG, (200, 30))


name = pygame.image.load("IMG/name.png")
name = pygame.transform.scale(name, (350, 32))


# player
player = pygame.image.load("IMG/player.png")
player = pygame.transform.scale(player, (32, 32))
x = 225
y = 400
player_vel = 3


# rock
rock_IMG = pygame.image.load("IMG/Big_rock.png")
rock_IMG = pygame.transform.scale(rock_IMG, (20, 20))
rock_state = ("ready")

rock_vel = (0.7)

rock_X = random.choice(range(20, 410))
rock_Y = (20)


# bullet
bullet_IMG = pygame.image.load("IMG/bullet.png")
bullet_IMG = pygame.transform.scale(bullet_IMG, (2, 32))
bullet_X = (x)
bullet_Y = (-200)
bullet_vel = (8)
bullet_state = ("ready")


# health
heart = pygame.image.load("IMG/heart.png")
h_X = (16)
h_Y = (18)
h_X1 = (h_X+21)
h_X2 = (h_X1+21)

health = (3)


# game stastes
game_states = ("menu")




run = True
while run:





    # win fps
    pygame.time.delay(10)

    # close win
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ev = pygame.event.get()

    mouse_X, mouse_Y = pygame.mouse.get_pos()

    if game_states == "menu":
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse_X in range(130, 330):
                if mouse_Y in range(200, 230):

                    game_states = ("playing")

    if game_states == "menu":
        if event.type == pygame.MOUSEBUTTONDOWN:

            if mouse_X in range(130, 330):
                if mouse_Y in range(250, 280):

                    run = False

    if game_states == "playing":

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= player_vel

        if keys[pygame.K_RIGHT]:
            x += player_vel

        if keys[pygame.K_SPACE]:
            if bullet_state == "ready":
                bullet_state = ("flying")
                bullet_X = (x+15)
                WIN.blit(bullet_IMG, (bullet_X, bullet_Y))
                bullet_Y = (400-32)
                



                
               



    if game_states == "playing":
        if rock_state == "ready":
            rock_Y = (rock_Y + rock_vel)
            WIN.blit(rock_IMG, (rock_X, rock_Y))

        if rock_Y >= 450:
            rock_Y = (-20)
            rock_X = random.choice(range(20, 430))
            health = (health - 1)

        if health == 2:
            h_X2 = (500)

        if health == 1:
            h_X1 = (500)

        if health == 0:
            game_states = ("menu")

    # checks if bullet_state is what is needed
    if bullet_state == "flying":

        bullet_Y = (bullet_Y - bullet_vel)

        if bullet_Y <= -32:
            bullet_Y = (-200)
            WIN.blit(bullet_IMG, (bullet_X, bullet_Y))
            bullet_state = ("ready")

        one = (rock_X)
        two = (rock_X+20)

        o = (one)
        r = (two)

        e = range(o, r)

        if bullet_X in e:
            if bullet_Y <= rock_Y:
                rock_Y = (-32)
                rock_X = random.choice(range(20, 410))
                rock_vel = rock_vel + 0.1

    # WIN update
    WIN.fill(black)

    if game_states == "menu":
        WIN.blit(menu_IMG, (130, 200))
        WIN.blit(exit_IMG, (130, 250))
        WIN.blit(name, (60, 50))

    if game_states == "playing":
        WIN.blit(rock_IMG, (rock_X, rock_Y))

        WIN.blit(heart, (h_X, h_Y))
        WIN.blit(heart, (h_X1, h_Y))
        WIN.blit(heart, (h_X2, h_Y))

        WIN.blit(player, (x, y))
        WIN.blit(bullet_IMG, (bullet_X, bullet_Y))
        # makes player not move out of screen
        if x < 5:
            x = (5)

        if x > 410:
            x = (410)

    pygame.display.update()


# quit
pygame.quit()
