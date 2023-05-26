"""
生成器
基于yield指令，使得函数暂停，并返回中间结果,此时函数的类型转为generator类型
"""
import tokenize

"""生成器模式"""
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def sample_01():
    fib = fibonacci()
    print(type(fib))
    print(fib.__next__())
    print(fib.__next__())
    print(fib.__next__())
    fia = fibonacci()
    result = [fia.__next__() for i in range(10)]
    print(result)



#TODO 标准库中tokenize模块将在文本之外生成令牌，并且针对每个处理过的行返回一个迭代器，---有问题
def sample_01B():
    reader = open('code02_iterator.py').__next__()
    tokens = tokenize.generate_tokens(reader)
    tokens.__next__()


#TODO 生成器嵌套使用
def power(values):
    for value in values:
        print('powering %s' % value)
        yield value


def adder(values):
    for value in values:
        print('adding to %s' % value)
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2


def sample_02():
    elements = [1, 4, 7, 9, 12, 19]
    res = adder(power(elements))
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    print(res.__next__())
    # print(res.__next__())


#TODO 生成器特性： 与next方法调用的代码进行交互的功能，此时yield变成一个表达式
#使用send与它交互，此时yield将变成能够返回传入的值
def psychologist():
    print("Please tell me your problem")
    while True:
        answer = (yield)
        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much question")
            elif 'good' in answer:
                print("A that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")


def sample_03():
    free = psychologist()
    free.__next__()
    print('I free bad')
    free.send('I free bad')
    print("--------------------")
    print("Why I shouldn't?")
    free.send("Why I shouldn't?")
    print("--------------------")
    print("ok then i should find what is good for me")
    free.send("ok then i should find what is good for me")



#TODO 典型生成器模板
def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exception'
    finally:
        print("ok, let's clean")



def sample_04():
    gen = my_generator()
    print(gen.__next__())
    print("--------------------")
    result = gen.throw(ValueError('mean mean mean'))
    print(result)
    print("-------2.>>>>>-------------")
    # 关闭之后再也无法使用生成器
    gen.close()
    print("------3.->>>>>-------------")


#TODO 生成器表达式
def sample_05():
    iter02 = (x**2 for x in range(10) if x % 2 == 0)
    for el in iter02:
        print(el)


if __name__ == '__main__':
    sample_05()

