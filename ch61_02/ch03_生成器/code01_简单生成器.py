"""
简单生成器
"""

def fibonacci():
    yield 1
    yield 1
    yield 2
    yield 3
    yield 5
    yield 8

for i in fibonacci():
    print(i)