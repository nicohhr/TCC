from cmath import cos
from math import cos, sin, radians
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