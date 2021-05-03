import socket 

client = socket.socket()
port = 1234
servername = '192.168.1.129'

client.connect((servername, 1234))
while True:
    data = input('>')
    
    if not data:
        break
    client.send(data.encode())
    data = client.recv(1024).decode()
    #if  not data
    #break
    print(data)
