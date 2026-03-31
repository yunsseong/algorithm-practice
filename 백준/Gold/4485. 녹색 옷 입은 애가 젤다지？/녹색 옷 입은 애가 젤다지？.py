import heapq

cnt = 0
while 1:
    cnt += 1
    n = int(input())
    if n == 0:
        break

    g = [list(map(int, input().split())) for _ in range(n)]

    hq = [(0, 0, g[0][0])]
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = g[0][0]
    while hq:
        cr, cc, cost = heapq.heappop(hq)
        if cost > dist[cr][cc]:
            continue

        for dr, dc in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < n and 0 <= nc < n:
                if dist[nr][nc] > g[nr][nc] + cost:
                    dist[nr][nc] = g[nr][nc] + cost
                    heapq.heappush(hq, (nr, nc, g[nr][nc] + cost))

    print(f"Problem {cnt}: {dist[n-1][n-1]}")