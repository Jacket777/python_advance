"""
groupby: uniq迭代器

可以对来自一个迭代器的重复元素进行分组，只要是相邻的
它还可以提供另一函数来执行元素比较，否则采用表示符比较
"""
from itertools import groupby


# 1. 压缩数据----返回的是一个generator
def compress(data):
    return ((len(list(group)), name) for name, group in groupby(data))


# 2. 解压数据
def decompress(data):
    # result = ''
    # for size, car in data:
    #     print(size, car)
    #     print(size*car)
    #     result = result.join(size*car)
    #     print(result)
    return (car*size for size, car in data)
    # return result


def sample_01():
    compressed = compress('get uuuuuuuuuuuuuuuuuuuuuuuuuuuuupuuuuuuuabc')
    print("-----------------------")
    list01 = list(decompress(compressed))
    print(list01)
    print("".join(list01))
    # print("".join(list(decompress(compressed)))) 这种方法不可以打印出来
    print("----------------")
    result = decompress(compressed)
    print("".join(result))


def test01():
    list01 = ['g', 'e', 't', ' ', 'uuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'p', 'uuuuuuu', 'a', 'b', 'c']
    print(''.join(list01))


if __name__ == '__main__':
    sample_01()
    # test01()
