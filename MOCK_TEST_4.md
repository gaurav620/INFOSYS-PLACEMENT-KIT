# 📝 Infosys SP/DSE Mock Test 4

**Duration: 3 Hours | 4 Questions | Languages: Python, C++, Java**

---

## Easy : Maximum Sliding Window

You have an array of N integers and a window of size K. The window slides from left to right, one position at a time.

For each window position, find the **maximum element** in the window.

Output all the maximums.

### Input Format
The first line contains an integer, n, denoting the size of the array.
The next line contains an integer, k, denoting the window size.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

### Constraints
1 <= k <= n <= 10^5
-10^9 <= arr[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
8
3
1
3
-1
-3
5
3
6
7
```
Output:
```
3 3 5 5 6 7
```
Explanation:
Window [1,3,-1] → max=3
Window [3,-1,-3] → max=3
Window [-1,-3,5] → max=5
Window [-3,5,3] → max=5
Window [5,3,6] → max=6
Window [3,6,7] → max=7

**Case 2**

Input:
```
4
4
9
8
7
6
```
Output:
```
9
```
Explanation:
Only one window of size 4: max = 9.

**Case 3**

Input:
```
5
1
5
4
3
2
1
```
Output:
```
5 4 3 2 1
```
Explanation:
Window size 1 → each element is its own max.

---

### ✅ ANSWER — Maximum Sliding Window

**🧠 Approach: Monotonic Deque**

**Kaise socha?**
- Brute force: har window mein max dhundho → O(n×k) → slow
- Trick: ek deque maintain karo jo **decreasing order** mein indices rakhta hai
- Naya element aaya → peeche se chhote elements hatao
- Front se purane elements hatao (window se bahar)
- Front hamesha current window ka max hoga

```python
from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    arr = [int(input()) for _ in range(n)]
    
    dq = deque()  # Stores indices
    result = []
    
    for i in range(n):
        # Remove elements outside window from front
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove smaller elements from back (they'll never be max)
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # Window is complete from index k-1
        if i >= k - 1:
            result.append(str(arr[dq[0]]))
    
    print(' '.join(result))

solve()
```

**Time: O(n) | Space: O(k)**

**🔑 Pattern: "Sliding window max/min" → Monotonic Deque**
- Max chahiye → decreasing deque maintain karo
- Min chahiye → increasing deque maintain karo

---

## Medium : Job Scheduling Profit

You have N jobs. Each job has a start time, end time, and profit. You can only do **one job at a time** (no overlapping).

Find the **maximum total profit** you can earn.

### Input Format
The first line contains an integer, n, denoting the number of jobs.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains three space-separated integers describing start[i], end[i], profit[i].

### Constraints
1 <= n <= 10^5
1 <= start[i] < end[i] <= 10^9
1 <= profit[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
1 2 50
3 5 20
6 19 100
2 100 200
```
Output:
```
250
```
Explanation:
Pick job 0 (1-2, profit 50) and job 3 (2-100, profit 200)? No, they overlap at time 2.
Pick job 0 (1-2, profit 50) and job 3 (2-100, profit 200): end of job 0 = 2, start of job 3 = 2 → no overlap!
Total = 50 + 200 = 250.

**Case 2**

Input:
```
3
1 3 10
2 5 20
4 6 30
```
Output:
```
40
```
Explanation:
Job 0 (10) + Job 2 (30) = 40 (no overlap since job 0 ends at 3, job 2 starts at 4).
Or just job 1 (20) → less.

**Case 3**

Input:
```
2
1 5 100
1 5 200
```
Output:
```
200
```
Explanation:
Both jobs overlap. Pick the more profitable one.

---

### ✅ ANSWER — Job Scheduling Profit

**🧠 Approach: Sort by end time + DP + Binary Search**

**Kaise socha?**
- "Non-overlapping items, maximize profit" → Weighted Interval Scheduling
- Sort by end time
- dp[i] = max profit considering first i jobs
- For each job: either skip it, or take it + best non-overlapping previous job
- Binary search to find last non-overlapping job

```python
from bisect import bisect_right
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    jobs = []
    for _ in range(n):
        s, e, p = map(int, input().split())
        jobs.append((s, e, p))
    
    # Sort by end time
    jobs.sort(key=lambda x: x[1])
    
    ends = [job[1] for job in jobs]
    dp = [0] * (n + 1)  # dp[i] = max profit from first i jobs
    
    for i in range(1, n + 1):
        start_i, end_i, profit_i = jobs[i - 1]
        
        # Option 1: Skip this job
        skip = dp[i - 1]
        
        # Option 2: Take this job
        # Find last job that ends <= start of current job
        # bisect_right gives first index where end > start_i
        idx = bisect_right(ends, start_i, 0, i - 1)
        take = dp[idx] + profit_i
        
        dp[i] = max(skip, take)
    
    print(dp[n])

solve()
```

**Time: O(n log n) | Space: O(n)**

**🔑 Pattern: "Max profit from non-overlapping intervals" → Sort + DP + Binary Search**

---

## Hard : Edit Distance

Given two strings word1 and word2. Find the **minimum number of operations** to convert word1 into word2.

Allowed operations (each costs 1):
- **Insert** a character
- **Delete** a character
- **Replace** a character

### Input Format
The first line contains a string word1.
The second line contains a string word2.

### Constraints
0 <= len(word1), len(word2) <= 500

### Sample Test Cases

**Case 1**

Input:
```
horse
ros
```
Output:
```
3
```
Explanation:
horse → rorse (replace h with r)
rorse → rose (remove r)
rose → ros (remove e)
3 operations.

**Case 2**

Input:
```
intention
execution
```
Output:
```
5
```
Explanation:
intention → inention (remove t)
inention → enention (replace i with e)
enention → exention (replace n with x)
exention → exection (replace n with c)
exection → execution (insert u)
5 operations.

**Case 3**

Input:
```
abc
abc
```
Output:
```
0
```
Explanation:
Already same. 0 operations.

---

### ✅ ANSWER — Edit Distance

**🧠 Approach: 2D DP (Classic)**

**Kaise socha?**
- Two strings compare karna hai → 2D DP usually
- dp[i][j] = min operations to convert word1[0..i-1] to word2[0..j-1]
- If word1[i-1] == word2[j-1]: no operation needed → dp[i-1][j-1]
- Else: try insert, delete, replace → 1 + min of three

```python
import sys
input = sys.stdin.readline

def solve():
    word1 = input().strip()
    word2 = input().strip()
    
    m, n = len(word1), len(word2)
    
    # dp[i][j] = edit distance of word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # No operation
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete from word1
                    dp[i][j - 1],      # Insert into word1
                    dp[i - 1][j - 1]   # Replace
                )
    
    print(dp[m][n])

solve()
```

**Time: O(m × n) | Space: O(m × n)**

**🔑 Pattern: "Convert string A to string B with min operations" → Edit Distance DP**
- 2D table, compare character by character
- 3 choices: insert, delete, replace

---

## Complex : Cycle Detection in Directed Graph

You have N nodes (0 to N-1) and M directed edges. Determine if the graph contains a **cycle**.

If a cycle exists, output "YES". Otherwise, output "NO".

### Input Format
The first line contains an integer, n, denoting the number of nodes.
The next line contains an integer, m, denoting the number of edges.
Each line i of the m subsequent lines (where 0 ≤ i < m) contains two space-separated integers describing u, v (edge from u to v).

### Constraints
1 <= n <= 10^5
1 <= m <= 10^5
0 <= u, v < n

### Sample Test Cases

**Case 1**

Input:
```
4
4
0 1
1 2
2 3
3 1
```
Output:
```
YES
```
Explanation:
Cycle: 1 → 2 → 3 → 1

**Case 2**

Input:
```
3
2
0 1
1 2
```
Output:
```
NO
```
Explanation:
No cycle exists. Linear path 0 → 1 → 2.

**Case 3**

Input:
```
2
2
0 1
1 0
```
Output:
```
YES
```
Explanation:
Cycle: 0 → 1 → 0

---

### ✅ ANSWER — Cycle Detection in Directed Graph

**🧠 Approach: DFS with 3 Colors**

**Kaise socha?**
- Directed graph mein cycle = back edge milna DFS mein
- 3 states for each node:
  - WHITE (0) = not visited
  - GRAY (1) = currently in DFS stack (being processed)
  - BLACK (2) = fully processed
- Agar GRAY node pe wapas pahunche → CYCLE!

```python
from collections import defaultdict
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    
    adj = defaultdict(list)
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = [WHITE] * n
    
    def dfs(u):
        color[u] = GRAY
        for v in adj[u]:
            if color[v] == GRAY:
                return True   # Back edge → cycle found!
            if color[v] == WHITE:
                if dfs(v):
                    return True
        color[u] = BLACK
        return False
    
    for node in range(n):
        if color[node] == WHITE:
            if dfs(node):
                print("YES")
                return
    
    print("NO")

solve()
```

**Time: O(V + E) | Space: O(V + E)**

**🔑 Pattern: "Cycle in directed graph" → DFS with 3 colors (WHITE/GRAY/BLACK)**
- Undirected graph cycle → Union-Find ya simple DFS (parent tracking)
- Directed graph cycle → 3-color DFS
- Alternative: Kahn's Algorithm (topological sort) — if topo sort covers all nodes → no cycle
