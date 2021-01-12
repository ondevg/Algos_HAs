def binsearch_left(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] < key:
            l = m
        else:
            r = m
    return r


def binsearch_right(x, key):
    l = -1
    r = len(x)
    while r - l > 1:
        m = (l + r) // 2
        if x[m] <= key:
            l = m
        else:
            r = m
    return r


N, M = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()


for i in range(M):
    l, r = map(int, input().split())
    print(binsearch_right(scores, r) - binsearch_left(scores, l))
