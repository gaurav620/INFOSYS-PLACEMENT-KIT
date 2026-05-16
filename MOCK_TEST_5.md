# 📝 Infosys SP/DSE Mock Test 5

**Duration: 3 Hours | 4 Questions | Languages: Python, C++, Java**

---

## Easy : Duplicate Finder

Given an array of N integers where each element is between 1 and N-1 (inclusive). There is exactly **one duplicate** number which may appear more than once.

Find the **duplicate number** without modifying the array and using O(1) extra space.

### Input Format
The first line contains an integer, n, denoting the size of the array.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

### Constraints
2 <= n <= 10^5
1 <= arr[i] <= n-1

### Sample Test Cases

**Case 1**

Input:
```
5
1
3
4
2
2
```
Output:
```
2
```

**Case 2**

Input:
```
5
3
1
3
4
2
```
Output:
```
3
```

**Case 3**

Input:
```
3
1
1
2
```
Output:
```
1
```

---

### ✅ ANSWER — Duplicate Finder

**🧠 Approach: Floyd's Tortoise and Hare (Cycle Detection)**

**Kaise socha?**
- Array ko linked list ki tarah socho: arr[i] points to next index
- Duplicate hai → cycle banega!
- Floyd's algorithm: slow (1 step) aur fast (2 step) pointers
- Phase 1: cycle detect karo
- Phase 2: cycle start dhundho = duplicate number

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    
    # Phase 1: Find intersection point in cycle
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entry point of cycle
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    print(slow)

solve()
```

**Time: O(n) | Space: O(1)**

**🔑 Pattern: "Find duplicate in [1,N-1] range, O(1) space" → Floyd's Cycle Detection**

---

## Medium : Merge Intervals

Given N intervals where each interval has a start and end time.
Merge all **overlapping intervals** and return the list of merged intervals.

Print each merged interval on a separate line.

### Input Format
The first line contains an integer, n, denoting the number of intervals.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains two space-separated integers describing start[i] and end[i].

### Constraints
1 <= n <= 10^5
0 <= start[i] <= end[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
1 3
2 6
8 10
15 18
```
Output:
```
1 6
8 10
15 18
```
Explanation:
[1,3] and [2,6] overlap → merge to [1,6]

**Case 2**

Input:
```
2
1 4
4 5
```
Output:
```
1 5
```
Explanation:
Touching intervals merge.

**Case 3**

Input:
```
3
1 10
2 3
4 5
```
Output:
```
1 10
```
Explanation:
[2,3] and [4,5] are both inside [1,10].

---

### ✅ ANSWER — Merge Intervals

**🧠 Approach: Sort + Linear Scan**

**Kaise socha?**
- Pehle sort karo by start time
- Fir ek ek karke dekho: agar current interval previous se overlap karta hai → merge
- Overlap condition: current.start ≤ previous.end

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    intervals = []
    for _ in range(n):
        s, e = map(int, input().split())
        intervals.append((s, e))
    
    intervals.sort()  # Sort by start time
    
    merged = [intervals[0]]
    
    for i in range(1, n):
        curr_start, curr_end = intervals[i]
        last_start, last_end = merged[-1]
        
        if curr_start <= last_end:
            # Overlap → merge (extend end)
            merged[-1] = (last_start, max(last_end, curr_end))
        else:
            # No overlap → add new interval
            merged.append((curr_start, curr_end))
    
    for s, e in merged:
        print(s, e)

