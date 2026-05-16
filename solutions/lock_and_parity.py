"""
Lock & Parity (Hard) - Infosys SP/DSE
Key Insight: Answer is always the minimum cost even-valued pair.
- Single odd pair: even=0 < odd=1 → INVALID
- Two odd pairs: even=0 < odd=2 → INVALID
- Any set with odd pairs needs >= equal even pairs → more cost
- Single even pair: even=1 >= odd=0 → VALID and cheapest
Time: O(n^2)
"""
import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    L = [int(input()) for _ in range(N)]
    
    min_even_cost = float('inf')
    
    for j in range(N):
        for i in range(j + 1, N):
            if L[j] != L[i]:
                cost = abs(L[j] - L[i])
                if cost % 2 == 0:
                    min_even_cost = min(min_even_cost, cost)
    
    if min_even_cost == float('inf'):
        print(-1)
    else:
        print(min_even_cost)

solve()
