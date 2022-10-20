import math 

# Funções de conversão
def t0(angle : float) -> float:
    return 90 - math.degrees(angle)

def t1(angle : float) -> float:
    return math.degrees(angle)

def t2(angle : float) -> float: 
    return 180 - math.degrees(angle)


# Definindo coordenadas desejadas
x = 15
y = 5
z = -5 - 8.5

# Tamanho dos elos [cm] 
d1 = 8.5
d2 = 10.5
d3 = 10.2
d4 = 2.6
d5 = 16.5

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

print("t0:", t0(theta_0))
print("t1:", t1(theta_1))
print("t2:", t2(theta_2))
