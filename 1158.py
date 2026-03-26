n, k = map(int, input().split())

p = [i for i in range(1, n+1)]
ans = []
pos = k - 1
while p:
    cur_val = p[pos]
    ans.append(cur_val)
    p.remove(cur_val)

    if len(p) == 0: break
    pos = (pos + k - 1) % len(p)
print("<"+", ".join(map(str, ans))+">")