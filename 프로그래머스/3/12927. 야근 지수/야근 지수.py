import heapq

def solution(n, works):
    works = [-1 * i for i in works]
    heapq.heapify(works)
    
    while (n):
        e = heapq.heappop(works) * -1
        if (e == 0):
            break
        heapq.heappush(works, (e - 1) * -1 ) 
        n -= 1
    
    answer = sum([i * i for i in works])
    return answer