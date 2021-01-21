inf = 10**9


def nails(x):
    N = len(x)
    d = [inf] * (N)
    d[0] = inf
    d[1] = x[1] - x[0]
    for i in range(2, N):
        d[i] = min(d[i - 2], d[i - 1]) + x[i] - x[i - 1]
    return d[N - 1]


N = int(input())
x = sorted(list(map(int, input().split())))
print(nails(x))