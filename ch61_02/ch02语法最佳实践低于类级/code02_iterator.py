"""
迭代器
说明：迭代器是一个实现迭代器协议的容器， 它基于两个方法
1.next 返回容器中下一个元素
2.__iter__: 返回迭代器本身
迭代器生成：两个元素
1.内建函数 iter
2.一个序列

与生成器

"""

def sample01():
    result = iter('abc')
    print(result.__next__())
    print(result.__next__())
    print(result.__next__())
    """下一个将报异常 StopIteration"""
    print(result.__next__())


class MyIterator:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        """return the next element"""
        if self.step == 0:
            raise StopIteration
        self.step -= 1
        return self.step

    def __iter__(self):
        """return the iterator itself"""
        return self


def sample02():
    for el in MyIterator(4):
        print(el)


class MyIterator2:
    def __init__(self, step):
        self.step = step

    def __next__(self):
        if self.step - 1< 0:
            raise StopIteration
        self.step -= 2
        print("==============")
        return self.step

    def hasNext(self):
        if self.step > 0:
            return True
        else:
            return False

    def __iter__(self):
        return self

def sample03():
    it = MyIterator2(10)
    for i in it:
        print(i)
    # while(it.hasNext()):
    #     print(it.next())


if __name__ == '__main__':
    sample03()