solve()
```

**Time: O(n log n) | Space: O(n)**

**🔑 Pattern: "Merge overlapping intervals" → Sort by start + Linear merge**

---

## Hard : 0/1 Knapsack

You have N items. Each item has a weight w[i] and a value v[i].
You have a bag with maximum weight capacity W.

Each item can be taken **at most once**. Find the **maximum total value** you can carry.

### Input Format
The first line contains an integer, n, denoting the number of items.
The next line contains an integer, W, denoting the bag capacity.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains two space-separated integers describing w[i] and v[i].

### Constraints
1 <= n <= 1000
1 <= W <= 2000
1 <= w[i], v[i] <= 1000

### Sample Test Cases

**Case 1**

Input:
```
4
7
1 1
3 4
4 5
5 7
```
Output:
```
9
```
Explanation:
Take items with weight 3 (value 4) and weight 4 (value 5).
Total weight = 7 ≤ 7. Total value = 9.

**Case 2**

Input:
```
3
5
2 3
3 4
4 5
```
Output:
```
7
```
Explanation:
Take items: weight 2 (value 3) + weight 3 (value 4) = weight 5, value 7.

**Case 3**

Input:
```
1
1
2 10
```
Output:
```
0
```
Explanation:
Item weighs 2 but bag capacity is 1. Cannot take anything.

---

### ✅ ANSWER — 0/1 Knapsack

**🧠 Approach: Classic DP**

**Kaise socha?**
- "Take or skip each item, maximize value under weight limit" → 0/1 Knapsack!
- dp[i][w] = max value using first i items with capacity w
- Optimized: 1D array, iterate weight in **reverse** (important for 0/1!)

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    W = int(input())
    items = []
    for _ in range(n):
        w, v = map(int, input().split())
        items.append((w, v))
    
    # dp[w] = max value achievable with capacity w
    dp = [0] * (W + 1)
    
    for weight, value in items:
        # REVERSE order! (ensures each item used at most once)
        for w in range(W, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    
    print(dp[W])

solve()
```

**Time: O(n × W) | Space: O(W)**

**🔑 Pattern: "Pick items, max value, weight limit" → 0/1 Knapsack**
- 0/1 (each item once): inner loop **REVERSE**
- Unbounded (unlimited items): inner loop **FORWARD**

---

## Complex : Topological Sort + Shortest Path in DAG

You have N tasks numbered 0 to N-1. Some tasks depend on others. Each task takes time[i] to complete.

A task can only start after **all its dependencies** are finished. Multiple independent tasks can run in **parallel**.

Find the **minimum total time** to complete all tasks.

### Input Format
The first line contains an integer, n, denoting the number of tasks.
The next line contains an integer, m, denoting the number of dependencies.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing time[i].
Each line i of the m subsequent lines (where 0 ≤ i < m) contains two space-separated integers a, b meaning task a must finish before task b starts.

### Constraints
1 <= n <= 10^5
0 <= m <= 10^5
1 <= time[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
3
3
2
4
1
0 1
0 2
1 3
```
Output:
```
7
```
Explanation:
Task 0 (time 3) → then Task 1 (time 2) and Task 2 (time 4) in parallel → Task 1 finishes at 5, Task 2 at 7.
Task 3 needs Task 1 → starts at 5, finishes at 6.
All done at time 7.

**Case 2**

Input:
```
3
0
5
3
7
```
Output:
```
7
```
Explanation:
No dependencies. All tasks run in parallel. Longest task = 7.

**Case 3**

Input:
```
3
2
1
2
3
0 1
1 2
```
Output:
```
6
```
Explanation:
Chain: 0→1→2. Total = 1+2+3 = 6.

---

### ✅ ANSWER — Task Scheduling (Critical Path)

**🧠 Approach: Topological Sort + Longest Path in DAG**

**Kaise socha?**
- Dependencies = Directed Acyclic Graph (DAG)
- Parallel execution = each task starts ASAP after dependencies done
- Earliest completion of task i = max(completion of all parents) + time[i]
- Answer = max completion time across all tasks
- Process in **topological order** (dependencies pehle)

```python
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    time_cost = [int(input()) for _ in range(n)]
    
    adj = defaultdict(list)
    in_degree = [0] * n
    
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        in_degree[b] += 1
    
    # Topological sort (Kahn's algorithm) + compute earliest finish
    earliest_finish = [0] * n
    queue = deque()
    
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            earliest_finish[i] = time_cost[i]
    
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            # Task v can start after task u finishes
            earliest_finish[v] = max(earliest_finish[v], 
                                     earliest_finish[u] + time_cost[v])
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    print(max(earliest_finish))

solve()
```

**Time: O(V + E) | Space: O(V + E)**

**🔑 Pattern: "Min time with parallel execution + dependencies" → Topological Sort + Longest Path (Critical Path Method)**
