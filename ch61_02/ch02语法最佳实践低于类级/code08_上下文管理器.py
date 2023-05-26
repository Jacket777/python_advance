'''
使用类库提供的上下文管理器
'''
from contextlib import contextmanager

class MyResource:
    def query(self):
        print("query data")


@contextmanager
def make_myresource():
    print('start to connect')
    yield MyResource()
    print("end connect")
    pass


if __name__ == '__main__':
    with make_myresource() as r:
        r.query()
    