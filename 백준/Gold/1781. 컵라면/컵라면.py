import heapq
n = int(input())
p = []

for _ in range(n):
    a, b = map(int, input().split())
    p.append([a, b])

p.sort()
hq = []

for d, c in p:
    heapq.heappush(hq, c)
    if len(hq) > d:
        heapq.heappop(hq)
print(sum(hq))