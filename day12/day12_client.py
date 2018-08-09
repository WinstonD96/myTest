# Encoding = utf-8
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',9999))
while True:
    cliStr = input('客户端：')

    s.send(cliStr.encode(encoding='utf-8'))

    data = s.recv(1024)
    if data.decode('utf-8') == 'bye' or cliStr == 'bye' :
        break
    else:
        print(data.decode('utf-8'))
