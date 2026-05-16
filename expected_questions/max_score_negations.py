"""
Expected Q3 (Medium): Maximum Score with K Negations
Problem: Given array and K, negate any element K times. Maximize total array sum.
Time: O(n log n + k log n)
"""
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    a = [int(input()) for _ in range(n)]
    
    heapq.heapify(a)
    for _ in range(k):
        smallest = heapq.heappop(a)
        heapq.heappush(a, -smallest)
    print(sum(a))

solve()
