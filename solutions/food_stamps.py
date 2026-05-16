"""
Food Stamps (Easy) - Infosys SP/DSE
Approach: Binary Search on the threshold taste value
Time: O(n * log(max_v))
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    v = [int(input()) for _ in range(n)]
    d = [int(input()) for _ in range(n)]
    
    def count_and_sum(X):
        """Count meals with value >= X and their total taste points."""
        cnt = 0
        total = 0
        for i in range(n):
            if v[i] < X:
                continue
            t = (v[i] - X) // d[i] + 1
            if t <= 0:
                continue
            total += t * v[i] - d[i] * (t * (t - 1) // 2)
            cnt += t
        return cnt, total
    
    lo, hi = 0, max(v) + 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        cnt, _ = count_and_sum(mid)
        if cnt >= m:
            lo = mid
        else:
            hi = mid - 1
    
    cnt, total = count_and_sum(lo)
    excess = cnt - m
    total -= excess * lo
    
    print(total)

solve()
