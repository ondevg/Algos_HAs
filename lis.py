from bisect import bisect_left


inf = 10**9


def lis(x):
    N = len(x)
    d = [inf] * (N + 1)
    d[0] = -inf
    for i in range(N):
        l = bisect_left(d, x[i])
        d[l] = x[i]
    return max([i for i in range(N + 1) if d[i] < inf])


N = int(input())
x = list(map(int, input().split()))
print(lis(x))
