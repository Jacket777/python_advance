"""
装饰器参数--更加灵活
"""
import functools
import json

import functools
import json


class JSONOutputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# TODO 1 函数当作装饰器使用
def json_output(decorated=None, indent=None, sort_keys=False):
    """
    Return the decorated function,serialize the result of that function to JSON,and return the JSON string
    :param indent:
    :param sort_keys:
    :return:
    """
    # 如果被修饰的方法和参数，则报错
    if decorated and (indent or sort_keys):
        raise RuntimeError("Unexpected arguments.")

    # Define the actual decorator function
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

    if decorated:
        return actual_decorator(decorated)
    else:
        return actual_decorator


# TODO 2 装饰器应用
@json_output
def do_nothing():
    return {'status': 'done'}


@json_output(indent=4, sort_keys=True)
def do_something():
    return {'code': '200'}


if __name__ == '__main__':
    print(do_nothing())
    print("========================")
    print(do_something())
