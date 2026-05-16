# 🎯 Infosys SP/DSE Off-Campus Round 1 — Complete Prep Kit (May 2026)

> **Your Test:** 17th May 2026 | 9:00 AM – 12:00 PM | 3 Hours | 4 Questions (Easy → Complex)

---

## 📊 Test Pattern Analysis

| Level | Topics | Strategy | Time |
|-------|--------|----------|------|
| **Easy** | Greedy, Heap, Sorting, Arrays | Must solve 100% test cases | 30 min |
| **Medium** | Kadane's, DP, Sliding Window, Two Pointers | Aim 80%+ test cases | 45 min |
| **Hard** | Graph+DP, Matching, Bitmask DP, Combinatorics | Aim 60%+ test cases | 50 min |
| **Complex** | Layered Graph DP, Segment Trees, Advanced DP | Partial credit OK | 55 min |

---

## ✅ Solutions to YOUR Actual Questions

### 1. Food Stamps (Easy) — Greedy + Heap + Binary Search

**Key Insight:** Each food's t-th purchase gives `v[i] - d[i]*(t-1)` points. Use **binary search on the threshold value** — find the cut-off where we take exactly M meals.

> **⚠️ M can be 10^9!** A naive per-meal heap-pop will TLE. Use binary search on the "minimum acceptable taste value".

```python
def solve():
    n = int(input())
    m = int(input())
    v = [int(input()) for _ in range(n)]
    d = [int(input()) for _ in range(n)]
    
    # Binary search on threshold X: take all purchases with value >= X
    # For food i, purchases with value >= X: v[i] - d[i]*(t-1) >= X
    # => t <= (v[i] - X) / d[i] + 1
    
    def count_and_sum(X):
        cnt = 0
        total = 0
        for i in range(n):
            if v[i] < X:
                continue
            t = (v[i] - X) // d[i] + 1
            if t <= 0:
                continue
            # Sum of AP: v[i] + (v[i]-d[i]) + ... for t terms
            # = t*v[i] - d[i]*(0+1+...+(t-1)) = t*v[i] - d[i]*t*(t-1)//2
            total += t * v[i] - d[i] * (t * (t - 1) // 2)
            cnt += t
        return cnt, total
    
    lo, hi = 0, max(v) + 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        cnt, _ = count_and_sum(mid)
        if cnt >= m:
            lo = mid
        else:
            hi = mid - 1
    
    cnt, total = count_and_sum(lo)
    # Remove excess meals (all valued exactly lo)
    excess = cnt - m
    total -= excess * lo
    
    print(total)

solve()
```

**Verification with samples:**
- Case 1: n=1, m=1, v=[5], d=[2] → buy once → 5 ✓
- Case 2: n=2, m=2, v=[5,7], d=[2,4] → buy each once → 12 ✓
- Case 3: n=3, m=5, v=[5,7,9], d=[2,4,6] → 5+3+7+3+9 = 27 ✓

---

### 2. MSS With Swaps (Medium) — Brute Force + Greedy Swaps

**Key Insight:** n ≤ 500, so O(n³) is fine. For each subarray [l,r], greedily swap: replace smallest inside elements with largest outside elements.

```python
def solve():
    n = int(input())
    k = int(input())
    a = [int(input()) for _ in range(n)]
    
    best = max(a)  # Single element is always valid
    
    for l in range(n):
        for r in range(l, n):
            inside = sorted(a[l:r+1])
            outside = sorted(a[:l] + a[r+1:], reverse=True)
            
            s = sum(inside)
            for swap_idx in range(min(k, len(inside), len(outside))):
                # Swap smallest inside with largest outside if beneficial
                if inside[swap_idx] < outside[swap_idx]:
                    s += outside[swap_idx] - inside[swap_idx]
                else:
                    break
            best = max(best, s)
    
    print(best)

solve()
```

**Verification:**
- Case 1: [1,-5,2], k=1 → subarray [0,2], swap -5↔nothing? Better: subarray [1,2]=[−5,2], swap -5 with 1 → sum=1+2=3 ✓
- Case 2: [5,-1,5], k=0 → full array sum=9 ✓
- Case 3: [1,-5,2], k=0 → max single subarray = [2] = 2 ✓

---

### 3. Lock & Parity (Hard) — Pair Enumeration + Parity Analysis

**Key Insight:** Adding more pairs only increases total cost. So optimal = smallest cost even-valued pair. If none exists, answer is -1.

**Why?** Any valid set needs `#even ≥ #odd`. Single odd pair → invalid (0 ≥ 1 fails). Two odd pairs → invalid (0 ≥ 2 fails). Any set with odd pairs needs ≥ equal even pairs, adding cost. Single even pair (even=1, odd=0) is always minimum.

```python
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
```

**Verification:**
- Case 1: min even pair = |41−15| = 26 ✓
- Case 2: min even pair = |45−15| = 30 ✓
- Case 3: min even pair = |1−25| = 24 ✓

---

### 4. Layer-Split Path Maximization (Complex) — Layered Graph DP

