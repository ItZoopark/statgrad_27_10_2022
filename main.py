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

def task_14():
    def to_16(x):
        alphabet = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        res = ''
        while x != 0:
            if x % 16 > 9:
                res = alphabet[x % 16] + res
            else:
                res = str(x % 16) + res
            x //= 16
        return res

    return to_16(4 ** 36 + 3 * 4 ** 20 + 4 ** 15 + 2 * 4 ** 7 + 49)


# print(len(set(task_14())))

def task_15():
    def f(x, A):
        return (x & 85 == 0) <= ((x & 54 != 0) <= (x & A != 0))

    A = 0
    while True:
        for x in range(1001):
            if not f(x, A):
                break
        else:
            return A
        A += 1


# print(task_15())

def task_16():
    def f(n):
        if n == 0:
            return 0
        elif n > 0 and n % 2 == 0:
            return f(n // 2)
        elif n % 2 != 0:
            return 1 + f(n - 1)

    count = 0
    for i in range(1, 501):
        if f(i) == 8:
            print(i, bin(i)[2:])
            count += 1
    print(count)


# print(task_16())
# print(bin(500)[2:])
def task_22():
    x = 4
    while True:
        x += 1
        a = 7 * x + 27
        b = 7 * x - 33
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a

        if a == 15:
            print(x)
            break


# task_22()
def task_23():
    def f(x, y):
        if x == y:
            return 1
        elif x > y:
            return 0
        else:
            return f(x + 1, y) + f(x * 3, y)

    print(f(2, 28) * f(28, 90))


# task_23()
def task_24():
    # data = 'jfhdgjAfghkAj'
    data = open('24.txt').read()
    mas = data.split('A')
    max_count = 0
    for i in range(len(mas) - 1):
        max_count = max(len(mas[i]) + len(mas[i + 1]) + 1, max_count)
        # t = mas[i] + 'A' + mas[i + 1]
        # max_count = max(len(t), max_count)
    print(max_count)
    # s = 'FGHGHH'
    # print(s.split('A'))
    # print(len(max(data.split('A'), key=len)) + 1)
    # cur_count = 0
    # cur_all = 0
    # countA = 0
    # for c in data:
    #     if countA > 1:
    #         cur_all = max(cur_all, cur_count + 1)
    #         cur_count = 0
    #     if c == 'A':
    #         countA += 1
    #     else:
    #         cur_count += 1
    # cur_all = max(cur_all, cur_count + 1)
    # print(cur_all)


# task_24()
# a = ['Z', 'AB']
# print(len(max(a, key=len)))
def razbor_19_20_21():
    size = 93
    win = 107
    a = [[0] * size * 2 for i in range(size * 2)]

    for s1 in range(size):
        for s2 in range(size):
            if 2 * s1 + s2 >= win or s1 + 2 * s2 >= win:
                a[s1][s2] = 1

    for k in range(2 * size):
        for s1 in range(size):
            for s2 in range(size):
                if a[s1][s2] == 0:
                    if a[s1 * 2][s2] > 0 and a[s1][s2 * 2] > 0 and a[s1 + 1][s2] > 0 and a[s1][s2 + 1] > 0:
                        a[s1][s2] = -max(a[s1 * 2][s2], a[s1][s2 * 2], a[s1 + 1][s2], a[s1][s2 + 1])
                    elif a[s1 * 2][s2] < 0 or a[s1][s2 * 2] < 0 or a[s1 + 1][s2] < 0 or a[s1][s2 + 1] < 0:
                        neg = list(
                            filter(lambda x: x < 0, [a[s1 * 2][s2], a[s1][s2 * 2], a[s1 + 1][s2], a[s1][s2 + 1]]))
                        a[s1][s2] = abs(min(neg)) + 1

    for s in range(1, 94):
        if a[13][s] == 2:
            print(s)


def razbor_23():
    a = set()

    def f(x, p, m):
        if p == m:
            a.add(x)
            return
        f(x + 2, p + 1, m)
        f(x * 3, p + 1, m)

    f(2, 0, 10)
    print(len(a))

razbor_23()
