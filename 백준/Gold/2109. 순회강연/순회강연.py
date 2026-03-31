import heapq

n = int(input())
lecture = sorted([list(map(int, input().split())) for _ in range(n)], key = lambda x : (x[1], x[0]))
hq = []

for p, d in lecture:
    heapq.heappush(hq, p)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))