**Key Insight:** Process nodes by layer (ascending). DP[u] = max score of path ending at u. Cross-layer transitions incur `(y-x)²` penalty. Same-layer transitions have no penalty but need iterative relaxation.

```python
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
    
    # dp[u] = max score of any valid path ending at u
    dp = [v for v in values]  # start: single-node path
    best = max(values)
    
    # Group nodes by layer
    layer_groups = defaultdict(list)
    for u in range(N):
        layer_groups[layers[u]].append(u)
    
    sorted_layer_vals = sorted(layer_groups.keys())
    
    for layer_val in sorted_layer_vals:
        nodes = layer_groups[layer_val]
        
        # 1) Extend from neighbors with SMALLER layer
        for u in nodes:
            for v in adj[u]:
                if layers[v] < layers[u]:
                    penalty = (layers[u] - layers[v]) ** 2
                    candidate = dp[v] + values[u] - penalty
                    if candidate > dp[u]:
                        dp[u] = candidate
        
        # 2) Propagate within same layer (no penalty, iterate until stable)
        changed = True
        iterations = 0
        while changed and iterations < len(nodes) + 1:
            changed = False
            iterations += 1
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
```

**Verification:**
- Case 1: path 0→1, penalty=(3-1)²=4, score=10+100-4=106 ✓
- Case 2: path 0→1→2, penalties=1+1=2, score=60-2=58 ✓
- Case 3: just node 1, score=100 ✓

---

## 🔮 6 Expected Questions for Round 1

### Expected Q1 (Easy): Minimize Maximum Load — Binary Search on Answer

**Problem:** Distribute N tasks (with times `t[i]`) among K workers. Each worker gets contiguous tasks. Minimize the maximum total time any worker has.

```python
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
```

---

### Expected Q2 (Easy): Minimum Cost to Connect Ropes — Heap

```python
import heapq

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
```

---

### Expected Q3 (Medium): Maximum Score with K Negations

**Problem:** Given array and K, negate any element K times. Maximize the total array sum.

```python
import heapq

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
```

---

### Expected Q4 (Medium): Minimum Platforms for Trains

```python
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
```

---

### Expected Q5 (Hard): Partition Array Max Sum DP

**Problem:** Partition array into subarrays of max length K. Each subarray's values become its max. Maximize total sum.

```python
def solve():
    n = int(input())
    k = int(input())
    a = [int(input()) for _ in range(n)]
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        mx = 0
        for j in range(1, min(k, i) + 1):
            mx = max(mx, a[i - j])
            dp[i] = max(dp[i], dp[i - j] + mx * j)
    print(dp[n])

solve()
```

---

### Expected Q6 (Hard): Shortest Path with K Free Passes — Modified Dijkstra

```python
import heapq
from collections import defaultdict

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
    pq = [(0, 0, 0)]
    
    while pq:
        cost, u, p = heapq.heappop(pq)
        if u == n - 1:
            print(cost)
            return
        if cost > dist[u][p]:
            continue
        for v, w in adj[u]:
            if cost + w < dist[v][p]:
                dist[v][p] = cost + w
                heapq.heappush(pq, (cost + w, v, p))
            if p < k and cost < dist[v][p + 1]:
                dist[v][p + 1] = cost
                heapq.heappush(pq, (cost, v, p + 1))
    print(-1)

solve()
```

---

## 📋 Top 15 Patterns Quick Reference

| # | Pattern | When to Use |
|---|---------|-------------|
| 1 | **Max-Heap Greedy** | Repeatedly pick best option |
| 2 | **Binary Search on Answer** | "Minimize max" / "Maximize min" |
| 3 | **Kadane's Algorithm** | Maximum subarray sum |
| 4 | **Sliding Window** | Fixed/variable size subarray |
| 5 | **Two Pointers** | Sorted array pair finding |
| 6 | **0/1 Knapsack DP** | Select items with weight limit |
| 7 | **LIS/LCS DP** | Longest increasing/common seq |
| 8 | **Interval Scheduling** | Non-overlapping intervals |
| 9 | **Dijkstra's Algorithm** | Shortest path weighted graph |
| 10 | **BFS/DFS** | Graph traversal/components |
| 11 | **Union-Find** | Connected components/MST |
| 12 | **Prefix Sums** | Range sum queries |
| 13 | **Monotonic Stack** | Next greater/smaller element |
| 14 | **Topological Sort** | DAG ordering/dependencies |
| 15 | **Bitmask DP** | Small n subset problems |

---

## 🏆 Exam Day Strategy

1. **Read ALL 4 questions first** (5 min) — identify Easy immediately
2. **Solve Easy first** (25 min) — get full marks here
3. **Medium next** (40 min) — usually Kadane's/Greedy variant
4. **Hard** (50 min) — look for the key insight (parity, matching, etc.)
5. **Complex** (50 min) — even partial solution scores points
6. **Last 10 min** — recheck edge cases, verify sample outputs

**Python Fast I/O:**
```python
import sys
input = sys.stdin.readline
```

**Good luck on 17th May! 🚀**
