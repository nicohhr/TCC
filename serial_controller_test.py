import pygame 
from pygame.constants import*

import serial 
import time 

def map(x, in_min, in_max, out_min, out_max) -> float:
    return float((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


# Definindo taxas de velocidade (aceleração)
xlr8_m1 = 10
xlr8_m2 = 10

# Posição inicial dos motores/juntas
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
serialObj.baudrate = 9600
serialObj.port = 'COM5'
serialObj.open()

# Teste: Enviando letra A
print("CTRL + C para finalizar...")
byte_msg = bytearray([int(m1), int(m2), int(m3), int(m4), int(m5), int(m6)])

m1_plus = -1
m1_minus = -1


while True:

    for event in pygame.event.get():
        if event.type == JOYAXISMOTION:

            # Obtendo valor do Joystick 
            m1_plus = pygame.joystick.Joystick(0).get_axis(5)
            m1_minus = pygame.joystick.Joystick(0).get_axis(4)
    

    # Definindo razão de aceleração a partir da entrada
    m1_minus_ratio = map(m1_minus, -1, 1, 0, 1)
    m1_plus_ratio = map(m1_plus, -1, 1, 0, 1)
                    
    # Somando taxa de velocidade pela razão do gatilho
    m1 = m1 + xlr8_m1*m1_plus_ratio
    m1 = m1 - xlr8_m1*m1_minus_ratio

    # Conferindo que valor não passe de 180 nem seja menor que 0 
    if m1 > 180:
        m1 = 180
    elif m1 < 0: 
        m1 = 0   

    # Atualizando array de bytes 
    byte_msg = bytearray([int(m1), int(m1), int(m1), int(m1), int(m1), int(m1)])

    #print("Trigger Pos: ", trigger_pos)
    #print("Ratio Plus: ", m1_plus_ratio)
    #print("Ratio Minus: ", m1_minus_ratio)
    #print("M1: ", m1)

    serialObj.write(byte_msg)
    time.sleep(0.02)

    if serialObj.in_waiting: 
        packet = serialObj.readline()
        print(packet.decode())