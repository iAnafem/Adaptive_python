def power(a, n):
    if n < 0:
        return 1 / a ** -n
    elif n == 0:
        return 1
    elif n == 1:
        return a
    elif n % 2 == 0:
        return power(a * a, n / 2)
    else:
        return a * power(a * a, (n - 1) / 2)


_a, _n = [float(input()) for i in range(2)]
print(power(_a, _n))

