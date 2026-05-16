"""
Layer-Split Path Maximization (Complex) - Infosys SP/DSE
Approach: Process nodes by layer (ascending). DP[u] = max score ending at u.
- Cross-layer: penalty = (y-x)^2
- Same-layer: no penalty, iterate until stable
Time: O(N * M) approximately
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    N = int(input())
    M = int(input())
    K = int(input())
    
    layers = [0] * N
    values = [0] * N
    for i in range(N):
        l, v = map(int, input().split())
        layers[i] = l
        values[i] = v
    
    adj = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
    
    dp = [v for v in values]
    best = max(values)
    
    layer_groups = defaultdict(list)
    for u in range(N):
        layer_groups[layers[u]].append(u)
    
    for layer_val in sorted(layer_groups.keys()):
        nodes = layer_groups[layer_val]
        
        # Extend from neighbors with smaller layer
        for u in nodes:
            for v in adj[u]:
                if layers[v] < layers[u]:
                    penalty = (layers[u] - layers[v]) ** 2
                    dp[u] = max(dp[u], dp[v] + values[u] - penalty)
        
        # Propagate within same layer (no penalty)
        changed = True
        iters = 0
        while changed and iters < len(nodes) + 1:
            changed = False
            iters += 1
            for u in nodes:
                for v in adj[u]:
                    if layers[v] == layers[u]:
                        candidate = dp[v] + values[u]
                        if candidate > dp[u]:
                            dp[u] = candidate
                            changed = True
        
        for u in nodes:
            best = max(best, dp[u])
    
    print(best)

solve()
