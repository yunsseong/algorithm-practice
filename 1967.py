from collections import deque

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    p, c, w = map(int, input().split())
    g[p].append([c, w])
    g[c].append([p, w])

def bfs(s):
    d = [-1] * (n + 1)
    d[s] = 0
    q = deque([s])

    while q:
        cur = q.popleft()
        for next, w in g[cur]:
            if d[next] == -1:
                d[next] = d[cur] + w
                q.append(next)

    max_node, max_d = 0, 0
    for i in range(1, n + 1):
        if max_d < d[i]:
            max_d = d[i]
            max_node = i

    return max_node, max_d

max_node, max_d = bfs(1)
print(bfs(max_node)[1])
