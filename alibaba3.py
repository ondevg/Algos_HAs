def knapsack(ws, cs, W):
    N = len(ws)
    d = [[0] * (W + 1) for i in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if ws[i - 1] > w:
                d[i][w] = d[i - 1][w]
            else:
                d[i][w] = max(d[i - 1][w], d[i - 1][w - ws[i - 1]] + cs[i - 1])

    i = N
    w = W
    res = []
    while i > 0 and w > 0:
        if d[i][w] != d[i - 1][w]:
            res.append(i)
            w -= ws[i - 1]
        i -= 1
    return d[N][W], res


W, N = map(int, input().split())
w = list(map(int, input().split()))
c = list(map(int, input().split()))
c, res = knapsack(w, c, W)
print(c)
print(len(res))
print(' '.join(map(str, res)))