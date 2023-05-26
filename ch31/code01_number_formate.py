"""
1.2 数字格式化输出
"""

x = 1234.56789


def test01():
    print(f'0.2f   format {x}: {x:0.2f}')  # 不指定宽度，小数位保留2 位  1234.57
    print(f'>10.1f format {x}: {x: >10.1f}')  # 指定宽度为10，小数位保留1 位，靠后显示
    print(f'<10.1f format {x}: {x: <10.1f}')  # 指定宽度为10，小数位保留1 位，靠前显示
    print(f'^10.1f format {x}: {x: ^10.1f}')  # 指定宽度为10，小数位保留1 位，居中显示
    print(f',      format {x}: {x: ,}')  # 设置千分位符号  1,234.56789
    print(f'0,.1f  format {x}: {x: 10,.1f}')  # 设置千分位符号,小数位保留1 位  1,234.6,靠后显示


def test02():
    print(f'e    format {x} is: {x: e}')
    print(f'0.2E format {x} is: {x: 0.2E}')  # 保留小数点两位


def test03():
    print(f'The value is：{x: 0,.2f}')


def test04():
    print(f'x  format: {x: 0.1f}')
    print(f'-x format: {-x: 0.1f}')


"""
交换千分位
"""


def test05():
    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))  # 1.234,56789


if __name__ == '__main__':
    test05()
