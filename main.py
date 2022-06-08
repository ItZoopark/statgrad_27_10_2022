# 2
def f(x, y, z, w):
    return (x != y) <= ((x and w) == (z and (not w)))


def task_2():
    print('x y z w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if f(x, y, z, w) == 0:
                        print(x, y, z, w)


# task_2()
def task_3():
    N = 1
    while True:
        N += 1
        Nc = N
        s = 0
        si = 0
        l = len(str(Nc))
        i = 0
        while Nc != 0:
            d = Nc % 10
            Nc //= 10
            if (l - i) % 2 == 0:
                si += d
            i += 1

            if d % 2 == 0:
                s += d
        if abs(s - si) == 13:
            print(N)
            break


# task_3()
def task_4():
    count = 0

    for s in range(400, 500):
        sc = 3 * (s // 10)
        n = 1
        while sc < 221:
            sc = sc + 13
            n = n * 2
        if n == 128:
            print(s, end=' ')
            count += 1
    print(count)


# task_4()

# def to_5(x):
#     s = ''
#     while x != 0:
#         s = str(x % 5) + s
#         x //= 5
#     print(s)
#
# to_5(5)
# print(int('FF', 16))
def task_12():
    def alg(x):
        while '111' in x or '222' in x:
            x = x.replace('111', '22', 1)
            x = x.replace('222', '1', 1)
        return x

    s = '1' * 200
    while True:
        s += '1'
        if len(set(alg(s))) == 1 and '1' in set(alg(s)):
            break
    print(len(s))

# task_12()


