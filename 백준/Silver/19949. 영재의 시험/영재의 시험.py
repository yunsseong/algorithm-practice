p = list(map(int, input().split()))

s = [0] * 10
cnt = 0

def rec(idx, solved):
    global cnt

    if solved + (10 - idx) < 5:
        return

    if idx == 10:
        if solved >= 5:
            cnt += 1
        return

    for i in range(1, 6):
        if idx >= 2 and i == s[idx - 1] == s[idx - 2]:
            continue
        s[idx] = i
        rec(idx + 1, solved + (1 if p[idx] == i else 0))

rec(0, 0)
print(cnt)