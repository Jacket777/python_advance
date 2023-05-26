"""
装饰器应用：输出格式化
"""
import functools
import json


def json_output(decorated):
    """
    Run the decorated function, serialize the result of that function to JSON,
    and return the JSON string
    :param decorated:the method by decorated
    :return:
    """
    @functools.wraps(decorated)
    def inner(*args, **kwargs):
        result = decorated(*args, **kwargs)
        return json.dumps(result)
    return inner


@json_output
def do_nothing():
    return {'status': 'done'}


if __name__ == '__main__':
    print(do_nothing())
