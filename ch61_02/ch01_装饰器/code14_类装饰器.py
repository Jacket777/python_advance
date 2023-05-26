"""
类装饰器
"""

import functools
import time


def sortable_by_creation_time(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.__created = time.time()

    cls.__init__ = new_init

    cls.__lt__ = lambda self, other: self.__created < other.__created
    cls.__gt__ = lambda self, other: self.__created > other.__created

    return cls


@sortable_by_creation_time
class Sortable(object):
    def __init__(self, identifier):
        self.identifier = identifier

    def __repr__(self):
        return self.identifier

first  = Sortable('first')
second = Sortable('second')
third = Sortable('third')

sortables = [second, first, third]
sorted(sortables)
