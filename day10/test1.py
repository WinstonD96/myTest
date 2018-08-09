# Encoding = utf-8
# 限制属性

class Student():
    def __init__(self):
        self.__id = '1111111111'
        self.__name = 'asdf'
        self.__sex = '男'
        self.__iNum = '1234567890098'
        self.__email = '1@.com'

    def set_id(self, id):
        if id.isnumeric() and len(id) == 10:
            self.__id = id
        else:
            print('输入有误，学号必须时一个10位的纯数字！')

    def get_id(self):
        return self.__id

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_sex(self, sex):
        if sex == '男' or sex == '女':
            self.__sex = sex
        else:
            print('性别输入有误，必须是男或女')

    def get_sex(self):
        return self.__sex

    def set_iNum(self,iNum):
        if iNum.isnumeric() and len(iNum) == 13:
            self.__iNum = iNum
        else:
            print('输入有误，电话号码必须是一个13位的纯数字')

    def get_iNum(self):
        return self.__iNum

    def set_email(self,email):
        if email.find('@')!=-1 and email.endswith('.com'):
            self.__email = email
        else:
            print('输入有误，邮箱中必须包含@且以.com结尾')
    def get_email(self):
        return self.__email


if __name__ == '__main__':
    stu1 = Student()
    print(len('123456789'))
    print()
    stu1.set_id('123456789')
    stu1.set_name('dwj')
    stu1.set_sex('男')
    stu1.set_iNum('123456789012')
    stu1.set_email('@.com')
    print(stu1.get_id(),stu1.get_name(),stu1.get_iNum(),stu1.get_sex(),stu1.get_email())