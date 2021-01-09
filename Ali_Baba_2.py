import random


def less(i1, i2):
    return i1[0] * i2[1] < i2[0] * i1[1]


def equal(i1, i2):
    return i1[0] * i2[1] == i2[0] * i1[1]


def more(i1, i2):
    return i1[0] * i2[1] > i2[0] * i1[1]


def partition(x, l, r, pivot):
    il = l
    ir = l
    for i in range(l, r):
        if x[i] < pivot and ir < r:
            x[il], x[i] = x[i], x[il]
            if il != ir:
                x[ir], x[i] = x[i], x[ir]
            il += 1
            ir += 1
        elif x[i] == pivot and ir < r:
            x[ir], x[i] = x[i], x[ir]
            ir += 1
    return il, ir


def qsort(x, l=0, r=None):
    if r is None:
        r = len(x)
    if (r - l) > 1:
        pivot = x[random.randint(l, r - 1)]
        il, ir = partition(x, l, r, pivot)
        qsort(x, l, il)
        qsort(x, ir, r)


N, w = list(map(int, input().split()))
x = []
for i in range(N):
    x.append(tuple(map(int, input().split())))
qsort(x)
x = x[::-1]

s = 0
i = 0
while (i < N) and (w >= x[i][1]):
    s += x[i][0]
    w -= x[i][1]
    i += 1
if i < N:
    s += (x[i][0] * w // x[i][1])

print(s)
