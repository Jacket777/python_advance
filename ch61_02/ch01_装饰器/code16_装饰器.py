"""
任务执行器装饰器
"""

class Task(object):
    """
    定义一个任务类，该类中有一一个run方法，用来执行任务
    """
    def __call__(self, *args, **kwargs):
        print("============================")
        return self.run(*args, **kwargs)

    def run(self, *args, **kwargs):
        raise NotImplementedError('Subclasses must implement run.')

    def identify(self):
        return 'I am  a task'


# TODO 1 装饰器用来修饰类
def task(decorated):
    """返回一个类，该类执行给定的方法，如果它的run方法被调用"""
    class TaskSubclass(Task):
        def run(self, *args, **kwargs):
            return decorated(*args, **kwargs)
    return TaskSubclass()

@task
def foo():
    return 2+2

result = foo()
print(result)


print(foo.identify())