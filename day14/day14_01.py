# Encoding = utf-8
import sys,traceback

if __name__ == '__main__':
    list = [1,2]
    try:
        print(list[2])
    except IndexError as e:
        print(e)
        e_type, e_value, e_traceback = sys.exc_info()
        print(e_type, '', e_value)
        traceback.print_tb(e_traceback, file=sys.stdout)

    print('超出下标');