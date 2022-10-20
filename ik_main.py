import math 
from src.robotics import simulator 

# Definindo tamanho dos elos [cm]
d1 = 8.444
d2 = 10.5
d3 = 9.72
d4 = 2.8
d5 = 5.0

# Função para calculo da cinematica inversa do manipulador
def processInverseKinematics(desiredPos : list[float]) -> list[float]:
    
    # Coordenadas da posição desejada 
    x = desiredPos[0]
    y = desiredPos[1]
    z = desiredPos[2]

    # CALCULANDO ROTAÇÃO DA BASE
    # - Obtendo "novo x"
    new_x = math.sqrt(x**2 + y**2)

    # - Calculando ângulo de rotação da junta da base
    theta_0 = math.asin(y/new_x)

    # CALCULANDO ROTAÇÃO DO BRAÇO 
    # - Obtendo theta 1
    theta_1_1 = math.atan2(new_x, y) 
    theta_1_2 = math.acos((x**2 + y**2 + d2**2 - d3**2)/(d2*math.sqrt(new_x**2 + y**2)))
    theta_1 = theta_1_1 + theta_1_2

    # - Obtendo theta 2
    theta_2 = math.acos((new_x**2 + y**2 - d2**2 - d3**2)/(2*d2*d3))

    # Exibindo resultados
    print("theta0:", math.degrees(theta_0),"theta1:", math.degrees(theta_1), "theta2:", math.degrees(theta_2))
    
    return [theta_0, theta_1, theta_2, 90, 0, 0]

# Conectando com o simulador
simulator.connect()

while True: 

    # Recebendo dados
    endPos = simulator.getData(3)

    # Posição de juntas calculado
    jointPositions = processInverseKinematics(endPos)

    # Enviando dados
    simulator.sendArmData(motorPos=jointPositions)

    print(jointPositions)