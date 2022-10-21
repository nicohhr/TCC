import math 
from src.robotics import simulator 

# Definindo tamanho dos elos [cm]
d1 = 8.444
d2 = 10.5
d3 = 9.72
d4 = 2.8
d5 = 5.0
#d1 = 8.5
#d2 = 10.5
#d3 = 10.2
#d4 = 2.6
#d5 = 16.5

# Funções de conversão
def t0(angle : float) -> float:
    return 90 - math.degrees(angle)

def t1(angle : float) -> float:
    return math.degrees(angle)

def t2(angle : float) -> float: 
    return 180 - math.degrees(angle)

x = 0
y = 0
z = 0

# Função para calculo da cinematica inversa do manipulador
def processInverseKinematics(desiredPos : list[float]):
    
    # Coordenadas da posição desejada 
    global x, y, z
    x = desiredPos[0]
    y = desiredPos[1]
    z = desiredPos[2] - 8.5

    #print(x, y, z)
    
    try:
        # CALCULANDO ROTAÇÃO DA BASE
        # - Obtendo "novo x"
        new_x = math.sqrt(x**2 + y**2)
        # - Calculando ângulo de rotação da junta da base
        theta_0 = math.asin(y/new_x)
        
        # CALCULANDO ROTAÇÃO DO BRAÇO 
        # - Obtendo theta 1
        theta_1_1 = math.atan2(z, new_x) 
        theta_1_2 = math.acos((new_x**2 + z**2 + d2**2 - d3**2)/(2*d2*math.sqrt(new_x**2 + z**2)))
        theta_1 = theta_1_1 + theta_1_2
        
        # - Obtendo theta 2
        theta_2 = math.acos((new_x**2 + z**2 - d2**2 - d3**2)/(2*d2*d3))
        #print("t0:", t0(theta_0))
        #print("t1:", t1(theta_1))
        #print("t2:", t2(theta_2))
        return [t0(theta_0), t1(theta_1), t2(theta_2), 90, 0, 0]

    except ValueError:
        return [0, 0, 0, 0, 0, 0]

# Conectando com o simulador
simulator.connect()

while True: 

    # Recebendo dados
    endPos = simulator.getData(3)

    # Posição de juntas calculado
    jointPositions = processInverseKinematics(endPos)

    # Enviando dados
    simulator.sendArmData(motorPos=jointPositions)

    print(jointPositions, x, y, z)