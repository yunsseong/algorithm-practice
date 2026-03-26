from collections import deque

s = deque(input())
straight = False
res = []
buffer = deque()

while s:
    cur = s.popleft()
    if cur == "<":
        straight = True
        buffer.append(cur)
    elif cur == ">":
        buffer.append(cur)
        res.extend(buffer)
        buffer = deque()
        straight = False
    elif cur == " ":
        buffer.append(cur)
        if not straight:
            res.extend(buffer)
            buffer = deque()
    else:
        if straight:
            buffer.append(cur)
        else:
            buffer.appendleft(cur)
if buffer:
    res.extend(buffer)

print(''.join(res))