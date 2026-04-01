n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]

def dfs(r, c):
    if r == n - 1 and c == n - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for dr, dc in ((0, g[r][c]), (g[r][c], 0)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]

print(dfs(0, 0))