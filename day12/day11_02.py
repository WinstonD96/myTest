# Encoding = utf-8

# Animal = type('Animal', (), {'name': 'hello'})
# animal = Animal()
# print(animal.name)


def add():
    print('测试成功')


class Animal(type):
    def __new__(cls, name, bases, attrs):
        attrs['name'] = '动物'
        attrs['addMethod'] = add
        return type.__new__(cls, name, bases, attrs)


class Cat(object, metaclass=Animal):
    def __init__(self):
        add()
        self.color = '黄色'


cat = Cat()
# print(cat.name, '******', cat.color)
