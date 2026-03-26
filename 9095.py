n = int(input())
cases = [int(input()) for _ in range(n)]
dp = [0] * (max(cases) + 1)

dp[1] = 1

if n >= 2:
    dp[2] = 2

if n >= 3:
    dp[3] = 4

for i in range(4, max(cases) + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for c in cases:
    print(dp[c])