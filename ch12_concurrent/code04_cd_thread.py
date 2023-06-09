"""
通过继承构造线程类
"""
import time
from threading import Thread


class CountdownThread(Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print(f'T-minus: {self.n}')
            self.n -= 1
            time.sleep(5)


if __name__ == '__main__':
    c = CountdownThread(5)
    c.start()
