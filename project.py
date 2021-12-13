import pygame
from random import choice
import time
import tkinter as tk
from tkinter import messagebox

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_a,
    K_d,
    K_e,
    K_p,
    K_b,
    K_u,
    K_s
)

pygame.init()
clock = pygame.time.Clock()
background_image = pygame.image.load(r'background.png')
image = pygame.image.load(r'archer_idle_1.png')
image2 = pygame.image.load(r'download.png')
default_bg_size = (800,650)
background_image = pygame.transform.scale(background_image, default_bg_size)
white = (255, 255, 255)
black = (0, 0, 0)

#text setup
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

def lost():
    message_display('You Lost')

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',115)
        TextSurf, TextRect = text_objects("You have to defeat the monsters to save the princess./n You can find extra health in the scroll room./n Directional keys are used to move while 'A' and 'D' are used to attack and defend./n 'B' is to go back, 'P' is to pick 'E' is to enter and 'U' is to go up./n Press 'S' to start", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
    if event.type == K_s:
        intro = False

#player setup
x = 500
y = 500
x1 = 400
y1 = 400
velocity = 10
default_player_size = (75,75)
image = pygame.transform.scale(image, default_player_size)
image2 = pygame.transform.scale(image2, default_player_size)
Player_life = 100
image2_life = 100


# game screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Princess Rescue')

i = 0
c = 1
    
def attack(character, target, target_hp, power):
    damage_taken = target_hp - power
    target_hp = damage_taken

def defence(character, target, target_hp, power):
    damage = 0
    damage_taken = target_hp - damage
    target_hp = damage_taken

running = True
outside = True
downstairs = False
alive = True
upstairs = False
princess_rescued = False
final_battle = False
picked = False
i = 0
c = 1
monst_moves = ['Nothing', 'Attack']
monst_move = choice(monst_moves)
    
while running:
    screen.fill((255,255,255))
    screen.blit(background_image, [0, 0])
    screen.blit(image, (x,y))
            
    for event in pygame.event.get():
            
        if event.type == KEYDOWN:

            if event.key == K_LEFT:
                x -= velocity

            if event.key == K_RIGHT:
                x += velocity

            if event.key == K_UP:
                y -= velocity

            if event.key == K_DOWN:
                y += velocity
                
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
                quit()

            
        elif event.type == QUIT:
            running = False
            pygame.quit()
            quit()
                
    while alive and (abs(x-x1)<=50 or abs(y-y1)<=50):
        screen.blit(image2, (x1,y1))
        while Player_life > 0 or image2_life > 0:
            if event.key == K_a:
                player_move = attack(image, image2, image2_life, 10)
            elif event.key == K_d:
                player_move = defence(image, image2, Player_life, 20)
            if monst_move == 'Attack':
                if  event.key == K_d:
                    pass
                else:
                    monst_attack = attack(image2, image, Player_life, 20)
        if Player_life == 0:
            lost()
            running = False
            pygame.quit()
            quit()
        elif image2_life == 0:
            alive = False
            outside = False
            background_image = pygame.image.load(r'background2.png')
            background_image = pygame.transform.scale(background_image, default_bg_size)

    screen.blit(background_image, [0, 0])
    while downstairs:
        if event.key == K_e:
            background_image = pygame.image.load(r'background3.png')
            background_image = pygame.transform.scale(background_image, default_bg_size)
            screen.blit(background_image, [0, 0])
            while not picked:
                image3 = pygame.image.load(r'firstaid.png')
                image3 = pygame.transform.scale(image3, default_player_size)
                screen.blit(image3, (x1,y1))
            if event.key == K_p:
                picked = True
                Player_life = 100
            if event.key == K_b:
                background_image = pygame.image.load(r'background2.png')
                background_image = pygame.transform.scale(background_image, default_bg_size)
                screen.blit(background_image, [0, 0])
        elif event.key == K_u:
            downstairs = False
            upstairs = True

    while upstairs:
        background_image = pygame.image.load(r'background3.png')
        background_image = pygame.transform.scale(background_image, default_bg_size)
        screen.blit(background_image, [0, 0])
        final_battle = True
        image2 = pygame.image.load(r'images2.png')
        image2 = pygame.transform.scale(image2, default_player_size)
        image2_life = 100
        screen.blit(image2, (x1,y1))
        while final_battle and (abs(x-x1)<=50 or abs(y-y1)<=50):
            screen.blit(image2, (x1,y1))
            while Player_life > 0 or image2_life > 0:
                if event.key == K_a:
                    player_move = attack(image, image2, image2_life, 10)
                elif event.key == K_d:
                    player_move = defence(image, image2, Player_life, 20)
                if monst_move == 'Attack':
                    if  event.key == K_d:
                        pass
                    else:
                        monst_attack = attack(image2, image, Player_hp, 20)
            if Player_life == 0:
                lost()
                running = False
                pygame.quit()
                quit()
            elif image2_life == 0:
                final_battle = False
                princess_rescued = True
                upstairs = False
                background_image = pygame.image.load(r'background3.png')
                background_image = pygame.transform.scale(background_image, default_bg_size)
                screen.blit(background_image, [0, 0])
                running = False
                pygame.quit()
                quit()
    
pygame.display.update()
pygame.time.wait(500) 
