"""
定义： tee(iterator, count)
说明： iterator  迭代器， count 整数
返回值：返回参数中提到的迭代器数量
"""
from itertools import tee, islice

#TODO 1. 简单使用
def sample01():
    list01 = [0, 1, 2, 3, 4]
    iterator = iter(list01)
    a, b = tee(iterator, 2)
    print(list(a))
    print(list(b))
    c, d = tee(['a','b','c','d'], 2)
    print(type(c))
    print(list(c))
    print(list(d))


def with_head(iterable, headsize=1):
    a, b = tee(iterable)
    print(type(a))
    print(type(b))
    return list(islice(a, headsize)), list(b)

def sample_02():
    seq = ['one', 'two', 'three', 'four', 'five']
    print(with_head(seq,24))


if __name__ == '__main__':
    sample_02()
