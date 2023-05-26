"""
装饰器应用初步
函数注册表
"""

registry = []  # 定义一个函数注册列表，用于存放函数


# TODO 1 定义一个装饰器，用于将函数存放到函数注册列表中，并返回原函数
def register(decorated):
    """
    :param decorated: 装饰函数
    :param registry:  函数注册表
    :return:
    """
    registry.append(decorated)
    return decorated


# TODO 2 使用装饰器，将该函数注册到注册表中
@register
def foo():
    return 3

# TODO 3 使用装饰器，将该函数注册到注册表中
@register
def bar():
    return 5


# TODO 测试函数注册表--遍历函数注册表并执行
def test():
    answers = []
    for func in registry:
        answers.append(func())
    print(answers)


if __name__ == '__main__':
    test()
