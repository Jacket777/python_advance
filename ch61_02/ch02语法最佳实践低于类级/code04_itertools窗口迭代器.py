"""itertools 模块中迭代器"""
import itertools
"""
1.窗口迭代器
2.往返式迭代器 tee(iterator, count)
3.


"""


#TODO 1.窗口迭代器 islice
def starting_at_five():
    print("Please input the info")
    value = input().strip()
    print("value = "+value)
    while value != '':
        for el in itertools.islice(value.split(), 4, None):
            yield el
        print("Please input the info again")
        value = input().strip()

#TODO 2. 窗口迭代器 改进 islice
def start_five():
    list01 = ['one', 'two','three','four','five','six']
    while len(list01) >= 4:
        for el in itertools.islice(list01, 4, None):
            yield el
        list01 = list01[2:] + list01[:2]



def sample_01():
    iter01 = starting_at_five()
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())


def sample_02():
    iter01 = start_five()
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())
    print(iter01.__next__())





if __name__ == '__main__':
   pass
