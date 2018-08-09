# Encoding = utf-8

import threading, socket, sys


class Phone():
    def __init__(self, name, bindIP, bindPort, sendIP, sendPort):
        threading.Thread.__init__(self)
        self.name = name
        self.bindIP = bindIP
        self.bindPort = bindPort
        self.sendIP = sendIP
        self.sendPort = sendPort
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.bindIP, int(self.bindPort)))

def main():
    name = input('请输入手机名：')
    bindIP = input('请输入本地ip：')
    bindPort = input('请输入本地端口：')
    sendIP = input('请输入目标IP：')
    sendPort = input('请输入目标端口：')
    p1 = Phone(name, bindIP, bindPort, sendIP, sendPort)
    return p1

p1 = main()

def send():
    while True:
        msg = input('%s，请输入发送内容：' % (p1.name))
        if msg == 'bye':
            sys.exit()
        p1.sock.sendto(msg.encode(encoding='utf-8'), (p1.sendIP, int(p1.sendPort)))


def recv():
    while True:
        data, addr = p1.sock.recvfrom(1024)
        data = data.decode('utf-8')
        print(addr, '发来消息：', data)


if __name__ == '__main__':
    s1 = threading.Thread(target=send)
    r1 = threading.Thread(target=recv)
    s1.start()
    r1.start()
