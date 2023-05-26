"""
类装饰器--不太好的应用，好的看code16
"""


# TODO 1 任务类的基类，它本身不能运行run方法，必须依靠子类运行
class Task(object):
    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement run.')

    def identify(self):
        """
        标识实例身份
        :return: 字符串
        """
        return 'I am  a task'


#TODO 2 定义装饰器
def task(decorated):
    """
    :param decorated: 被修饰的函数
    :return:一个Task子类，如果它的run方法被调用，它则会运行被修饰的函数
    """
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass

@task
def foo():
    return 2 + 2


f = foo()
print(f.run())
print(f.identify())



