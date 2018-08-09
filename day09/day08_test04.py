# Encoding = utf-8

class studentInfo():
    def __init__(self, id, username, xingming, sex, age, iNum, email):
        self.id = id
        self.username = username
        self.xingming = xingming
        self.sex = sex
        self.age = age
        self.iNum = iNum
        self.email = email


def inputStuInfo():
    count = 0

    while 0 < 10:

        id = input('第', count, '位同学的学号：')
        username = input('第', count, '位同学的用户名：')
        xingming = input('第', count, '位同学的姓名：')
        sex = input('第', count, '位同学的性别：')
        age = input('第', count, '位同学的年龄：')
        iNum = input('第', count, '位同学的手机号码：')
        email = input('第', count, '位同学的学号邮箱：')
        userInfo = id + username + xingming + sex + age + iNum + email
        count += 1
        return userInfo


if __name__ == '__main__':
    pass
