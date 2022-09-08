from cmath import cos
from math import cos, sin, radians
from scipy.spatial.transform import Rotation as R 
import numpy as np

def Rx(angle:int | float) -> np.array: 
    '''
    Calcula matriz de rotação em relação ao eixo X da referência. 

    Parameters
    ----------
    - angle: int | float 
        ângulo de rotação 
    
    Returns
    -------
    - numpy.array:
         matriz de rotação em relação a X 
    '''

    matrix = np.array([[1,                   0,                    0, 0], 
                       [0, cos(radians(angle)), -sin(radians(angle)), 0],
                       [0, sin(radians(angle)), cos(radians(angle)),  0],
                       [0,                   0,                   0,  1]])

    return matrix 

def Ry(angle:int | float) -> np.array: 
    '''
    Calcula matriz de rotação em relação ao eixo Y da referência. 

    Parameters
    ----------
    - angle: int | float 
        ângulo de rotação 
    
    Returns
    -------
    - numpy.array:
         matriz de rotação em relação a Y 
    '''

    matrix = np.array([[cos(radians(angle)) , 0, sin(radians(angle)), 0], 
                       [0                   , 1,                   0, 0],
                       [-sin(radians(angle)), 0, cos(radians(angle)), 0],
                       [0,                   0,                   0,  1]])

    return matrix

def Rz(angle:int | float) -> np.array: 
    '''
    Calcula matriz de rotação em relação ao eixo Z da referência. 

    Parameters
    ----------
    - angle: int | float 
        ângulo de rotação 
    
    Returns
    -------
    - numpy.array:
         matriz de rotação em relação a Z 
    '''

    matrix = np.array([[cos(radians(angle)) , -sin(radians(angle)), 0, 0], 
                       [sin(radians(angle)) , cos(radians(angle)) , 0, 0],
                       [0                   , 0                   , 1, 0],
                       [0                   , 0                   , 0, 1]])

    return matrix

def Trans(x: int | float, y: int | float, z: int | float) -> np.array: 
    '''
    Calcula matriz de translação aplicada a mais de um eixo de referência 
    de maneira simultânea. 

    Parameters -> Distâncias transladadas
    ----------
    - x: int | float 
    - y: int | float
    - z: int | float
    
    Returns
    -------
    - numpy.array:
         matriz de translação com as medidas desejadas
    '''

    matrix = np.array([[1, 0, 0, x],
                       [0, 1, 0, y],
                       [0, 0, 1, z], 
                       [0, 0, 0, 1]])

    return matrix

def Tx(d: int | float) -> np.array: 
    '''
    Calcula matriz de translação referente ao eixo X

    Parameters 
    ----------
    - d: int | float 
        Distância transladada
    
    Returns
    -------
    - numpy.array:
         matriz de translação em relação a X
    '''

    matrix = np.array([[1, 0, 0, d],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0], 
                       [0, 0, 0, 1]])

    return matrix

def Ty(d: int | float) -> np.array: 
    '''
    Calcula matriz de translação referente ao eixo Y

    Parameters 
    ----------
    - d: int | float 
        Distância transladada
    
    Returns
    -------
    - numpy.array:
         matriz de translação em relação a Y
    '''

    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, d],
                       [0, 0, 1, 0], 
                       [0, 0, 0, 1]])

    return matrix

def Tz(d: int | float) -> np.array: 
    '''
    Calcula matriz de translação referente ao eixo Z

    Parameters 
    ----------
    - d: int | float 
        Distância transladada
    
    Returns
    -------
    - numpy.array:
         matriz de translação em relação a Z
    '''

    matrix = np.array([[1, 0, 0, 0],
                       [0, 1, 0, 0],
                       [0, 0, 1, d], 
                       [0, 0, 0, 1]])

    return matrix

def denavit(a: int | float, alfa: int | float, d: int | float, teta: int | float) -> np.array:
    '''
    Calcula transformada homogênea de um elo a partir dos parâmetros de Denavit-Hartenberg fornecidos.

    Parameters 
    ----------
    - a: int | float - 
        Distância entre z medida no eixo x
    - alfa: int | float -
        Angulo entre z medido no eixo x
    - d: int | float -
        Distância entre x medida no eixo z
    - teta: int | float -
        Angulo entre x medido no eixo z
    
    Returns
    -------
    - numpy.array:
         matriz de translação em relação a Z
    '''

    # Convertendo angulos de graus para radianos
    alfa_r = radians(alfa)
    teta_r = radians(teta)

    matrix = np.array([[cos(teta_r), -cos(alfa_r)*sin(teta_r), sin(alfa_r)*sin(teta_r), a*cos(teta_r)],
                       [sin(teta_r), cos(alfa_r)*cos(teta_r), -sin(alfa_r)*cos(teta_r), a*sin(teta_r)],
                       [0          , sin(alfa_r)            , cos(alfa_r)             , d            ],
                       [0          , 0                      , 0                       , 1            ]])

    return matrix