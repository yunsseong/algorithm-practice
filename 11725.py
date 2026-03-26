n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

stack = [1]
visited = [False] * (n + 1)
visited[1] = True
res = [0] * (n + 1)

while stack:
    cur = stack.pop()
    for next in g[cur]:
        if not visited[next]:
            res[next] = cur
            visited[next] = True
            stack.append(next)

print('\n'.join(map(str,res[2:])))