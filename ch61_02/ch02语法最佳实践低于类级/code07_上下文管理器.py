'''
上下文管理器模拟
'''

class MyOpen(object):
    '''path 文件路径  mode 类型'''
    def __init__(self, path, mode):
        self.__path = path
        self.__mode = mode

    def __enter__(self):
        print("代码执行到__enter__......")
        # 打开文件
        self.__handle = open(self.__path, self.__mode)
        # 返回打开的文件对象的引用，用来给as 后的变量f赋值
        return self.__handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("代码执行到__exit__......")
        self.__handle.close()




def test01():
    print("使用with作为上下文管理器")
    with open("E:\\test.txt",'a+') as f:
        f.write("test python\n")
        print("写入成功")


def test02():
    with MyOpen("E:\\test.txt",'a+') as f:
        f.write("hello world\n")
        print("自定义写入成功")



class MyCount(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __enter__(self):
        print("代码执行到__enter__......")
        return self

    # exc_type 异常类型
    # exc_val 异常值
    # exc_tb  异常回溯追踪
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("代码执行到了__exit__......")
        if exc_type == None:
            print("程序没问题")
        else:
            print("程序有问题， 如果能看懂，问题如下: ")
            print('Type:', exc_type)
            print('Value:',exc_val)
            print('TraceBack:',exc_tb)
        # 返回值决定了捕获的异常是否继续向外抛出
        # 如果是False，那么就会继续向外抛出，程序会看到系统提示的异常信息
        # 如果是True， 不会向外抛出，程序看不到系统提示信息，只能看到else中的输出
        return False

    def div(self):
        print("代码执行到了除法 div")
        return self.__x/self.__y


def test03():
    # TODO 1 正常执行
    with MyCount(20,2) as mc:
        mc.div()
    # TODO 2 异常执行
    print("=====================")
    with MyCount(20,0) as mc:
        mc.div()



if __name__ == '__main__':
    # test02()
    test03()



