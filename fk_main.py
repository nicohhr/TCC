from src.robotics import simulator 
from src.robotics import kinematics as kin
import numpy as np

JOINT_COUNT = 4 # definindo quantidade de motores 

# ----------------- Conversão de rotações referencia unity/servo para Denavit

def servo1(servoPos : float) -> float:
    return kin.map(servoPos, 0, 180, 90, -90)

# Servo 2 corresponde diretamente a posição do servomotor, 0 é totalmente para frente,
# 180 totalmente para atrás 

def servo3(servoPos : float) -> float:
    return servoPos - 180

def servo4(servoPos : float) -> float: 
    return kin.map(servoPos, 0, 180, -90, 90)

# ----------------- DEFININDO ROTAÇÃO DE CADA JUNTA

# Declarando comprimento dos elos em [cm]
d1 = 8.444
d2 = 10.5
d3 = 9.72
d4 = 2.8
d5 = 5.0

# Declarando posição inicial de das juntas em graus, valores de 0 a 180
j1 = 90.0
j2 = 90.0
j3 = 90.0
j4 = 90.0
initialPositions = [j1, j2, j3, j4]

# Definindo tabela de cálculo de Denavit-Hartenberg
def processDenavitTable(jointPositions : list[float]) -> list[float]:
    
    # Processando referência das juntas
    positions = [servo1(jointPositions[0]), jointPositions[1], servo3(jointPositions[2]), servo4(jointPositions[3])]

    # Calculando linhas da tabela
    h01 = kin.denavit(0, 90, d1, positions[0])
    h12 = kin.denavit(d2, 0, 0, positions[1])
    h23 = kin.denavit(d3, 0, 0, positions[2])
    h34 = kin.denavit(d4, 90, 0, positions[3])
    h45 = kin.denavit(0, 0, d5, 0)
    return  kin.getDenavitPositions((h01.dot(h12).dot(h23).dot(h34).dot(h45)))

# ----------------------------------------------------------------------------

# Estabelecendo conexão com o simulador
simulator.connect()

# Iniciando loop do programa 
while True: 

    # Recebendo posição das juntas do simulador
    armPositions = simulator.getData(JOINT_COUNT)

    # Calculando posição do end effector pela cinematica direta
    endEffector_pos = processDenavitTable(armPositions)

    # Enviando posição calculada de volta 
    simulator.sendArmData(fk_pos=endEffector_pos)

    # Exibindo posição calculada
    print(armPositions, endEffector_pos)