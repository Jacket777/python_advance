"""
装饰器--日志管理
"""
import functools
import logging
import time


def logged(method):
    @functools.wraps(method)
    def inner(*args, **kwargs):
        start = time.time()
        return_value = method(*args, **kwargs)
        end = time.time()
        delta = end - start
        logger = logging.getLogger('decorator.logged')
        # %r 万能的格式付
        logger.warning('Called method %s at %.02f; execution time %.02f second; result %r.'
                    '' % (method.__name__, start, delta, return_value))
        return return_value
    return inner

@logged
def sleep_and_return(return_value):
    time.sleep(2)
    return return_value


if __name__ == '__main__':
    sleep_and_return(20)


