import pygame
from pygame.constants import*

# Incializando instância de jogo
pygame.init()
pygame.joystick.init()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

while True: 
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
        if event.type == JOYAXISMOTION:
            print(event)
        if event.type == JOYHATMOTION:
            print(event)

