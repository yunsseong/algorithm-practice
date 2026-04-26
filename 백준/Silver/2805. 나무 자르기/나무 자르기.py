n, m = map(int, input().split())
t = list(map(int, input().split()))

s, e = 0, max(t)

while s <= e:
    middle = (s + e) // 2
    get = sum([max(i - middle, 0) for i in t])
    if get >= m:
        s = middle + 1
    else:
        e = middle - 1
print(e)