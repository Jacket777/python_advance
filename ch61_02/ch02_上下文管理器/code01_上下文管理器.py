"""
上下文管理器
"""
class ContextManager(object):
    def __init__(self):
        self.entered = False

    def __enter__(self):
        self.entered = True
        return self

    def __exit__(self, exc_type, exc_instance, traceback):
        """
        :param exc_type:  异常类型
        :param exc_instance: 异常实例
        :param traceback: 回溯选择
        :return:
        """
        self.entered = False