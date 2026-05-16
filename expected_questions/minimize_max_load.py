"""
Expected Q1 (Easy): Minimize Maximum Load — Binary Search on Answer
Problem: Distribute N tasks among K workers (contiguous). Minimize max total time.
Time: O(n * log(sum))
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    t = [int(input()) for _ in range(n)]
    
    def feasible(max_load):
        workers = 1
        curr = 0
        for time in t:
            if time > max_load:
                return False
            if curr + time > max_load:
                workers += 1
                curr = time
            else:
                curr += time
        return workers <= k
    
    lo, hi = max(t), sum(t)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)

solve()
