# Encoding = utf-8
# 动物园

class Felidae():
    def __init__(self):
        self.__name = '猫科动物'
        self.__color = '颜色'
        self.__eat = '吃'
        self.__crow = '叫'

    def eat(self):
        print(self.__name, self.__eat)

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_eat(self, eat):
        self.__eat = eat

    def get_eat(self):
        return self.__eat

    def set_crow(self, crow):
        self.__crow = crow

    def get_crow(self):
        return self.__crow


class Cat(Felidae):
    def paShu(self):
        print(self.get_name(), '会爬树')


class Tiger(Felidae):
    pass


class peacock():
    __slots__ = ('__name', '__color')

    age = 20

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def name(self):
        self.__sex = '母'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

class Fib(object):
    def __init__(self):
        self.__a, self.__b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.__a, self.__b = self.__b,self.__a+self.__b
        if self.__a>10000:
            raise StopIteration()
        return self.__a

class fish(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'fish name %s' %self.name

if __name__ == '__main__':

    f = fish('小鱼')
    f

    # for i in Fib():
    #     print(i)
    # p = peacock()
    # p.name = '孔雀'
    # p.color = '绿'
    # print(p.name)
    # print(p.color)
    # p.sex
    # cat = Cat()
    # tiger = Tiger()
    # cat.set_name('猫')
    # tiger.set_name('老虎')
    # cat.set_eat('吃猫粮')
    # tiger.set_eat('吃肉')
    # cat.paShu()
    # cat.eat()
    # tiger.eat()
