# Encoding = utf-8

import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.bind(('localhost',8888))
    data = 'hi,i am cilent'
    s.sendto(data.encode(encoding='utf-8'),('localhost',9999))

    data, attr = s.recvfrom(1024)
    print(data)