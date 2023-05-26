import reprlib
import pprint
import textwrap
import locale

# reprlib.repr(set(’super’))

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t)

doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines.
"""

print(textwrap.fill(doc, width=40))

locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()
x = 1234567.8
number = locale.format_string("%d", x, grouping=True)
print(number)
result = locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'],x), grouping=True)
print(result)


