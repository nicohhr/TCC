from ast import Try
from turtle import delay
import serial 
import time 

serialObj = serial.Serial('COM5') # Selecionando porta serial 

# Definindo propriedades 
serialObj.baudrate = 9600
serialObj.bytesize = serial.EIGHTBITS     # Numero de bits com data
serialObj.parity = serial.PARITY_EVEN     # Sem paridade
serialObj.stopbits = serial.STOPBITS_ONE  

time.sleep(3)

# Teste: Enviando letra A

print("CTRL + C para finalizar...")

try:
    while True:
        serialObj.write(b'A')
        time.sleep(1)
except:
    serialObj.close()         # Fechando porta serial

