# Encoding = utf-8

def testIO():
    userInfo = open('../text/userInfo.text','r+')
    str1 = userInfo.readlines()
    print('***',str1)
    userInfo.write('xxxxxx\n')
    #str1 = userInfo.readlines()
    #print('***', str1)
    userInfo.close()



if __name__ == '__main__':
    testIO()