"""
装饰器应用--异常自定义与抛出
"""
import functools
import json

# TODO 1 定义JSON异常
class JSONOutputError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


# TODO 2 输出格式化装饰器
def json_output(decorated):
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        try:
            result = decorated(*args, **kwargs)
        except JSONOutputError as ex:
            result = {
                'status': 'error',
                'message': str(ex),
            }
        return json.dumps(result)
    return inner


@json_output
def error():
    raise JSONOutputError("This function is erratic.")


@json_output
def other_error():
    raise ValueError("The grass is always greener")



if __name__ == '__main__':
    error()
    print("=================")
    print(other_error())
