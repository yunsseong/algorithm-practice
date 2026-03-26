import sys
input = sys.stdin.readline

m = int(input().rstrip())
s = 0

for _ in range(m):
    c = input().rstrip()
    if c in ("all", "empty"):
        if c == "all":
            s = (1 << 21) - 1
        elif c == "empty":
            s = 0
    else:
        o, n = c.split()
        n = int(n)
        if o == "add":
            s = s | (1 << n)
        elif o == "remove":
            s = s & ~(1 << n)
        elif o == "check":
            print(1 if (s >> n) & 1 else 0)
        elif o == "toggle":
            s = s ^ (1 << n)