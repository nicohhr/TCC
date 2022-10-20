import math

# Definindo coordenadas desejadas
x = 8 
y = 3
z = 5

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
theta_1_1 = math.atan2(new_x, z) 
theta_1_2 = math.acos((x**2 + z**2 + d2**2 - d3**2)/(d2*math.sqrt(new_x**2 + z**2)))
theta_1 = theta_1_1 + theta_1_2

# - Obtendo theta 2
theta_2 = math.acos((new_x**2 + z**2 - d2**2 - d3**2)/(2*d2*d3))

# Exibindo resultados
print("theta0:", math.degrees(theta_0),"theta1:", math.degrees(theta_1), "theta2:", math.degrees(theta_2))