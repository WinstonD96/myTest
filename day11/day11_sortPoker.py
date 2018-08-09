# Encoding = utf-8
from day11.day11_02 import *


# 将扑克进行排序
# 先将点数和花色int化
# 然后通过冒泡排序比较点数和花色大小进行降序排序

# 将点数int化
def dotNumInt(dotNum):
    if dotNum in ('3', '4', '5', '6', '7', '8', '9', '10'):
        return int(dotNum)
    elif dotNum == 'J':
        return 11
    elif dotNum == 'Q':
        return 12
    elif dotNum == 'K':
        return 13
    elif dotNum == 'A':
        return 14
    elif dotNum == '2':
        return 15
    elif dotNum == '小':
        return 16
    elif dotNum == '大':
        return 17


# 将花色int化
def suitsInt(suits):
    if suits == '黑桃':
        return 4
    elif suits == '梅花':
        return 3
    elif suits == '红桃':
        return 2
    elif suits == '方块':
        return 1


# 比较扑克大小
def comparePoker(poker1, poker2):
    result = 0
    poker1dot = dotNumInt(poker1.num)
    poker2dot = dotNumInt(poker2.num)
    result = poker1dot - poker2dot
    if result == 0:
        poker1suit = suitsInt(poker1.suits)
        poker2suit = suitsInt(poker2.suits)
        result = poker1suit - poker2suit
    return result


# 通过冒泡排序比较大小
def sortPokers(pokers):
    for i in range(len(pokers) - 1):
        for j in range(len(pokers) - 1 - i):
            if comparePoker(pokers[j], pokers[j + 1]) < 0:
                pokers[j], pokers[j + 1] = pokers[j + 1], pokers[j]

    return pokers
