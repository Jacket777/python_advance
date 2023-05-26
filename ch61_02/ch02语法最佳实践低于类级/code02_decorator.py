# 装饰器的作用

def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper


@debug
def say_hello(something):
    print("hello  {}".format(something))
    print("=============================")


if __name__ == '__main__':
    say_hello("jack")
