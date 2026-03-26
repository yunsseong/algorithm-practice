r, c = map(int, input().split())
g = []
for _ in range(r):
    g.append([ord(i) - 65 for i in list(input())])

stack = [[0, 0, 0, 0]]
res = 0
while stack:
    cr, cc, visited, depth = stack.pop()
    if visited & 1 << g[cr][cc]:
        continue
    depth += 1
    visited |= 1 << g[cr][cc]
    res = max(res, depth)
    for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < r and 0 <= nc < c and not (visited >> g[nr][nc]) & 1:
            stack.append([nr, nc, visited, depth])
print(res)