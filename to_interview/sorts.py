def gcd_m(a, b):
    if not b or not a:
        return b or a
    else:
        return gcd_m(b, a % b)

print(gcd_m(0, 5))
print(gcd_m(6, 0))
print(gcd_m(6456, 5))
print(gcd_m(56456, 546456))


def gcd_2(a, b):
    if b == 0:
        return a
    else:

        return gcd_m(b, a % b)


print(gcd_2(12555, 313875))
print(gcd_2(53453453324234435344534456, 54623345232))