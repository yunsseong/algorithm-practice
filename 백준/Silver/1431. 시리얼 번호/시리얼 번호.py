n = int(input())
s = []

for _ in range(n):
    tmp = input()
    num = 0
    for t in tmp:
        if t.isdigit():
            num += int(t)
    s.append([len(tmp), num, tmp])

s.sort(key = lambda x : (x[0], x[1], x[2]))
print('\n'.join([k for i,j,k in s]))