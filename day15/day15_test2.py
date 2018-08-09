# encoding = utf-8

# 网络通讯实现UDP的聊天

import threading
import socket
import sys


class Mic(threading.Thread):
    def __init__(self, targetIP, targetPort):
        threading.Thread.__init__(self)
        self.targetIP = targetIP
        self.targetPort = targetPort
        self.sendSorcket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def run(self):
        while True:
            msg = input('请输入信息内容：')
            if msg == 'bye':
                sys.exit()
            self.sendSorcket.sendto(msg.encode(encoding='utf-8'), (self.targetIP, self.targetPort))


class Speaker(threading.Thread):
    def __init__(self, bindIP, bindPort):
        threading.Thread.__init__(self)
        self.bindIP = bindIP
        self.bindPort = bindPort
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__socket.bind((self.bindIP, self.bindPort))

    def run(self):
        while True:
            data, attr = self.__socket.recvfrom(1024)
            data = data.decode('utf-8')
            print(data)


class Pthone(threading.Thread):
    def __init__(self, mic, speaker):
        threading.Thread.__init__(self)
        self.__mic = mic
        self.__speaker = speaker

    def run(self):
        self.__mic.start()
        self.__speaker.start()


if __name__ == '__main__':
    m1 = Mic('localhost', 9999)
    s1 = Speaker('localhost', 8888)
    p1 = Pthone(m1, s1)
    m2 = Mic('localhost', 8888)
    s2 = Speaker('localhost', 9999)
    p2 = Pthone(m2, s2)
    p1.start()
    p2.start()
