class FibonacciGenerator:
    def __init__(self):
        self.prev = 0
        self.cur = 1

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        return result

    def __iter__(self):
        return self


def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


for i in FibonacciGenerator():
    print("tyt", i)

    if i > 10000:
        break

for i in fibonacci():
    print(i)

    if i > 100:
        break


def fib(num):
    if num == 0:
        return 0
    elif num == 1 or num == 2:
        return 1
    else:
        return fib(num - 2) + fib(num - 1)


for i, j in enumerate(range(10)):
    print("fib" + str(i) + " = ", fib(i))


fib2 = fibonacci()

for i in range(10):
    print(next(fib2))

fibo = {0: 0, 1: 1}


def fib_dynamic(num):
    if num in fibo:
        return fibo[num]
    else:
        temp_fib = fib_dynamic(num - 2) + fib_dynamic(num - 1)
        fibo[num] = temp_fib
        return temp_fib


print(fib_dynamic(9))
print(fibo)
print(fib_dynamic(15))
print(fibo)
print(fib_dynamic(25))
print(fibo)
print(fib_dynamic(20))
print(fibo)


a = fibonacci()
for i, num in enumerate(a):
    print(f'{i} fibonacci = {num}')
    if i > 9:
        break


def my_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


x = my_generator(10)

for i in x:
    print(i)

L = ["Roger", "Nadal", "Novac", "Andre", "Sarena", 4, 6, 7, 8, 8, 9, 90, 3, 4, 6, 8]

a = ((lambda b, d: b ** d)(x, y) for y, x in enumerate(L) if type(x) is not str and x % 2 == 0)

print('lol', a)
for i in a:
    print(i)


def fib5(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib5(n-2) + fib5(n-1)


print("fib5 = ", fib5(9))

print(fib_dynamic(0))





a, b ,c = (i for i in range(3))

print(a, b, c)

f, *g ,h = (4,5,6, 4, 5)

print(f, g, h)