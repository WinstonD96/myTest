# Encoding = utf-8

import _thread, time, threading


# def testThread(name, count):
#     for a in range(count):
#         print(name, a)
#         time.sleep(1)


class MyThread(threading.Thread):
    def __init__(self, tname, count):
        threading.Thread.__init__(self)
        self.tname = tname
        self.count = count

    def run(self):
        for a in range(self.count):
            print(self.tname,'-->', a)
            time.sleep(1)


if __name__ == '__main__':
    t1 = MyThread('zhangsan', 10);
    t2 = MyThread('lisi', 10);

    t1.start()
    t2.start()
    # a = 0
    # _thread.start_new_thread(testThread, ('Thread1', 10))
    # _thread.start_new_thread(testThread, ('Thread2', 10))
