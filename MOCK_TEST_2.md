# 📝 Infosys SP/DSE Mock Test 2

**Duration: 3 Hours | 4 Questions | Languages: Python, C++, Java**

---

## Easy : Candy Distribution

You are a teacher with N students standing in a line. Each student has a rating.
You must give candies to students following these rules:
1. Every student must get at least 1 candy.
2. A student with a **higher rating** than their neighbor must get **more candies** than that neighbor.

Find the **minimum total number of candies** you need.

### Input Format
The first line contains an integer, n, denoting the number of students.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing rating[i].

### Constraints
1 <= n <= 10^5
1 <= rating[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
3
1
0
2
```
Output:
```
5
```
Explanation:
Ratings: [1, 0, 2]
- Student 0 (rating 1): higher than student 1 (rating 0) → needs more than student 1
- Student 1 (rating 0): lowest → gets 1 candy
- Student 2 (rating 2): higher than student 1 → needs more than student 1
Candies: [2, 1, 2] → Total = 5

**Case 2**

Input:
```
4
1
2
3
4
```
Output:
```
10
```
Explanation:
Strictly increasing → [1, 2, 3, 4] → Total = 10

**Case 3**

Input:
```
5
1
3
2
2
1
```
Output:
```
7
```
Explanation:
Candies: [1, 2, 1, 2, 1] → but wait, student 3 (rating 2) = student 2 (rating 2), equal rating means no rule applies.
So: [1, 2, 1, 2, 1] → Total = 7

---

### ✅ ANSWER — Candy Distribution

**🧠 Approach: Two-Pass Greedy**

**Kaise socha?**
- Ek taraf se dekhein toh left neighbor se compare karna hai
- Doosri taraf se dekhein toh right neighbor se compare karna hai
- **Solution: Left-to-right pass + Right-to-left pass, take max**

**Steps:**
1. Sabko 1 candy do
2. Left → Right: agar rating[i] > rating[i-1] → candy[i] = candy[i-1] + 1
3. Right → Left: agar rating[i] > rating[i+1] → candy[i] = max(candy[i], candy[i+1] + 1)

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    rating = [int(input()) for _ in range(n)]
    
    candy = [1] * n
    
    # Left to Right pass
    for i in range(1, n):
        if rating[i] > rating[i - 1]:
            candy[i] = candy[i - 1] + 1
    
    # Right to Left pass
    for i in range(n - 2, -1, -1):
        if rating[i] > rating[i + 1]:
            candy[i] = max(candy[i], candy[i + 1] + 1)
    
    print(sum(candy))

solve()
```

**Time: O(n) | Space: O(n)**

**🔑 Pattern: "Both neighbors matter" → Two-pass greedy (left-to-right + right-to-left)**

---

## Medium : Water Container

You have N vertical lines on x-axis. Line i has height h[i] and is at position i.

Choose two lines to form a container. The container holds water = **min(h[i], h[j]) × (j - i)**.

Find the **maximum water** the container can hold.

### Input Format
The first line contains an integer, n, denoting the number of lines.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing h[i].

### Constraints
2 <= n <= 10^5
1 <= h[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
9
1
8
6
2
5
4
8
3
7
```
Output:
```
49
```
Explanation:
Lines at index 1 (height 8) and index 8 (height 7):
Water = min(8, 7) × (8 - 1) = 7 × 7 = 49

**Case 2**

Input:
```
2
1
1
```
Output:
```
1
```
Explanation:
Only two lines: min(1,1) × (1-0) = 1

**Case 3**

Input:
```
4
4
3
2
1
```
Output:
```
4
```
Explanation:
Best: index 0 (h=4) and index 2 (h=2): min(4,2) × 2 = 4
Or: index 0 (h=4) and index 1 (h=3): min(4,3) × 1 = 3
Or: index 0 (h=4) and index 3 (h=1): min(4,1) × 3 = 3
Maximum = 4

---

### ✅ ANSWER — Water Container

**🧠 Approach: Two Pointers**

**Kaise socha?**
- Brute force: try all pairs → O(n²) → TLE for n=10^5
- Width maximum hai jab left=0, right=n-1
- Ab width kam karni padegi, toh height badhani chahiye
- **Chhoti height wali side ko move karo** (badi side move karne se kuch nahi milega)

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    h = [int(input()) for _ in range(n)]
    
    left = 0
    right = n - 1
    max_water = 0
    
    while left < right:
        # Current container
        water = min(h[left], h[right]) * (right - left)
        max_water = max(max_water, water)
        
        # Move the shorter side
        if h[left] < h[right]:
            left += 1
        else:
            right -= 1
    
    print(max_water)

solve()
```

**Time: O(n) | Space: O(1)**

**🔑 Pattern: "Two elements optimize something" + sorted/indexed → Two Pointers**

---

## Hard : Coin Change Ways

You have N types of coins with values coin[i]. You have an unlimited supply of each type.

Find the **number of distinct ways** to make a total of amount S using these coins.

Two ways are different if they use a different count of any coin type.

### Input Format
The first line contains an integer, n, denoting the number of coin types.
The next line contains an integer, s, denoting the target amount.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing coin[i].

### Constraints
1 <= n <= 300
1 <= s <= 5000
1 <= coin[i] <= 5000

### Sample Test Cases

**Case 1**

Input:
```
3
5
1
2
5
```
Output:
```
4
```
Explanation:
Ways to make 5:
1. 5 = 5
2. 5 = 2 + 2 + 1
3. 5 = 2 + 1 + 1 + 1
4. 5 = 1 + 1 + 1 + 1 + 1
Total = 4 ways

**Case 2**

Input:
```
2
3
1
2
```
Output:
```
2
```
Explanation:
1. 3 = 1 + 1 + 1
2. 3 = 2 + 1
Total = 2 ways

**Case 3**

Input:
```
1
7
3
```
Output:
```
0
```
Explanation:
Cannot make 7 using only coins of value 3.

---

### ✅ ANSWER — Coin Change Ways

**🧠 Approach: Unbounded Knapsack DP**

**Kaise socha?**
- Unlimited supply → Unbounded Knapsack
- "Number of ways" → DP count problem
- State: dp[amount] = number of ways to make this amount
- Process coin by coin (NOT amount by amount) → avoids counting permutations

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = int(input())
    coins = [int(input()) for _ in range(n)]
    
    # dp[j] = number of ways to make amount j
    dp = [0] * (s + 1)
    dp[0] = 1  # 1 way to make 0: use no coins
    
    # Process coin by coin (important! avoids duplicate counting)
    for coin in coins:
        for j in range(coin, s + 1):
            dp[j] += dp[j - coin]
    
    print(dp[s])

solve()
```

**Time: O(n × s) | Space: O(s)**

**🔑 Pattern: "Count ways with unlimited items" → Unbounded Knapsack**
- **Combinations** (not permutations): outer loop = coins, inner loop = amounts
- **Permutations**: outer loop = amounts, inner loop = coins

---

## Complex : Network Delay

You have N servers numbered 0 to N-1. There are M one-way connections between servers. Each connection from server u to server v has a delay time w.

You send a signal from server **source**. Find the **minimum time** for the signal to reach **ALL** servers. If any server is unreachable, output -1.

### Input Format
The first line contains an integer, n, denoting the number of servers.
The next line contains an integer, m, denoting the number of connections.
The next line contains an integer, source, denoting the source server.
Each line i of the m subsequent lines (where 0 ≤ i < m) contains three space-separated integers describing u, v, w (connection from u to v with delay w).

### Constraints
1 <= n <= 10^5
1 <= m <= 10^5
0 <= source < n
0 <= u, v < n
1 <= w <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
4
0
0 1 1
0 2 4
1 2 2
2 3 1
```
Output:
```
4
```
Explanation:
From server 0:
- To server 1: direct = 1
- To server 2: via 1 = 1+2=3 (better than direct 4)
- To server 3: via 1,2 = 1+2+1=4
All servers reached. Maximum delay = 4.

**Case 2**

Input:
```
3
2
0
0 1 5
0 2 10
```
Output:
```
10
```
Explanation:
From 0: to 1 = 5, to 2 = 10. Max = 10.

**Case 3**

Input:
```
3
1
0
0 1 3
```
Output:
```
-1
```
Explanation:
Server 2 is unreachable from server 0.

---

### ✅ ANSWER — Network Delay

**🧠 Approach: Dijkstra's Algorithm**

**Kaise socha?**
- "Shortest path from one source to all" → **Single Source Shortest Path**
- All weights positive → **Dijkstra** (not Bellman-Ford)
- Answer = maximum of all shortest distances (slowest server decides total time)

```python
import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    source = int(input())
    
    adj = defaultdict(list)
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
    
    # Dijkstra
    INF = float('inf')
    dist = [INF] * n
    dist[source] = 0
    pq = [(0, source)]  # (distance, node)
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > dist[u]:
            continue  # Already found shorter path
        
        for v, w in adj[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    
    # Check if all reachable
    max_dist = max(dist)
    if max_dist == INF:
        print(-1)
    else:
        print(max_dist)

solve()
```

**Time: O((V + E) log V) | Space: O(V + E)**

**🔑 Pattern: "Shortest path from source" + positive weights → Dijkstra**
- Negative weights → Bellman-Ford
- All pairs → Floyd-Warshall
- Unweighted → BFS
