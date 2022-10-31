import math
import re 
from src.robotics import simulator 

# Definindo tamanho dos elos [cm]
d1 = 8.444
d2 = 10.5
d3 = 9.72
l3 = 4.28297 #5.77 # #3.9

# Angulo de offset de end effector
offset_angle = math.atan2(28, 50)

# Angulo da ferramenta em relação a superficie 
phi = math.radians(-90) #-(math.radians(90) - offset_angle)

# Funções de conversão
def t0(angle : float) -> float:
    val = 90 - math.degrees(angle)
    return clamp(val, 0, 180)

def t1(angle : float) -> float:
    val = math.degrees(angle)
    return clamp(val, 0, 180)

def t2(angle : float) -> float: 
    val = math.degrees(angle)
    return clamp(val, 0, 180) 

def t3(angle : float) -> float:
    val = math.degrees(angle)
    #res = (360 + val)
    #res = - val + math.degrees(offset_angle)
    res = - val
    return  clamp(res, 0, 180)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

x = 9.73
y = 0
z = 19

# Função para calculo da cinematica inversa do manipulador
def processInverseKinematics(desiredPos : list[float]):
    
    # Coordenadas da posição desejada 
    global x, y, z
    x = desiredPos[0]
    y = desiredPos[1]
    z = desiredPos[2] - 8.5

    x = x - (l3 * math.cos(phi))
    z = z - (l3 * math.sin(phi))

    #print(x, y, z)
    
    
    try:
        # CALCULANDO ROTAÇÃO DA BASE
        # - Obtendo "novo x"
        new_x = math.sqrt(x**2 + y**2) 
        #new_x = new_x - (l3 * math.cos(phi))

        # - Calculando ângulo de rotação da junta da base
        theta_0 = math.asin(y/new_x)
        
        # CALCULANDO ROTAÇÃO DO BRAÇO 
        # - Obtendo theta 1
        theta_1_1 = math.atan2(z, new_x) 
        theta_1_2 = math.acos((new_x**2 + z**2 + d2**2 - d3**2)/(2*d2*math.sqrt(new_x**2 + z**2)))
        theta_1 = theta_1_1 + theta_1_2
        
        # - Obtendo theta 2
        theta_2 = math.acos((new_x**2 + z**2 - d2**2 - d3**2)/(2*d2*d3))

        # - Obtendo theta 3 
        theta_3 = phi - (theta_1 - theta_2)
        print(math.degrees(theta_3), t3(theta_3), new_x, y, (z + 8.5), math.degrees(phi)) 

        return [t0(theta_0), t1(theta_1), t2(theta_2), t3(theta_3), 0, 0]

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

    #print(jointPositions, x, y, z)