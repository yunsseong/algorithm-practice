n, c = map(int, input().split())
x = sorted([int(input()) for _ in range(n)])

s, e = 0, x[-1] - x[0]

while s <= e:
    mid = (s + e) // 2

    cnt = 1
    prv = x[0]

    for i in range(1, len(x)):
        if x[i] - prv >= mid:
            cnt += 1
            prv = x[i]

    if cnt >= c:
        s = mid + 1
    else:
        e = mid - 1
print(e)




