import sys
input = sys.stdin.readline

left = list(input().rstrip())
right = []
n = int(input().rstrip())

for _ in range(n):
    c = input().rstrip()
    if c == "L":
        if left:
            right.append(left.pop())
    elif c == "D":
        if right:
            left.append(right.pop())
    elif c == "B":
        if left:
            left.pop()
    else:
        left.append(c[2])

print(''.join(left + right[::-1]))
