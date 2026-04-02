k, n = map(int, input().split())
ls = [int(input()) for _ in range(k)]
s, e = 0, max(ls)

while s <= e:
    mid = (s + e) // 2
    if mid == 0:
        break
    cnt = sum([l // mid for l in ls])

    if cnt >= n:
        s = mid + 1
    else:
        e = mid - 1
print(e)