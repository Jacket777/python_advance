"""
*args 说明
作用 1： 打包，在函数定义时，使用*, 实际调用的过程中，将多个参数打包成一个元组
作用 2： 分包，在函数实际调用中使用*将参数中元组或列表分拆为单个参数

"""


# TODO 1 打包参数
def test01(*args):
    for i in args:
        print(i)
    print(type(args))


def test02(a, *args):
    print('a:', a)
    print('args:', args)
    for i in args:
        print(i)
    print(type(args))


def test03(a, b, *args):
    print('a:', a)
    print('b:', b)
    print('args:', args)
    for i in args:
        print(i)
    print(type(args))



#TODO 2 拆分参数
def test04(a, b, c):
    print(a)
    print(b)
    print(c)



if __name__ == '__main__':
    test04(*(1, 2, 3))
    #test04(*[1, 2, 3, 4]) # 报错

