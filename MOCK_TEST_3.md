# 📝 Infosys SP/DSE Mock Test 3

**Duration: 3 Hours | 4 Questions | Languages: Python, C++, Java**

---

## Easy : Stock Profit

You have the prices of a stock for N days. You can buy the stock on one day and sell it on a **later** day.

Find the **maximum profit** you can make. If no profit is possible, output 0.

### Input Format
The first line contains an integer, n, denoting the number of days.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing price[i].

### Constraints
1 <= n <= 10^5
1 <= price[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
6
7
1
5
3
6
4
```
Output:
```
5
```
Explanation:
Buy on day 1 (price=1), sell on day 4 (price=6). Profit = 6-1 = 5.

**Case 2**

Input:
```
5
7
6
4
3
1
```
Output:
```
0
```
Explanation:
Prices always decrease. No profitable transaction possible.

**Case 3**

Input:
```
3
2
4
1
```
Output:
```
2
```
Explanation:
Buy on day 0 (price=2), sell on day 1 (price=4). Profit = 2.

---

### ✅ ANSWER — Stock Profit

**🧠 Approach: Track minimum price so far**

**Kaise socha?**
- Har din pe socho: agar aaj bechta toh maximum kitna milta?
- Uske liye chahiye: aaj tak ka minimum buy price
- max_profit = max(price[i] - min_price_so_far)

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    prices = [int(input()) for _ in range(n)]
    
    min_price = prices[0]
    max_profit = 0
    
    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - min_price)
        min_price = min(min_price, prices[i])
    
    print(max_profit)

solve()
```

**Time: O(n) | Space: O(1)**

**🔑 Pattern: "Buy low sell high with order constraint" → Track running minimum**

---

## Medium : Subarray Sum Equals K

Given an array of N integers (can be negative) and a target K.

Find the **total number of contiguous subarrays** whose sum equals K.

### Input Format
The first line contains an integer, n, denoting the size of the array.
The next line contains an integer, k, denoting the target sum.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

### Constraints
1 <= n <= 10^5
-10^9 <= k <= 10^9
-1000 <= arr[i] <= 1000

### Sample Test Cases

**Case 1**

Input:
```
4
0
1
-1
1
-1
```
Output:
```
4
```
Explanation:
Subarrays with sum 0: [1,-1], [-1,1], [1,-1], [1,-1,1,-1]
Total = 4

**Case 2**

Input:
```
3
3
1
2
3
```
Output:
```
2
```
Explanation:
[1,2] = 3, [3] = 3 → Total = 2

**Case 3**

Input:
```
3
7
1
2
3
```
Output:
```
0
```
Explanation:
No subarray sums to 7.

---

### ✅ ANSWER — Subarray Sum Equals K

**🧠 Approach: Prefix Sum + HashMap**

**Kaise socha?**
- Brute force: try all subarrays → O(n²) → possible but slow
- Key insight: sum(arr[i..j]) = prefix[j] - prefix[i-1]
- Agar prefix[j] - prefix[i-1] = K → prefix[i-1] = prefix[j] - K
- HashMap mein store karo: kitne baar kaunsa prefix sum aaya hai

```python
import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    arr = [int(input()) for _ in range(n)]
    
    count = 0
    prefix_sum = 0
    # Map: prefix_sum → how many times it appeared
    freq = defaultdict(int)
    freq[0] = 1  # Empty prefix (before array starts)
    
    for num in arr:
        prefix_sum += num
        # How many previous prefixes had sum = prefix_sum - k?
        count += freq[prefix_sum - k]
        freq[prefix_sum] += 1
    
    print(count)

solve()
```

**Time: O(n) | Space: O(n)**

**🔑 Pattern: "Count subarrays with sum = K" → Prefix Sum + HashMap**
- Works for negative numbers too (sliding window won't work here!)

---

## Hard : Longest Increasing Subsequence

Given an array of N integers. Find the length of the **longest strictly increasing subsequence**.

A subsequence is a sequence that can be derived from the array by deleting some (or no) elements **without changing the order** of the remaining elements.

### Input Format
The first line contains an integer, n, denoting the size of the array.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

### Constraints
1 <= n <= 10^5
-10^9 <= arr[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
8
10
9
2
5
3
7
101
18
```
Output:
```
4
```
Explanation:
LIS: [2, 3, 7, 101] or [2, 5, 7, 101] or [2, 3, 7, 18] → length = 4

**Case 2**

Input:
```
5
5
4
3
2
1
```
Output:
```
1
```
Explanation:
Strictly decreasing. Any single element is the longest increasing subsequence.

**Case 3**

Input:
```
6
1
3
5
2
4
6
```
Output:
```
4
```
Explanation:
LIS: [1, 3, 5, 6] or [1, 2, 4, 6] → length = 4

---

### ✅ ANSWER — Longest Increasing Subsequence

**🧠 Approach: Binary Search + Patience Sort**

**Kaise socha?**
- O(n²) DP: dp[i] = LIS ending at i → TLE for n=10^5
- O(n log n) trick: maintain a "tails" array
  - tails[i] = smallest tail element for increasing subsequence of length i+1
  - For each element: binary search where to place it in tails

```python
import bisect
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    
    # tails[i] = smallest ending element of all increasing subsequences of length i+1
    tails = []
    
    for num in arr:
        # Find position where num should go
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            tails.append(num)  # Extend longest subsequence
        else:
            tails[pos] = num   # Replace to keep smallest possible tail
    
    print(len(tails))

solve()
```

**Time: O(n log n) | Space: O(n)**

**🔑 Pattern: "Longest Increasing Subsequence" → Binary Search with tails array**
- `bisect_left` for strictly increasing
- `bisect_right` for non-decreasing

---

## Complex : Island Count

You are given a grid of N rows and M columns. Each cell is either land ('1') or water ('0').

An island is a group of connected land cells. Two cells are connected if they share an **edge** (up, down, left, right — not diagonal).

Find the **total number of islands**.

### Input Format
The first line contains an integer, n, denoting the number of rows.
The next line contains an integer, m, denoting the number of columns.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains m space-separated integers (0 or 1).

### Constraints
1 <= n, m <= 500
grid[i][j] is either 0 or 1

### Sample Test Cases

**Case 1**

Input:
```
4
5
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0
```
Output:
```
1
```
Explanation:
All 1s are connected → 1 island.

**Case 2**

Input:
```
4
5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
```
Output:
```
3
```
Explanation:
Island 1: top-left 2×2 block
Island 2: single cell (2,2)
Island 3: cells (3,3) and (3,4)

**Case 3**

Input:
```
3
3
0 0 0
0 0 0
0 0 0
```
Output:
```
0
```
Explanation:
No land cells → 0 islands.

---

### ✅ ANSWER — Island Count

**🧠 Approach: BFS/DFS Flood Fill**

**Kaise socha?**
- Connected components count karna hai → Graph traversal
- Har unvisited '1' pe BFS/DFS start karo → count++
- Visit karte waqt cell ko '0' mark kardo (ya visited array use karo)

```python
from collections import deque
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    islands = 0
    
    def bfs(si, sj):
        queue = deque([(si, sj)])
        grid[si][sj] = 0  # Mark visited
        while queue:
            i, j = queue.popleft()
            # Check 4 directions
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                    grid[ni][nj] = 0
                    queue.append((ni, nj))
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(i, j)
                islands += 1
    
    print(islands)

solve()
```

**Time: O(n × m) | Space: O(n × m)**

**🔑 Pattern: "Count connected groups in grid" → BFS/DFS Flood Fill**
- Visit karo, mark karo, count karo
- 4-directional = up/down/left/right
- 8-directional = diagonals bhi (problem padho carefully)
