G = None
visited = None


def dfs2(G: list, visited: list, s: int, color):
    vertex_stack = [s]
    while vertex_stack:
        v = vertex_stack.pop()
        if not visited[v]:
            visited[v] = color
            for u in G[v]:
                if not visited[u]:
                    vertex_stack.append(u)


N, M = map(int, input().split())
G = [[] for i in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    G[x].append(y)
    G[y].append(x)

visited = [False] * len(G)

t = 0
for i in range(N):
    if not visited[i]:
        t += 1
        dfs2(G, visited, i, t)

comps = [[] for i in range(t)]
for i, v in enumerate(visited):
    comps[v - 1].append(i)

print(len(comps))
for c in comps:
    print(len(c))
    print(' '.join(map(str, c)))
