"""
Expected Q2 (Easy): Minimum Cost to Connect Ropes — Min-Heap Greedy
Problem: Connect N ropes into one. Cost = sum of two ropes connected. Find min total cost.
Time: O(n log n)
"""
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ropes = [int(input()) for _ in range(n)]
    heapq.heapify(ropes)
    total = 0
    while len(ropes) > 1:
        a = heapq.heappop(ropes)
        b = heapq.heappop(ropes)
        total += a + b
        heapq.heappush(ropes, a + b)
    print(total)

solve()
