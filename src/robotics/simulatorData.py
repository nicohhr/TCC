import socket
import array
import struct
import numpy as np 

host, port = "127.0.0.1", 25001
unitySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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

def receiveSimData() -> array:
    receivedData = unitySocket.recv(1024).decode("UTF-8")
    print(receivedData) 

def sendArmData(fk_pos : array = None, ik_pos : array = None, motorPos : array = np.tile(np.float32(90), 6)) -> None:

    # Definindo valores de posicoes cinematica direta e inversa 
    if (fk_pos == None) and (ik_pos == None):
        fk_pos = [88,77,99]
        ik_pos = [66,55,44]

    positions = [0, 0, 0, 0, 0, 0]
    for n in range(len(motorPos)):
        positions[n] = motorPos[n]

    # Adicionando informações de cinematica 
    positions += fk_pos
    positions += ik_pos

    print(positions)

    # Declarando array que armazenará valores em bytes 
    byte_array = bytearray(48)

    # Convertendo valores
    for x in range(len(positions)):
        struct.pack_into("f", byte_array, (x*4), positions[x])

    # Enviando dados 
    unitySocket.send(byte_array)



    
    