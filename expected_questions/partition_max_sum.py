"""
Expected Q5 (Hard): Partition Array for Maximum Sum — DP
Problem: Partition array into subarrays of max length K.
Each subarray values become its max. Maximize total sum.
Time: O(n * k)
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    a = [int(input()) for _ in range(n)]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        mx = 0
        for j in range(1, min(k, i) + 1):
            mx = max(mx, a[i - j])
            dp[i] = max(dp[i], dp[i - j] + mx * j)
    print(dp[n])

solve()
