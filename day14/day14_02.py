# Encoding  =  utf-8

import sys

def gradeDrv():
    count = 1
    grades = []
    sum = 0
    while True:
        print('请输入第', count, '位同学的成绩：', end='')
        grade = input()
        if grade == 'exit':
            break
        else:
            try:
                grades.append(float(grade))
            except:
                print('输入的成绩为非数字，请重新输入')
                count -= 1
        count += 1
    for i in grades:
        sum += i
    try:
        avg = sum / len(grades)
    except BaseException as e:
        e_type,e_value,e_trance = sys.exc_info()
        return('成绩列表为空：',e_value)

    return avg


if __name__ == '__main__':
    if isinstance(gradeDrv(),float):
        print('平均成绩是：', gradeDrv())
    else:
        print(gradeDrv())