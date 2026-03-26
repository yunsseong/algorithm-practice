k = int(input())
n = list(map(int, input().split()))

for i in range(k-1, -1, -1):
    tmp = []
    for j in range(2**i - 1, len(n), 2**(i + 1)):
        tmp.append(n[j])
    print(' '.join(map(str, tmp)))
