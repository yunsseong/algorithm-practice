import sys
sys.setrecursionlimit(500 * 500 + 10)

m, n = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]

def dfs(r, c):
    if r == m - 1 and c == n - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = dr + r, dc + c
        if 0 <= nr < m and 0 <= nc < n and g[nr][nc] < g[r][c]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]

print(dfs(0, 0))