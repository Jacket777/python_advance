"""
简单装饰器使用：
执行时封装代码
类型检查，确保函数所接收的所有参数都是整型，否则报错
"""


def requires_ints(decorated):
    """
    :param decorated: 被装饰的可以调用方法
    :return: 新的可调用函数
    """
    def inner(*args, **kwargs):
        print("---------test-----------------")
        # 遍历参数a=1,b=2形式的参数
        kwarg_values = [i for i in kwargs.values()]
        for arg in list(args) + kwarg_values:
            if not isinstance(arg, int):
                raise TypeError("%s only accepts integers as arguments." % decorated.__name__)
        return decorated(*args, **kwargs)
    return inner


@requires_ints
def sum_integer(x, y):
    """
    :param x:
    :param y:
    :return: the sum of x and y
    """
    return x + y


def test01():
    # 注意此时方法名称已经改变
    help(sum_integer)
    # 装饰器开始检查
    sum_integer(2, 56)
    # 装饰器开始检查, 类型不符合，报错
    sum_integer(2.6, 56)



if __name__ == '__main__':
    test01()
