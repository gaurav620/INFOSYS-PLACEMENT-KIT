"""
Expected Q6 (Hard): Shortest Path with K Free Passes — Modified Dijkstra
Problem: N cities, M roads with tolls. Find min cost from 0 to N-1 with K free passes.
Time: O((V+E) * K * log(V*K))
"""
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    k = int(input())
    
    adj = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    INF = float('inf')
    dist = [[INF] * (k + 1) for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]  # cost, node, passes_used
    
    while pq:
        cost, u, p = heapq.heappop(pq)
        if u == n - 1:
            print(cost)
            return
        if cost > dist[u][p]:
            continue
        for v, w in adj[u]:
            # Pay toll
            if cost + w < dist[v][p]:
                dist[v][p] = cost + w
                heapq.heappush(pq, (cost + w, v, p))
            # Use free pass
            if p < k and cost < dist[v][p + 1]:
                dist[v][p + 1] = cost
                heapq.heappush(pq, (cost, v, p + 1))
    
    print(-1)

solve()
