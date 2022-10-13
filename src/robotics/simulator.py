from ctypes import sizeof
import socket
import array
import struct
import sys
from tkinter.messagebox import RETRY
import numpy as np 

JOINT_COUNT = 4
host, port = "127.0.0.1", 25001
unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect() -> None: 
    unitySocket.connect((host, port))

def sendJointData(motorPos: np.ndarray = None, fk_pos : array = None, ik_pos : array = None) -> None:
    
    # Conferindo se valores de posição foram passados
    if (fk_pos == None):
        fk_pos = [0,0,0]
    if (ik_pos == None):
        ik_pos = [0,0,0]

    # Convertendo array de float para array de inteiros
    positions = [0, 0, 0, 0, 0, 0]
    for n in range(len(motorPos)):
        positions[n] = int(motorPos[n])

    # Adicionando posições (CONVERTER VALOR DAS POSICOES)
    positions += fk_pos
    positions += ik_pos

    # Convertendo posições para valor em byte
    # IMPORTANTE: VALORES ENVIADOS DE 0 A 255
    byte_msg = bytearray(positions)
    unitySocket.send(byte_msg)

def sendFloatData(number : float) -> None: 
    byte_array = bytearray(struct.pack("f", number))
    unitySocket.send(byte_array)

def sendArmData(fk_pos : list[float] = None, ik_pos : array = None, motorPos : array = np.tile(np.float32(90), 6)) -> None:

    # Definindo valores de posicoes cinematica direta e inversa 
    if (fk_pos == None):
        fk_pos = [0.1,0.1,0.1]

    if (ik_pos == None):    
        ik_pos = [0.1, 0.1, 0.1]

    positions = [0, 0, 0, 0, 0, 0]
    for n in range(len(motorPos)):
        positions[n] = motorPos[n]

    # Adicionando informações de cinematica 
    positions += fk_pos
    positions += ik_pos

    #print(positions)

    # Declarando array que armazenará valores em bytes 
    byte_array = bytearray(48)

    # Convertendo valores de float para byte
    for x in range(len(positions)):
        struct.pack_into("f", byte_array, (x*4), positions[x])

    # Enviando dados 
    unitySocket.send(byte_array)

def getData() -> list[float]:
    
    # Recebendo dados de posição do simulador em bytes
    receiveData = unitySocket.recv(4*4)

    # Declarando array de floats 
    jointPos = [0.1, 0.1, 0.1, 0.1]
    lastPos = 0

    # Convertendo array de bytes em array de floats 
    for x in range(JOINT_COUNT):
        
        # Dividindo buffer de entrada em subarray a cada numero 
        subBytes = bytearray(4)
        for i in range(JOINT_COUNT):
            subBytes[i] = receiveData[lastPos]
            lastPos += 1

        tupleNum = struct.unpack('f', subBytes)
        floatNum = tupleNum[0]
        jointPos[x] = floatNum

    return jointPos