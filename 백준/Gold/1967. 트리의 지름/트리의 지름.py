from collections import deque

n = int(input())
g = [[] for _ in range(n + 1)]

def bfs(s):
    q = deque([s])
    maxn, maxd = 0, 0
    visited = [-1] * (n + 1)
    visited[s] = 0
    while q:
        cur = q.popleft()
        for nxt, weight in g[cur]:
            if visited[nxt] == -1:
                q.append(nxt)
                visited[nxt] = visited[cur] + weight
                if maxd < visited[nxt]:
                    maxn = nxt
                    maxd = visited[nxt]
    return maxn, maxd

for _ in range(n - 1):
    a, b, w = map(int, input().split())
    g[a].append([b, w])
    g[b].append([a, w])

maxn, maxd = bfs(1)
print(bfs(maxn)[1])