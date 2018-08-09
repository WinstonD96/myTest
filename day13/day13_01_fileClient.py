# Encoding = utf-8

import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('localhost',9999))
    fileName = input('输入要传输的文件:')
    file = open(fileName, 'rb')
    fileList = fileName.split('/')
    for fileInfo in fileList:
        if fileInfo.rfind('.text'):
            fileNameInfo = fileInfo
    print(fileNameInfo)
    fileNameInfo += '\n'
    s.send(fileNameInfo.encode(encoding='utf-8'))
    while True:
        oldFile = file.read(512)
        if oldFile:
            s.send(oldFile)
        else:
            break
    file.close()
    s.close()