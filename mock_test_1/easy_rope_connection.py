"""
Easy: Rope Connection — Min Heap Greedy
Approach: Always connect 2 smallest ropes first
Time: O(n log n)
"""
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ropes = [int(input()) for _ in range(n)]
    
    if n == 1:
        print(0)
        return
    
    heapq.heapify(ropes)
    total_cost = 0
    
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        combined = first + second
        total_cost += combined
        heapq.heappush(ropes, combined)
    
    print(total_cost)

solve()
