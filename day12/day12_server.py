# Encoding = utf-8

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
mySocket, addr = s.accept()#监听
while True:
    myData = mySocket.recv(1024)
    print(addr)
    if myData.decode('utf-8') == 'bye':
        break
    else:
        print(myData.decode('utf-8'))
        serStr = input('服务器')
        mySocket.send((serStr.encode(encoding='utf-8')))