from collections import deque

g = [deque(list(input())) for _ in range(4)]
c = [list(map(int, input().split())) for _ in range(int(input()))]

for i, d in c:
    i -= 1
    m = [0] * 4
    m[i] = d

    if i == 0:
        if g[0][2] != g[1][6]:
            m[1] = d * -1
            if g[1][2] != g[2][6]:
                m[2] = d
                if g[2][2] != g[3][6]:
                    m[3] = d * -1
    elif i == 1:
        if g[1][6] != g[0][2]:
            m[0] = d * -1
        if g[1][2] != g[2][6]:
            m[2] = d * -1
            if g[2][2] != g[3][6]:
                m[3] = d
    elif i == 2:
        if g[2][2] != g[3][6]:
            m[3] = d * -1
        if g[2][6] != g[1][2]:
            m[1] = d * -1
            if g[0][2] != g[1][6]:
                m[0] = d
    else:
        if g[3][6] != g[2][2]:
            m[2] = d * -1
            if g[2][6] != g[1][2]:
                m[1] = d
                if g[1][6] != g[0][2]:
                    m[0] = d * -1

    for j, x in enumerate(m):
        if x == 1:
            g[j].appendleft(g[j].pop())
        elif x == -1:
            g[j].append(g[j].popleft())

print(sum([int(g[i][0]) * 2 ** i for i in range(4)]))