# Encoding = utf-8

class Fib():
    def __getitem__(self, item):
        a = b = 1
        for c in range(item):
            a, b = b, a + b
        return a

    def __getattr__(self, item):
        if item == 'test':
            return 10

if __name__ == '__main__':
    fib = Fib()
    a = 0

    while a < 10:
        print(fib[a])
        a+= 1
    print(fib.test)