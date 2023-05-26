# yield的使用
from inspect import isgeneratorfunction
import types
from collections import Iterable


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1


# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n = n + 1
#     return L


# class Fab:
#     def __init__(self, max):
#         self.max = max
#         self.n, self.a, self.b = 0, 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < self.max:
#             print("------>>>>>>>---------")
#             result = self.b
#             self.a, self.b = self.b, self.a + self.b
#             self.n = self.n + 1
#             return result
#         raise StopIteration()


def fab(value):
    n, a, b = 0, 0, 1
    while n < value:
        yield b
        print("==========", b)
        a, b = b, a+b   # 后面的a+b 是原来的a,而不是赋值之后的a, b也是原来的b，不是赋值之后的b
        n = n + 1


def read_file(path):
    BLOCK_SIZE = 1024
    with open(path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if block:
                yield block
            else:
                return


if __name__ == '__main__':
    # fab(5)
    # for n in fab(5):
    #     print(n)
    # for n in Fab(5):
    #     print(n)
    # for n in fab(5):
    #     print(n)
    f = fab(5)
    # result = f.__next__()
    # print(result)
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # print(f.__next__())
    # 判断一个函数是否是一个特殊的generator 函数
    result = isgeneratorfunction(fab)
    print("是否为generator函数:", result)

    result = isinstance(fab, types.GeneratorType)
    print("是否为Generator类型实例： ", result)
    result = isinstance(fab(5), types.GeneratorType)
    print("是否为Generator类型实例： ", result)
    # 是否为可迭代的
    result = isinstance(fab, Iterable)
    print("是否为可迭代的: ", result)
    result = isinstance(fab(5), Iterable)
    print("是否为可迭代的: ", result)
    f = read_file("E:\ABC.txt")
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())
    print(f.__next__())


    # print(type(fab3))
    # print(type(fab3(5)))
    # print(type(range(10)))
    # for i in range(10):
    #     print(i)
    # a = range(10)
    # print(a)
    # print(type(xrange(10)))
    # print(isgeneratorfunction(fab3))
    # print(isinstance(fab3, types.GeneratorType))
    # print(isinstance(fab3(5), types.GeneratorType))
    # print(isinstance(fab3, Iterable))
    # print(isinstance(fab3(5), Iterable))
