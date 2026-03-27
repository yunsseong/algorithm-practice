import heapq

def dijk(s, e):
    global g
    dist = [float('inf')] * (n + 1)
    dist[s] = 0

    pq = [(0, s)]

    while pq:
        cost, cur = heapq.heappop(pq)
        if cost > dist[cur]:
            continue

        for next_node, next_cost in g[cur]:
            if cost + next_cost < dist[next_node]:
                dist[next_node] = cost + next_cost
                heapq.heappush(pq, (dist[next_node], next_node))
    return dist[e]

n, e = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    g[a].append([b, c])
    g[b].append([a, c])

v1, v2 = map(int, input().split())

res = min(dijk(1, v1) + dijk(v1, v2) + dijk(v2, n), dijk(1, v2) + dijk(v2, v1) + dijk(v1, n))
print(res if res != float('inf') else -1)
