"""
Medium: Chef's Special — Greedy + Max Heap
Approach: Sort by deadline, greedily pick dishes, swap if deadline missed
Time: O(n log n)
"""
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dishes = []
    for _ in range(n):
        p, e = map(int, input().split())
        dishes.append((e, p))  # (deadline, prep_time)
    
    dishes.sort()  # Sort by deadline
    
    current_time = 0
    max_heap = []  # stores negative prep times (for max heap)
    
    for deadline, prep_time in dishes:
        current_time += prep_time
        heapq.heappush(max_heap, -prep_time)
        
        if current_time > deadline:
            biggest = -heapq.heappop(max_heap)
            current_time -= biggest
    
    print(len(max_heap))

solve()
