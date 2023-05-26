"""
说明：列表推导
"""


# TODO 1.获取0-9中偶数 比较差的代码实现
def test01():
    numbers = range(10)
    size = len(numbers)
    evens = []
    i = 0
    while i < size:
        if i % 2 == 0:
            evens.append(i)
        i += 1
    print(evens)


# TODO 2.获取0-9中偶数 最佳实践代码--列表推导
def test02():
    evens = [i for i in range(10) if i % 2 == 0]
    print(evens)


# TODO 3. 将列表转为字典
def test03():
    i = 0
    seq = ["one", "two", "three"]
    for element in seq:
        seq[i] = '%d : %s' % (i, element)
        i += 1
    print(seq)


# TODO 4. 使用enumerate内部函数
def test04():
    seq = ["one", "two", "three"]
    list02 = enumerate(seq)  # 返回的是enumerate类对象
    print(type(enumerate(seq)))
    print(list(list02))  # 转为list之后，list列表中元素为元组
    for i, element in list02:
        seq[i] = '%d : %s' % (i, element)
    print(seq)


def treatment(pos, element):
    return '%d: %s' % (pos, element)


def sample03():
    seq = ["one", "two", "three"]
    result = [treatment(i, element) for i, element in enumerate(seq)]
    print(result)


if __name__ == '__main__':
    test04()