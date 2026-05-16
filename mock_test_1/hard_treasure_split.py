"""
Hard: Treasure Split — Partition DP
Approach: dp[i][j] = min cost to split first i elements into j groups
Time: O(n^2 * k)
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    arr = [int(input()) for _ in range(n)]
    
    # Precompute cost[i][j] = max(arr[i..j]) - min(arr[i..j])
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        mn = mx = arr[i]
        for j in range(i, n):
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])
            cost[i][j] = mx - mn
    
    # DP
    INF = float('inf')
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            for l in range(j - 1, i):
                if dp[l][j - 1] < INF:
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + cost[l][i - 1])
    
    print(dp[n][k])

solve()
