import sys
input = sys.stdin.readline

n = int(input().rstrip())
s = 0
for _ in range(n):

    c = input().rstrip()
    command = c[0:3]
    if command == "add":
        s |= 1 << int(c.split()[1])
    elif command == "che":
        print(s >> int(c.split()[1]) & 1)
    elif command == "tog":
        if s >> int(c.split()[1]) & 1:
            s &= ~(1 << int(c.split()[1]))
        else:
            s |= 1 << int(c.split()[1])
    elif command == "rem":
        s &= ~(1 << int(c.split()[1]))
    elif command == "all":
        s = (1 << 21) - 1
    elif command == "emp":
        s = 0