"""
装饰器原理解析与简单应用
"""


# TODO 1 装饰器方法
def decorated_by(func):
    """
    :param func: 被装饰的函数
    :return: 返回装饰过的函数
    """
    func.__doc__ += '\nDecorated by decorated_by function'
    return func


# TODO 2 被装饰的函数
def add(x, y):
    """Return the sum of x and y"""
    return x + y


# TODO 3 测试未被装饰过的函数与装饰过的函数区别
def test01():
    print("未被装饰器修饰过的函数")
    help(add)
    print("被装饰器修饰过的函数")
    add2 = decorated_by(add)
    help(add2)


# TODO 实际使用规范
@decorated_by
def minus(x, y):
    """Return the minus x and y"""
    return x if x < y else y


def minus2(x, y):
    """Return the minus x and y"""
    return x if x < y else y


def test02():
    print("测试标准使用规范效果")
    help(minus)
    print("测试基本原理演示")
    min = decorated_by(minus2)
    help(min)


if __name__ == '__main__':
    test02()
