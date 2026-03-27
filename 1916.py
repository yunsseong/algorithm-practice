import heapq

n, m = int(input()), int(input())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    g[s].append([e, c])

s, e = map(int, input().split())
pq = [(0, s)]

dist = [float('inf')] * (n + 1)

while pq:
    cost, cur = heapq.heappop(pq)

    if cost > dist[cur]:
        continue

    for next_node, next_cost in g[cur]:
        if cost + next_cost < dist[next_node]:
            dist[next_node] = cost + next_cost
            heapq.heappush(pq, (dist[next_node], next_node))

print(dist[e])
