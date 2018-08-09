# Encoding  = utf-8

import socket

if __name__ == '__main__':
    # 创建socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定IP和端口号
    s.bind(('localhost', 9999))
    # 设置信道数
    s.listen(5)
    # 设置监听
    mySocket, attr = s.accept()
    fileDizi = input('接收文件地址:')
    fileInfo = ''
    while True:
        newFile = mySocket.recv(512)
        newFile = newFile.decode('utf-8')
        if newFile:
            fileInfo += newFile
        else:
            break
    list1 = fileInfo.split('\n')
    print(list1)
    a = 1
    newFileInfo = ''
    for list2 in list1:
        if a == 1:
            fileName = list1[0]
        elif a > 1:
            print(list2)
            newFileInfo += list2
        a += 1
    print('使用原有的文件名1，使用新的文件名2')
    chioce = input('-->')
    if chioce == '2':
        fileName = input('输入新的文件名：')
    fileDizi += fileName
    print(fileDizi)
    file = open(fileDizi, 'wb')
    file.write(newFileInfo.encode(encoding='utf-8'))
    mySocket.close()
    file.close()
    s.close()
