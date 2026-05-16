"""
Expected Q4 (Medium): Minimum Platforms — Sweep Line / Events
Problem: Given arrival/departure of N trains, find min platforms needed.
Time: O(n log n)
"""
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dep = [int(input()) for _ in range(n)]
    events = [(a, 1) for a in arr] + [(d, -1) for d in dep]
    events.sort(key=lambda x: (x[0], x[1]))
    curr = mx = 0
    for _, typ in events:
        curr += typ
        mx = max(mx, curr)
    print(mx)

solve()
