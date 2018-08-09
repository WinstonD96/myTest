# Encoding = utf-8

import time, threading


def testThread(threadName, count, myLock):
    myLock.acquire()  # 上锁
    for i in range(count):
        print(threadName, '-->', i)
        time.sleep(1)

    myLock.release()


if __name__ == '__main__':
    myLock = threading.Lock()
    t1 = threading.Thread(target=testThread, args=('thread1', 5, myLock))
    t2 = threading.Thread(target=testThread, args=('thread2', 5, myLock))
    t1.start()
    t2.start()


