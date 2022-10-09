import math
from turtle import delay
import pygame 
from pygame.constants import*

import serial 
import time 

def map(x, in_min, in_max, out_min, out_max) -> float:
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# Definindo taxas de velocidade (aceleração)
xlr8_m1 = 10
xlr8_m2 = 10

# Posição inicial dos motores/juntas (OBS: transformar em array)
m1 = 90
m2 = 90
m3 = 90
m4 = 90
m5 = 90
m6 = 90

# Incializando instância de jogo
pygame.init()
pygame.joystick.init()
pygame.event.pump()

joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

# Inicializando instância serial
serialObj = serial.Serial() 

# Definindo propriedades 
serialObj.baudrate = 115200
serialObj.port = 'COM6'
serialObj.open()

# Teste: Enviando letra A
print("CTRL + C para finalizar...")
byte_msg = bytearray([79, 80, int(m1), int(m2), int(m3), int(m4), int(m5), int(m6), 69, 68])

m1_plus = -1
m1_minus = -1

# Motor a ser movimentado
motor_selection = 1

# Pulando lixo serial
for i in range(50):
  serialObj.readline()


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
    m1_minus_ratio = map(m1_minus, -1, 1, 0, 1)
    m1_plus_ratio = map(m1_plus, -1, 1, 0, 1)
                    
    # Somando taxa de velocidade pela razão do gatilho
    match motor_selection:
        case 1: 
            m1 = m1 + xlr8_m1*m1_plus_ratio
            m1 = m1 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m1 > 180:
                m1 = 180
            elif m1 < 0: 
                m1 = 0   
        case 2:
            m2 = m2 + xlr8_m1*m1_plus_ratio
            m2 = m2 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m2 > 180:
                m2 = 180
            elif m2 < 0: 
                m2 = 0   
        case 3:
            m3 = m3 + xlr8_m1*m1_plus_ratio
            m3 = m3 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m3 > 180:
                m3 = 180
            elif m3 < 0: 
                m3 = 0   
        case 4: 
            m4 = m4 + xlr8_m1*m1_plus_ratio
            m4 = m4 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m4 > 180:
                m4 = 180
            elif m4 < 0: 
                m4 = 0   
        case 5: 
            m5 = m5 + xlr8_m1*m1_plus_ratio
            m5 = m5 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m5 > 180:
                m5 = 180
            elif m5 < 0: 
                m5 = 0   
        case 6: 
            m6 = m6 + xlr8_m1*m1_plus_ratio
            m6 = m6 - xlr8_m1*m1_minus_ratio

            # Conferindo que valor não passe de 180 nem seja menor que 0 
            if m6 > 180:
                m6 = 180
            elif m6 < 0: 
                m6 = 0   
    

    # Atualizando array de bytes 
    byte_msg = bytearray([79, 80, int(m1), int(m2), int(m3), int(m4), int(m5), int(m6), 69, 68])

    #print("Trigger Pos: ", trigger_pos)
    #print("Ratio Plus: ", m1_plus_ratio)
    #print("Ratio Minus: ", m1_minus_ratio)     
    #print("M1: ", m1)

    serialObj.write(byte_msg)
    time.sleep(0.02)

    if serialObj.in_waiting: 
        packet = serialObj.readline()
        #print(packet.decode())
        print(int(m1), int(m2), int(m3), int(m4), int(m5), int(m6))