"""
Complex: Grid Treasure Hunt — 3D DP (grid + shields)
Approach: dp[i][j][s] = max sum at (i,j) with s shields used
Time: O(n * m * k)
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    k = int(input())
    
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    k = min(k, n + m - 1)
    
    NEG_INF = float('-inf')
    dp = [[[NEG_INF] * (k + 1) for _ in range(m)] for _ in range(n)]
    
    # Base case
    dp[0][0][0] = grid[0][0]
    if grid[0][0] < 0 and k > 0:
        dp[0][0][1] = 0
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            for s in range(k + 1):
                best = NEG_INF
                # From top
                if i > 0 and dp[i-1][j][s] != NEG_INF:
                    best = max(best, dp[i-1][j][s] + grid[i][j])
                # From left
                if j > 0 and dp[i][j-1][s] != NEG_INF:
                    best = max(best, dp[i][j-1][s] + grid[i][j])
                dp[i][j][s] = max(dp[i][j][s], best)
                
                # Shield on this cell (only if negative)
                if grid[i][j] < 0 and s > 0:
                    shield_best = NEG_INF
                    if i > 0 and dp[i-1][j][s-1] != NEG_INF:
                        shield_best = max(shield_best, dp[i-1][j][s-1])
                    if j > 0 and dp[i][j-1][s-1] != NEG_INF:
                        shield_best = max(shield_best, dp[i][j-1][s-1])
                    dp[i][j][s] = max(dp[i][j][s], shield_best)
    
    ans = max(dp[n-1][m-1][s] for s in range(k + 1))
    print(ans)

solve()
