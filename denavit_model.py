from turtle import position
from robotics import kinematics as kin
import numpy as np

# Variaveis em cm 
d1 = 8.5
d2 = 10.5
d3 = 10.2
d4 = 2.6
d5 = 16.5

'''
    Sinal Rotações 
    ----------
    - m2 = sinal negativo inclina para frente, positivo para atrás (Considerando outras posições como as iniciais)
    - m3 = angulo negativo inclina para baixo, positivo para acima (Considerando outras posições como as iniciais)

'''

# Posição das juntas
positions = [0, -0 + 90, -0 -90, 0, 0]

# Transformada 0-1 
h01 = kin.denavit(0, 90, d1, positions[0])

# Transformada 1-2
h12 = kin.denavit(d2, 0, 0, positions[1])

# Transformada 2-3
h23 = kin.denavit(d3, 0, 0, positions[2])

# Transformada 3-4
h34 = kin.denavit(d4, 90, 0, positions[3])

# Transformada 4-5
h45 = kin.denavit(0, 0, d5, positions[4])

# Exibindo resultado
print(h01)
print(h01.dot(h12))
print(h01.dot(h12).dot(h23))
print(h01.dot(h12).dot(h23).dot(h34))
print(h01.dot(h12).dot(h23).dot(h34).dot(h45))

input("Press Enter to continue...")