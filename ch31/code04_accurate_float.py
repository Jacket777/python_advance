"""
1.4.2 浮点数运算
"""

from decimal import Decimal
from decimal import localcontext
import math


def test01():
    a = 2.1
    b = 4.2
    print(a + b)  # 显示 6.300000000000001


def test02():
    a = Decimal('2.1')
    b = Decimal('4.2')
    print(f'a + b = {a + b}')  # 显示 6.3




def test03():
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(f'a / b = {a / b}')  # 显示 0.7647058823529411764705882353
    with localcontext() as ctx:
        ctx.prec = 3  # 设置精度
        print(f'a / b = {a / b}')  # 显示 0.765

    with localcontext() as ctx:
        ctx.prec = 50
        print(f'a / b = {a / b}')  # 显示 0.76470588235294117647058823529411764705882352941176


num_list = [1.23e+18, 1, -1.23e+18]


def test04():
    print(f'sum result is: {sum(num_list)}')  # 显示 0.0


def test05():
    print(f'math sum result: {math.fsum(num_list)}')  # 显示 1.0


if __name__ == '__main__':
    test05()