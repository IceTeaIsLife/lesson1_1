import math


def f11(x, y, z):
    return math.tan(math.exp(y) + x ** 4) - 7 * z ** 6 - 32 + \
           ((x ** 2 + 83 * x ** 8) ** 8) / 4 + math.exp(y) + (63 * z ** 4 - x) ** 4 - y ** 5


# print('1.1\n')
# print('%.2e' % f11(-82, 70, -47))
# print('%.2e' % f11(-69, 2, 90))


def f12(x):
    if x < -7:
        return x ** 8 + math.cos(x)
    elif -7 <= x < 19:
        return 17 * x ** 2 - (x ** 6) / 14
    elif 19 <= x < 64:
        return math.sin(math.log(math.tan(x) + 56 * x ** 3)) + x ** 3
    elif 64 <= x < 138:
        return x ** 3 + math.log(x) + 82
    elif x >= 138:
        74 * (x ** 5 + math.log(x)) ** 5 + math.sin(x)


# print('\n1.2\n')
# print('%.2e' % f12(121))
# print('%.2e' % f12(7))


def f13(n, m):
    x, y = 0, 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x += (i ** 4 + j ** 8)
            y += (abs(i) + 42 * i ** 3 - 72)
    return x - 93 * y


# print('\n1.3\n')
# print('%.2e' % f13(31, 61))
# print('%.2e' % f13(75, 12))


def f14(n):
    if n < 0:
        return None
    if n == 0:
        return 2
    elif n == 1:
        return 5
    else:
        return f14(n - 1) / 52 + (f14(n - 1) ** 2) / 97 + 32


# print('\n1.4\n')
# print('%.2e' % f14(2))
# print('%.2e' % f14(6))
