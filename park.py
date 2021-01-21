from collections import deque

steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]
N = M = -1
INF = 10 ** 9


def bfs(maze, visited, d, s):
    vertex_queue = deque([s])
    while vertex_queue:
        vi, vj = vertex_queue.popleft()
        visited[vi][vj] = 2
        for step_i, step_j in steps:
            ui = vi + step_i
            uj = vj + step_j
            if 0 <= ui < N and 0 <= uj < M:
                if maze[ui][uj] != '#' and not visited[ui][uj]:
                    visited[ui][uj] = 1
                    vertex_queue.append((ui, uj))
                    d[ui][uj] = d[vi][vj] + 1


N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(input())

for i in range(N):
    for j in range(M):
        if maze[i][j] == 'E':
            s = (i, j)
        elif maze[i][j] == 'X':
            f = (i, j)

visited = [[0] * M for i in range(N)]
d = [[INF] * M for i in range(N)]
d[s[0]][s[1]] = 0
bfs(maze, visited, d, s)
res = d[f[0]][f[1]]
print(res if res != INF else -1)
