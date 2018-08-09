# encoding = utf-8
from enum import *

# month = Enum('month',('Jan','Feb'))
#
# month1 = month.Jan
# print(month1)

def menuPoker():
    suits = Enum('花色',('红桃','黑桃','梅花','方块'))
    suit = suits.黑桃
    print('*******',suit)
    print(suits)
    print(dir(suits))
    print(suits.__members__)
    for i,j in suits.__members__.items():
        print(i,j)

class enum(Enum):
    pass


if __name__ == '__main__':

    for i in range(10):
        print(i)
