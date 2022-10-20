from ctypes import sizeof
import socket
import array
import struct
import sys
from tkinter.messagebox import RETRY
import numpy as np 

host, port = "127.0.0.1", 25001
unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect() -> None: 
    unitySocket.connect((host, port))

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

def getData(dataSize : int) -> list[float]:
    
    # Recebendo dados da posição XYZ desejada em bytes 
    try:
        receiveData = unitySocket.recv(dataSize*4)
    except:
        print("Connection with simultor not possible.")
        return [0.1 for i in range(dataSize)] 
    
    #Convertendo array de bytes em array de floats
    return floats2bytes(dataSize, receiveData)

def floats2bytes(number_amount : int, received_data : bytes, ) -> list[float]:
    
    # Declarando array de saida
    resultData = [0.1 for i in range(number_amount)] 
    lastPos = 0

    # Convertendo array de bytes em array de floats 
    for x in range(number_amount):
        
        # Dividindo buffer de entrada em subarray a cada numero 
        subBytes = bytearray(4)
        for i in range(4):
            subBytes[i] = received_data[lastPos]
            lastPos += 1

        tupleNum = struct.unpack('f', subBytes)
        floatNum = tupleNum[0]
        resultData[x] = floatNum
    
    return resultData
