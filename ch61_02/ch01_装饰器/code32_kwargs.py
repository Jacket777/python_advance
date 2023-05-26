"""
**kwargs 作用
打包: 把多个关键字打包成一个字典
拆包：把字典的键值拆分单个的，依次赋值给函数的形参
"""


# TODO 1 打包
def test01(**kwargs):
    print(kwargs)

# TODO 2 拆包
def test02(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    print("打包，将多个形参关键字打包成一个字典")
    test01(a=1, b=2, c=3)
    print("拆包")
    test02(**{'a': 1, 'b': 2, 'c': 3})
