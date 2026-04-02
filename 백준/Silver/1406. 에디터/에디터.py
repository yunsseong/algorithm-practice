import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
n = int(input().rstrip())
cs = [input().rstrip() for _ in range(n)]

for c in cs:
    if c[0] == "P":
        left.append(c[2])
    else:
        if c == "L":
            if left:
                right.append(left.pop())
        elif c == "D":
            if right:
                left.append(right.pop())
        elif c == "B":
            if left:
                left.pop()
print(''.join(left) + ''.join(right[::-1]))