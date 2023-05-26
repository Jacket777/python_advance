"""
线程的启动与停止
"""
import time
from threading import Thread


def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


if __name__ == '__main__':
    t = Thread(target=countdown, args=(3,))
    # 后台进程---会在主线程终止时自动销毁
    # t = Thread(target=countdown,args=(10,),daemon=True)
    t.start()
    """注意加入后，主线程会等待该线程结束后终止"""
    # t.join()

    if t.is_alive():
        print('Still running')
    else:
        print('Completed')
    time.sleep(10)
    print("主线程结束运行.....")
