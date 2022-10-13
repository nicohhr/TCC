from src.robotics import kinematics as kin 
import numpy as np

# Variaveis em cm 
d1 = 8.444
d2 = 10.5
d3 = 9.72
d4 = 2.8
d5 = 5.0 #16.5

'''
    Sinal Rotações 
    ----------
    - m2 = sinal negativo inclina para frente, positivo para atrás (Considerando outras posições como as iniciais)
    - m3 = angulo negativo inclina para baixo, positivo para acima (Considerando outras posições como as iniciais)

'''

# ----------------- CONVERTENDO ROTAÇÕES UNITY PARA DENAVIT

def servo1(servoPos : float) -> float:
    return kin.map(servoPos, 0, 180, 90, -90)

# Servo 2 corresponde diretamente a posição do servomotor, 0 é totalmente para frente,
# 180 totalmente para atrás 

def servo3(servoPos : float) -> float:
    return servoPos - 180

def servo4(servoPos : float) -> float: 
    return kin.map(servoPos, 0, 180, -90, 90)

# ----------------- DEFININDO ROTAÇÃO DE CADA JUNTA

j1 = 52
j2 = 60
j3 = 83
j4 = 12

# Posição das juntas
positions = [servo1(j1), j2, servo3(j3), servo4(j4)]

# Transformada 0-1 
h01 = kin.denavit(0, 90, d1, positions[0])

# Transformada 1-2
h12 = kin.denavit(d2, 0, 0, positions[1])

# Transformada 2-3
h23 = kin.denavit(d3, 0, 0, positions[2])

# Transformada 3-4
h34 = kin.denavit(d4, 90, 0, positions[3])

# Transformada 4-5
h45 = kin.denavit(0, 0, d5, 0)

# Exibindo resultado
print(h01)
print(h01.dot(h12))
print(h01.dot(h12).dot(h23))
print(h01.dot(h12).dot(h23).dot(h34))
#print(h01.dot(h12).dot(h23).dot(h34).dot(h45))

print(kin.getDenavitPositions((h01.dot(h12).dot(h23).dot(h34).dot(h45))))

#input("Press Enter to continue...")