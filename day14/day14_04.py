# Encoding = utf-8


def inputStudent():
    stu = []
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    if not (age.isnumeric()) or int(age)< 0 or int(age) > 200:
        e = stuException('001', '学生年龄不合法:%s' % (age))
        raise e
    id = input('请输入学号：')
    if len(id) != 10 or not (id.isnumeric()):
        e = stuException('002', '学生学号不合法:%s(学号限为纯10位数字)' % (id))
        raise e
    sex = input('请输入性别：')
    if sex not in ('男', '女'):
        e = stuException('003', '学生性别不合法:%s' % (sex))
        raise e
    stu.append([id,name,age,sex])
    return stu


class stuException(Exception):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __str__(self):
        return self.code +':'+ self.msg


if __name__ == '__main__':
    try:
        stuList = inputStudent()
        for stu in stuList:
            print(stu)
    except BaseException as e:
        print(e)