inf = 10 ** 18
no_edge = 10 ** 5


def bellman_ford(N, E, s, K):
    d = [inf] * N
    d[s] = 0
    for i in range(K):
        tmp = list(d)
        for (v, u, w) in E:
            if d[u] > tmp[v] + w:
                d[u] = tmp[v] + w
    return d


N, s, f, K = map(int, input().split())
E = []
a = []
for i in range(N):
    a.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        if a[i][j] != -1:
            E.append((i, j, a[i][j]))

d = bellman_ford(N, E, s, K)
print(d[f] if d[f] != inf else -1)