"""
1.4.1 四舍五入运算
"""


def test01():
    print(round(1.23, 1))     # 显示 1.2
    print(round(1.28, 1))     # 显示 1.3
    print(round(-1.27, 1))    # 显示 -1.3
    print(round(1.25361, 3))  # 显示 1.254


def test02():
    a = 1627731
    print(round(a, -1))  # 显示 1627730
    print(round(a, -2))  # 显示 1627700
    print(round(a, -3))  # 显示 1628000


def test03():
    x = 1.23456
    print(f'{x: 0.2f}')  # 显示 1.23
    print(f'{x: 0.3f}')  # 显示 1.235


def test04():
    a = 2.1
    b = 4.2
    c = a + b
    print(c)              # 显示 6.300000000000001
    print(round(c, 2))    # 显示 6.3


if __name__ == '__main__':
    test04()
