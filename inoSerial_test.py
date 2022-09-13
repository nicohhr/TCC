from ast import Try
from turtle import delay
import serial 
import time 

serialObj = serial.Serial() # Selecionando porta serial 

# Definindo propriedades 
serialObj.baudrate = 9600
serialObj.port = 'COM5'
serialObj.open()

# Teste: Enviando letra A

print("CTRL + C para finalizar...")

motor_positions = [120, 90, 45, 30, 100, 180]
byte_msg = bytearray(motor_positions)

cnt = 0

try:
    while True:

        serialObj.write(byte_msg)
        time.sleep(0.05)

        if serialObj.in_waiting: 
            packet = serialObj.readline()
            print(packet.decode())
            
except: 
    serialObj.close()