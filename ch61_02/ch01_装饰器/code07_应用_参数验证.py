"""
简单装饰器使用：
注意比较
保存帮助信息
"""
import functools


def requires_ints(decorated):
    """
    :param decorated: 被装饰的可以调用方法
    :return: 新的可调用函数   @functools.wraps 用于显示函数的核心信息
    """
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        kwarg_values = [i for i in kwargs.values()]
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError("%s only accepts integers as arguments." % decorated.__name__)
        return decorated(*args, **kwargs)
    return inner


@requires_ints
def foo(x, y):
    """
    :param x:
    :param y:
    :return: the sum of x and y
    """
    return x + y


help(foo)

# print(foo(5.3,6))
