"""
4.1.5 迭代器切片
"""

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
print(c[5: 8])

import itertools
# for x in itertools.islice(c, 5, 8):
#     print(f'iter val is: {x}')
