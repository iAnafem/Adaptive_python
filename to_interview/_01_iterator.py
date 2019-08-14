import collections


class MyIterator(collections.abc.Iterator):
    def __init__(self, collection, cursor):
        self.collection = collection
        self.cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor + 1 >= len(self.collection):
            raise StopIteration
        self.cursor += 1
        return self.collection[self.cursor]

    def first(self):
        self.cursor = -1


class MyIterable(collections.abc.Iterable):
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return MyIterator(self.collection, -1)


agregate = MyIterable(list(range(15)))

for i in agregate:
    print(i, end=' ')

c = MyIterator
# or

itr = iter(agregate)

while True:
    item = next(itr, None)
    if item is None:
        break
    print(item, end=' ')

print()

a = list(range(15))
b = MyIterator(a, -1)


for i in b:
    print(i, end=" - ")

b.first()

for i in b:
    print(i, end=" + ")


print(type(b))

print(iter(range(10)))

a = iter(range(10))

print(isinstance(a, collections.abc.Iterator))
print(isinstance(range(10), collections.abc.Iterator))
print(isinstance(a, collections.abc.Generator))
print(isinstance(range(10), collections.abc.Generator))

