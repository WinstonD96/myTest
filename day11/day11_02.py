# Encoding = utf-8
import random
#from day11.day11_sortPoker import *
from day11.day12_sortPokers_Enum import *


# 斗地主


# 玩家(账号 昵称 密码) 身份 金币 等级  手上的牌
#        叫地主 明牌  加倍 出牌
class Player(object):
    def __init__(self):
        self.__username = ''
        self.__identity = ''
        self.__gold = 500
        self.__grade = 0
        self.__pokers = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def identity(self):
        return self.__identity

    @identity.setter
    def identity(self, value):
        self.__identity = value

    @property
    def gold(self):
        return self.__gold

    @gold.setter
    def gold(self, value):
        self.__gold = value

    @property
    def grade(self):
        self.grade

    @grade.setter
    def grade(self, value):
        self.grade = value

    @property
    def pokers(self):
        return self.__pokers

    @pokers.setter
    def pokers(self, value):
        self.__pokers

    def jiaoDizhu(self):
        result = False;
        return result;

    def mingPoker(self):
        result = False;
        return result;

    def double(self):
        result = 1;
        return result;

    def outPokers(self, pokers):
        # 手上的，包含在pokers中清除
        pass;

    def appendPoker(self, pokers):
        if not self.__pokers or not isinstance(self.__pokers, list):
            self.__pokers = []
        self.__pokers.append(pokers)

    def orderPoker(self, pokers):
        sortPokers(pokers)
        # sortPokers(pokers)


# 扑克（ 花色 牌面）
class Pokers():
    __slots__ = ('__suits', '__num')

    def __init__(self, suits, num):
        self.__suits = suits
        self.__num = num

    def __str__(self):
        return self.__suits + self.__num

    @property
    def suits(self):
        return self.__suits

    @suits.setter
    def suits(self, value):
        if value in ('黑桃', '梅花', '红桃', '方块', '王'):
            self.__suits = value
        else:
            raise ValueError('扑克花色不合法！')

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, value):
        if value in ('A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', '大', '小'):
            self.__num = value
        else:
            raise ValueError('扑克字面不合法')


# 荷官 ( 洗牌 发牌 顺序 判断合法 判断大小  判断胜负)
class Croupier():
    # 创建一副新牌
    def createPoker(self):
        pokers = []
        for i in ('黑桃', '梅花', '红桃', '方块'):
            for j in ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'):
                poker = Pokers(i, j)
                pokers.append(poker)
        pokers.append(Pokers('王', '大'))
        pokers.append(Pokers('王', '小'))
        return pokers

    # 洗牌
    def shuffle(self, pokers):
        count = 0
        while count < 100:
            a = random.randint(0, 53)
            b = random.randint(0, 53)
            pokers[a], pokers[b] = pokers[b], pokers[a]
            count += 1

    # 发牌
    def licensing(self, pokers):
        hand1, hand2, hand3, hand4 = [], [], [], []
        count = 1
        for poker in pokers:
            if (count - 1) % 3 == 0 and count < 52:
                hand1.append(poker)
            elif (count - 2) % 3 == 0 and count < 52:
                hand2.append(poker)
            elif count % 3 == 0 and count < 52:
                hand3.append(poker)
            elif count > 51:
                hand4.append(poker)
            count += 1

        return hand1, hand2, hand3, hand4

    # 出牌顺序
    def orderPokers(self):
        result = 'A'
        return result
                                                        
    # 判断出牌是否合法
    def outValidity(self, pok1):
        result = True
        return result

    # 比较牌面大小
    def comparePokers(self, pok1, pok2):
        result = True
        return result

    # 判断胜负
    def gameResult(self, play1):
        result = True
        return result


if __name__ == '__main__':
    croupier = Croupier()
    pokers = croupier.createPoker()

    croupier.shuffle(pokers)

    p1, p2, p3, p4 = croupier.licensing(pokers)
    play1 = Player()
    play1.username = '玩家1'
    play2 = Player()
    play2.username = '玩家2'
    play3 = Player()
    play3.username = '玩家3'
    print('开始游戏')
    play1.orderPoker(p1)
    play1.pokers = p1
    print(play1.username, '的手牌有：')
    for i in p1:
        print(i, end=',')
    play2.orderPoker(p2)
    play2.pokers = p2
    print()
    print(play2.username, '的手牌有：')
    for i in p2:
        print(i, end=',')
    play3.orderPoker(p3)
    play3.pokers = p3
    print()
    print(play3.username, '的手牌有：')
    for i in p3:
        print(i, end=',')
