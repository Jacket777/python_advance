"""
装饰器参数
"""

import functools
import json


class JSONOutputError(Exception):
    """
    定义异常类
    """

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# TODO 1 函数当作装饰器使用
def json_output(indent=None, sort_keys=False):
    """
    Return the decorated function,serialize the result of that function to JSON,and return the JSON string
    :param indent: 缩进位置
    :param sort_keys:是否排序控制
    :return:
    """

    def actual_decorator(decorated):
        @functools.wraps(decorated)
        def inner(*args, **kwargs):
            try:
                result = decorated(*args, **kwargs)
            except JSONOutputError as ex:
                result = {
                    'status': 'error',
                    'message': str(ex),
                }
            return json.dumps(result, indent=indent, sort_keys=sort_keys)

        return inner

    return actual_decorator


# TODO 2 装饰器应用
@json_output(indent=5, sort_keys=True)
def do_something():
    return {'status': 'done', "code": 200}


# TODO 3 装饰器应用 无参
@json_output()
def do_nothing():
    return {'status': 'finished', "code": 400}


if __name__ == '__main__':
    print("测试缩进与排序.......无参")
    print(do_nothing())
    print("测试缩进与排序.......有参")
    print(do_something())
