import collections
from functools import reduce
import dis

a = lambda x: x ** 2

print(a(2))

a = map(lambda x: x ** 2, [2, 4, 6, 8])

print(isinstance(a, collections.abc.Generator))
print(isinstance(a, collections.abc.Iterator))
print([x for x in a])
a = list(map(lambda x: x ** 2, [2, 4, 6, 8]))

b = list(filter(lambda x: x % 2 == 0, [2, 4, 6, 8, 9, 11]))
print(b)

print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))

print(reduce((lambda x, y: x * y), [2, 3, 3, 3]))


def func1(n, y):
    return n ** y


func2 = lambda x: x ** 2

dis.dis(func1)
dis.dis(func2)


print((lambda x: (x % 2 and 'odd' or 'even'))(3))


f = (lambda a, b: a > b and a or b)

print(f(15, 10))

print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow', 'fox', 'volf']))

print((lambda acc, x: f'{acc} | {x}')(5, 2))

print(reduce(func1, [2, 2, 2]))

print(reduce((lambda x, y: x * y), [1, 2, 3, 4]))

print(reduce((lambda x, y: x * y), [2, 3, 3, 3]))


_dict = {'a': 75, 'b': 11, 'v': 28, 'c': 36}
print(list(_dict))
print(_dict)
print(sorted(_dict))
print(sorted(_dict, key=lambda x: _dict[x]))


value_ = (lambda aa: aa**2)
print(value_(5))