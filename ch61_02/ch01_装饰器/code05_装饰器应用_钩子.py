"""
装饰器
应用钩子
"""


# TODO 1 编写注册表类
class Registry(object):
    def __init__(self):
        """
        初始化时，定义一个函数列表
        """
        self.functions = []

    # 作用就是一个装饰器--本质上就是将函数添加到函数列表中
    def register(self, decorated):
        """
        将被装饰的函数，添加到函数列表中
        :param decorated: 被装饰的函数
        :return: 被装饰的函数
        """
        self.functions.append(decorated)
        return decorated

    @classmethod
    def add_info(cls, decorated):
        decorated.__doc__ = "test class method doc"
        return decorated

    def run_all(self, *args, **kwargs):
        """ 执行函数列表中的函数，注意需要参数"""
        return_values = []
        for func in self.functions:
            return_values.append(func(*args, **kwargs))
        return return_values

    def display_all(self):
        """显示函数的说明文档"""
        for func in self.functions:
            print(func.__doc__)


# TODO 2 定义两个注册表
a = Registry()
b = Registry()


# TODO 3 注册到a注册表中
@Registry.add_info
@a.register
def foo(x=3):
    """foo function"""
    return x


# TODO 4 注册到b注册表中
@b.register
def bar(x=5):
    """bar function"""
    return x


# TODO 4 注册到a, b注册表中
@a.register
@b.register
def baz(x=7):
    print("baz function")
    return x


def test():
    # TODO 5 执行注册表中的方法，并返回结果
    print("a 注册表中的函数")
    value_list = a.run_all()
    print(value_list)
    a.display_all()
    print("b 注册表中的函数")
    # TODO 6 执行注册表中的方法，并返回结果
    value_listb = b.run_all()
    print(value_listb)
    print(a.run_all(x=4))


if __name__ == '__main__':
    test()
