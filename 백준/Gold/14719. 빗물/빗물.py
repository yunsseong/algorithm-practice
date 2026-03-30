h, w = map(int, input().split())
height = list(map(int, input().split()))

left, right = 0, w-1
left_max, right_max = height[0], height[-1]
res = 0

while left < right:

    if height[left] > height[right]:
        res += right_max - height[right]
        right -= 1
        right_max = max(right_max, height[right])
    else:
        res += left_max - height[left]
        left += 1
        left_max = max(left_max, height[left])

print(res)