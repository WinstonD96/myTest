# Encoding = utf-8

def copyFile():
    oldFile = open('../text/userInfo.text','rb')
    newFile = open('../text/newFile2.text','wb')
    try:
        oldStr = oldFile.read(10)
        while oldStr != b'':
            newFile.write(oldStr)
            oldStr = oldFile.read(10)
    finally:
        oldFile.close()
        newFile.close()

if __name__ == '__main__':
    copyFile()