"""
1.3 进制转换
"""

x = 1234


def test01():
    print(f'binary of {x}: {bin(x)}')  # 显示 0b10011010010
    print(f'octal of {x}: {oct(x)}')   # 显示 0o2322
    print(f'hexadecimal of {x}: {hex(x)}')  # 显示 0x4d2


def test02():
    print(f'binary not show 0b: {x:b}')  # 显示 0b10011010010
    print(f'octal not show 0b: {x:o}')   # 显示 2322
    print(f'hexadecimal not show 0b: {x:x}')  # 显示 4d2


def test03():
    y = -1234
    print(f'binary of {y}: {y:b}')  # 显示 -10011010010
    print(f'hexadecimal of {y}: {y:x}')  # 显示 -4d2


def test04():
    print(f'(2**32+x) binary result: {2**32+x:b}')  # 显示 100000000000000000000010011010010
    print(f'(2**32+x) hexadecimal result: {2 ** 32 + x:x}')  # 显示 1000004d2


def test05():
    print(int('4d2', 16))  # 显示  1234
    print(int('10011010010', 2))  # 显示  1234


if __name__ == '__main__':
    test05()