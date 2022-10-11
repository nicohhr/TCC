import socket 
import time 

host, port = "127.0.0.1", 25001
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.connect((host, port))

while True:
    # Envio
    time.sleep(0.5)
    mySocket.send(("180").encode("UTF-8"))
    
    # Recepção 
    receivedData = mySocket.recv(1024).decode("UTF-8")
    print(receivedData) 
    
