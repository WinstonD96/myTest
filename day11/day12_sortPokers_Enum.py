# Encoding = utf-8
from enum import Enum, unique
from day11.day11_02 import *

# 将扑克牌花色转为枚举类
@unique
class suitsEnum(Enum):
    黑桃 = 1
    梅花 = 2
    红桃 = 3
    方块 = 4


# 将扑克牌点数转为枚举类
@unique
class dotNumEnum(Enum):
    J = 11
    Q = 12
    K = 13
    A = 14
   # 2 = 15
    小 = 16
    大 = 17

#判断点数是否需要转换为枚举类型
def giveDot(pokerDot):
    if pokerDot in ('3','4','5','6','7','8','9','10'):
        return int(pokerDot)
    elif pokerDot == '2':

        return 15
    elif pokerDot in ('J','Q','K','A','小','大'):
        return dotNumEnum[pokerDot].value


# 比较扑克大小
def comparePoker(poker1, poker2):
    result = 0
    poker1dot = giveDot(poker1.num)
    poker2dot = giveDot(poker2.num)
    result = poker1dot - poker2dot
    if result == 0:
        poker1suit = suitsEnum[poker1.suits].value
        poker2suit = suitsEnum[poker1.suits].value
        result = int(poker2suit) - int(poker1suit)
    return result


# 通过冒泡排序比较大小
def sortPokers(pokers):
    for i in range(len(pokers) - 1):
        for j in range(len(pokers) - 1 - i):
            if comparePoker(pokers[j], pokers[j + 1]) < 0:

                pokers[j], pokers[j + 1] = pokers[j + 1], pokers[j]

