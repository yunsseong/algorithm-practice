s = list(input())
cnt = 0
res = 0

for i in range(len(s)):
    if s[i] == "(":
        cnt += 1
    else:
        cnt -= 1
        if s[i-1] == "(":
            res += cnt
        else:
            res += 1
print(res)
