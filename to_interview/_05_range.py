import collections
from collections.abc import Sequence



# range is iterable. We can call the iter() func:
a = iter(range(10))

print(a)


print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))


# but eange is not an iterator! We cannot call next on a range object.


try:
    print(next(range(10)))
except:
    print("no!")

# object range is a "lazy sequence" They’re sequences (like lists, tuples, and strings)
# but they don’t really contain any memory under the hood and instead answer questions computationally.

print(isinstance([1, 2], Sequence))  # return True

print(isinstance('hello', Sequence))  # return True

print(isinstance(range(3), Sequence))  # return True

print(isinstance(range(3), collections.abc.Iterator))  # return False

a = range(10)

print(a)
print(type(a))

c = iter(a)

print(next(c))

print('loop')

for i in c:
    print(i)

for i in c:
    print(i)

b = iter(range(10))


def my_range(stop, start=0, inc: float = 1):
    while start < stop:
        yield start
        start += inc


a = my_range(10)
print(a)
for i in a:
    print(i)

a = my_range(10, start=1, inc=0.5)

for i in a:
    print(i)


a = my_range(10, start=1, inc=2)

for i in a:
    print(i)


