from ctypes import sizeof
from turtle import delay
import pygame 
from pygame.constants import *

import serial 
import time 
import numpy as np 
import src.robotics.simulatorData as sd

MOTORS = 6 

# Metdos 
def map(x, in_min, in_max, out_min, out_max) -> float:
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

# Posiçao angular de cada um dos motores 
motorPositions = np.tile(np.float32(90), MOTORS)

# Definindo taxas de velocidade (aceleração)
xlr8 = np.tile(np.float32(0.01), MOTORS)

# Incializando instância de jogo
pygame.init()
pygame.joystick.init()
pygame.event.pump()

# Inicializando controles conectados no sistema
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
print("CTRL + C para finalizar...")

# Definindo motor a ser movimentado
motor_selection = 1
m1_plus = -1
m1_minus = -1

while True: 

    for event in pygame.event.get():

        # Conferindo se há algum botão selecionado
        if event.type == pygame.JOYHATMOTION:

            x_hat = pygame.joystick.Joystick(0).get_hat(0)[0]
            
            # Definindo motor selecionado a partir do pad direcional 
            if x_hat == 1 and (motor_selection < 6): 
                motor_selection = motor_selection + 1 

            elif x_hat == -1 and (motor_selection > 1):
                motor_selection = motor_selection - 1

        # Conferindo se houve alteração na posição dos gatilhos
        if event.type == JOYAXISMOTION:

            # Obtendo valor do Joystick 
            m1_plus = pygame.joystick.Joystick(0).get_axis(5)
            m1_minus = pygame.joystick.Joystick(0).get_axis(4)

    
    # Definindo razão de aceleração a partir da entrada
    m_minus_ratio = map(m1_minus, -1, 1, 0, 1)
    m_plus_ratio = map(m1_plus, -1, 1, 0, 1)

    # Somando prduto do gatilho com a taxa de velocidade
    motorPositions[motor_selection-1] = motorPositions[motor_selection-1] + xlr8[motor_selection-1]*m_plus_ratio
    motorPositions[motor_selection-1] = motorPositions[motor_selection-1] - xlr8[motor_selection-1]*m_minus_ratio

    # Conferindo que valor não passe de 180 nem seja menor que 0 
    if motorPositions[motor_selection-1] > 180:
        motorPositions[motor_selection-1] = 180
    elif motorPositions[motor_selection-1] < 0: 
        motorPositions[motor_selection-1] = 0   

    #sd.sendJointData(motorPos=motorPositions)
    #sd.sendFloatData(motorPositions[0])
    sd.sendArmData(motorPos=motorPositions)
    print(motorPositions)