"""
装饰器实际应用
在python实现类方法
使用classmethod的时候需要cls参数
使用staticmethod的时候不需要cls参数
"""


class MyClass:
    @classmethod
    def max(cls, x, y):
        """
        cls 表示该方法是个类方法
        :param x:
        :param y:
        :return: x y 之间的最大值
        """
        return x if x > y else y

    @staticmethod
    def getMin(x, y):
        return x if x < y else y

    def fuc(self):
        return 'hello world'


if __name__ == '__main__':
    value = MyClass.max(3, 4)
    print(value)
    value = MyClass.getMin(-2, 10)
    print(value)
