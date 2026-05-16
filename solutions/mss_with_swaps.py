"""
MSS With Swaps (Medium) - Infosys SP/DSE
Approach: Try every subarray, greedily swap smallest inside with largest outside
Time: O(n^3) — fine for n <= 500
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    a = [int(input()) for _ in range(n)]
    
    best = max(a)
    
    for l in range(n):
        for r in range(l, n):
            inside = sorted(a[l:r+1])
            outside = sorted(a[:l] + a[r+1:], reverse=True)
            
            s = sum(inside)
            for swap_idx in range(min(k, len(inside), len(outside))):
                if inside[swap_idx] < outside[swap_idx]:
                    s += outside[swap_idx] - inside[swap_idx]
                else:
                    break
            best = max(best, s)
    
    print(best)

solve()
