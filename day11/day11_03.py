# Encoding = utf -8
#冒泡排序
'''
外循环条件长度减一
内循环条件长度减一减外循环
循环体比较大小交换位置
'''

def order(list1):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]

if __name__ == '__main__':
    list1 = [4,3,2,5,6,3,2,6,8]
    order(list1)
    for i in list1 :
        print (i,end='  ')