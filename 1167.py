from collections import deque

n = int(input())
g = [[] for _ in range(n+1)]

for _ in range(n):
    tmp = list(map(int, input().split()))
    p = tmp[0]
    children = tmp[1:-1]
    for i in range(0, len(children), 2):
        g[p].append([children[i], children[i + 1]])
        g[children[i]].append([p, children[i + 1]])

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

    max_d, max_node = 0, 0
    for i in range(1, n + 1):
        if d[i] > max_d:
            max_d = d[i]
            max_node = i

    return max_d, max_node

max_d, max_node = bfs(1)
print(bfs(max_node)[0])

