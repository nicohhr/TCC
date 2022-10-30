import math 
from math import degrees

# Definindo tamanho dos elos [cm]
d1 = 8.444
d2 = 10.5
d3 = 9.72
d4 = 2.8
d5 = 5.0
l3 = 3.9

# Posição desejada
x = 10
y = 0 
z = 10 - 8.5

# Angulo da ferramenta em relação a superficie 
phi = math.radians(-135)

x = x - (l3 * math.cos(phi))
z = z - (l3 * math.sin(phi))

print(l3 * math.cos(phi))
print(l3 * math.sin(phi))

print("-------------------")

print("x (theta 3) ->", x)
print("z (theta 3) ->", z)

new_x = math.sqrt(x**2 + y**2)
print("new_x (pos j1 rotation) ->", new_x)
theta_0 = math.asin(y/new_x)

theta_1_1 = math.atan2(z, new_x) 
theta_1_2 = math.acos((new_x**2 + z**2 + d2**2 - d3**2)/(2*d2*math.sqrt(new_x**2 + z**2)))
theta_1 = theta_1_1 + theta_1_2
#theta_1_neg = theta_1_1 - theta_1_2
print("theta 0:", 90 - degrees(theta_0))
print("theta 1:", degrees(theta_1))

theta_2 = math.acos((new_x**2 + z**2 - d2**2 - d3**2)/(2*d2*d3))
print("theta_2:", degrees(theta_2))

theta_3 = phi - (theta_1 - theta_2)
print("theta_3:", -degrees(theta_3))
