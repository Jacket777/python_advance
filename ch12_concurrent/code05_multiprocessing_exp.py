import multiprocessing
import time
from threading import Thread


class CountdownTask:
    def __init__(self):
        """设置线程是否运行标志位--私有变量"""
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print(f'T-minus: {n}')
            n -= 1
            time.sleep(5)


if __name__ == '__main__':
    c = CountdownTask()
    p = multiprocessing.Process(target=c.run,args=(3,))
    p.start()


