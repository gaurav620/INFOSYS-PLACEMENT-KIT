# 🧠 Solutions with FULL Thinking Process — Mock Test 1

> Yeh guide tujhe sikhayega ki **question padhke kaise sochna hai**, step-by-step.

---

## 🟢 Easy: Rope Connection

### 📖 Question Samjho:
- N ropes hain, unko ek banana hai
- 2 ropes jodne ka cost = dono ki length ka sum
- Total cost minimize karo

### 🧠 Kaise Sochna Hai (Thinking Process):

**Step 1: Brute Force socho**
- Har baar koi bhi 2 ropes jod sakte hain
- Total combinations bahut zyada — brute force kaam nahi karega

**Step 2: Pattern dekho**
- Agar badi ropes pehle jodo → woh baar baar add hoti rahegi → cost badh jayega
- Example: ropes = [1, 2, 100]
  - Pehle 2+100=102 (cost 102), fir 1+102=103 (cost 103) → total=205
  - Pehle 1+2=3 (cost 3), fir 3+100=103 (cost 103) → total=106
- **INSIGHT: Chhoti ropes pehle jodo!**

**Step 3: Data Structure socho**
- Har step pe 2 sabse chhoti ropes chahiye → **MIN HEAP!**
- Heap se 2 nikalo, jodo, wapas daalo. Repeat.

**Step 4: Complexity check**
- N elements, har step 2 nikalo 1 daalo → N-1 steps
- Har step O(log N) → Total O(N log N) ✓

### ✅ Solution Code:

```python
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    ropes = [int(input()) for _ in range(n)]
    
    if n == 1:
        print(0)
        return
    
    heapq.heapify(ropes)  # Min heap banao
    total_cost = 0
    
    while len(ropes) > 1:
        # 2 sabse chhoti nikalo
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        
        # Jodo
        combined = first + second
        total_cost += combined
        
        # Wapas daalo
        heapq.heappush(ropes, combined)
    
    print(total_cost)

solve()
```

### 🔑 Yaad Rakhne Ki Cheezein:
- **Keyword "minimize cost of combining"** → MIN HEAP
- `heapq` Python mein by default MIN heap hai
- Edge case: n=1 → cost = 0 (kuch jodna hi nahi)

---

## 🟡 Medium: Chef's Special

### 📖 Question Samjho:
- N dishes hain, har dish mein prep time aur expiry time
- Ek time pe ek hi dish bana sakte ho
- Maximum kitne dishes bana sakte ho?

### 🧠 Kaise Sochna Hai:

**Step 1: Yeh problem kahan dekhi hai?**
- "Maximum number of tasks within deadlines" → Classic **GREEDY** problem!
- Similar to "Activity Selection" / "Job Scheduling"

**Step 2: Greedy kaise lagaye?**
- Option A: Sabse chhota prep time pehle? ❌ 
  - Counter: dish(1,2) dish(100,101) → prep time se sort works here
  - But: dish(1,100) dish(2,3) → pehle dish 2 banana chahiye (deadline tight hai)
- Option B: Sabse pehle expire hone wali pehle? ✓
  - **Sort by deadline (expiry time)!**
  - Then greedily pick — agar current time + prep_time ≤ deadline → le lo
  - Agar nahi → skip karo UNLESS tumne pehle koi bada prep time wala liya hai, toh usse hata ke yeh le lo

**Step 3: Optimal Greedy with Heap**
- Deadline se sort karo
- Ek MAX HEAP maintain karo (prep times ke)
- Har dish ke liye:
  - Current time mein prep time add karo
  - Agar time ≤ deadline → heap mein daal do
  - Agar time > deadline → check karo ki heap mein koi bada prep time hai? Haan toh swap karo
- Answer = heap ka size

### ✅ Solution Code:

```python
import heapq
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dishes = []
    for _ in range(n):
        p, e = map(int, input().split())
        dishes.append((e, p))  # (deadline, prep_time)
    
    # Deadline se sort karo
    dishes.sort()
    
    current_time = 0
    # Max heap (negative values because Python has min heap)
    max_heap = []
    
    for deadline, prep_time in dishes:
        current_time += prep_time
        heapq.heappush(max_heap, -prep_time)  # Negative for max heap
        
        # Agar deadline cross ho gayi
        if current_time > deadline:
            # Sabse bade prep time wala nikalo (greedy: biggest waste hatao)
            biggest = -heapq.heappop(max_heap)
            current_time -= biggest
    
    print(len(max_heap))

solve()
```

### 🔑 Yaad Rakhne Ki Cheezein:
- **"Maximum items within deadline"** → Sort by deadline + Greedy
- Max heap isliye ki agar deadline miss ho, toh sabse bada prep time hatao
- Python mein max heap = negative values daal ke min heap use karo

---

## 🔴 Hard: Treasure Split

### 📖 Question Samjho:
- Array ko exactly K contiguous parts mein todo
- Har part ka cost = max - min
- Total cost minimize karo

### 🧠 Kaise Sochna Hai:

**Step 1: Brute force socho**
- N elements, K parts → (N-1) choose (K-1) ways to split
- N=500, K=250 → bahut bada! Brute force nahi chalega.

**Step 2: DP laga sakte hain?**
- **State kya hoga?** dp[i][j] = minimum cost to split first i elements into j parts
- **Transition:** dp[i][j] = min over all split points l (dp[l][j-1] + cost(l+1, i))
- **Base case:** dp[0][0] = 0
- **Answer:** dp[N][K]

**Step 3: Cost function precompute**
- cost(l, r) = max(arr[l..r]) - min(arr[l..r])
- Precompute kar sakte hain O(N²) mein

**Step 4: Complexity**
- States: O(N × K)
- Transition: O(N) per state
- Total: O(N² × K)
- N=500, K=500 → 500 × 500 × 500 = 1.25 × 10^8 → tight but possible

### ✅ Solution Code:

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    k = int(input())
    arr = [int(input()) for _ in range(n)]
    
    # Precompute cost(l, r) = max - min for arr[l..r]
    # Using 0-indexed
    cost = [[0] * n for _ in range(n)]
    for i in range(n):
        mn = mx = arr[i]
        for j in range(i, n):
            mn = min(mn, arr[j])
            mx = max(mx, arr[j])
            cost[i][j] = mx - mn
    
    # DP
    INF = float('inf')
    # dp[i][j] = min cost to partition arr[0..i-1] into j groups
    dp = [[INF] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):       # first i elements
        for j in range(1, k + 1):   # j groups
            # Last group is arr[l..i-1] for some l
            for l in range(j - 1, i):  # need at least j-1 elements before
                if dp[l][j - 1] < INF:
                    dp[i][j] = min(dp[i][j], dp[l][j - 1] + cost[l][i - 1])
    
    print(dp[n][k])

solve()
```

### 🔑 Yaad Rakhne Ki Cheezein:
- **"Split array into K parts, minimize/maximize cost"** → PARTITION DP
- State: dp[i][j] = first i elements, j groups
- Transition: try every possible last cut point
- Cost function precompute karo pehle

---

## 🟣 Complex: Grid Treasure Hunt

### 📖 Question Samjho:
- Grid mein (0,0) se (N-1,M-1) jaana hai
- Right ya down ja sakte ho
- K baar shield use karke negative values ko 0 bana sakte ho
- Maximum sum find karo

### 🧠 Kaise Sochna Hai:

**Step 1: Without shield yeh kya hai?**
- Simple grid DP! dp[i][j] = max sum to reach (i,j)
- Transition: dp[i][j] = grid[i][j] + max(dp[i-1][j], dp[i][j-1])

**Step 2: Shield add karne se kya badla?**
- Ab state mein track karna padega: kitne shields use kiye
- **New state:** dp[i][j][s] = max sum to reach (i,j) using s shields

**Step 3: Transition with shield**
- Option 1: Shield use nahi karo → value = grid[i][j]
- Option 2: Shield use karo (agar grid[i][j] < 0 aur s > 0) → value = 0
- dp[i][j][s] = max of:
  - dp[i-1][j][s] + grid[i][j]  (from top, no shield)
  - dp[i][j-1][s] + grid[i][j]  (from left, no shield)
  - dp[i-1][j][s-1] + 0  (from top, use shield on negative cell)
  - dp[i][j-1][s-1] + 0  (from left, use shield on negative cell)

**Step 4: Complexity check**
- States: N × M × K → 200 × 200 × 400 = 16,000,000
- That's 1.6 × 10^7 → OK!

### ✅ Solution Code:

```python
import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    m = int(input())
    k = int(input())
    
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    # K ko cap karo — max shields useful = total negative cells on path
    # Path length = n + m - 1, max useful shields = n + m - 1
    k = min(k, n + m - 1)
    
    # dp[i][j][s] = max sum at (i,j) with s shields used
    NEG_INF = float('-inf')
    dp = [[[NEG_INF] * (k + 1) for _ in range(m)] for _ in range(n)]
    
    # Base case: starting cell (0,0)
    dp[0][0][0] = grid[0][0]
    if grid[0][0] < 0 and k > 0:
        dp[0][0][1] = 0  # Use shield on starting cell
    
    # Fill DP
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            
            for s in range(k + 1):
                best = NEG_INF
                
                # Come from top (i-1, j)
                if i > 0 and dp[i-1][j][s] != NEG_INF:
                    best = max(best, dp[i-1][j][s] + grid[i][j])
                
                # Come from left (i, j-1)
                if j > 0 and dp[i][j-1][s] != NEG_INF:
                    best = max(best, dp[i][j-1][s] + grid[i][j])
                
                dp[i][j][s] = max(dp[i][j][s], best)
                
                # Now try using shield on this cell (only if negative)
                if grid[i][j] < 0 and s > 0:
                    best_shield = NEG_INF
                    
                    if i > 0 and dp[i-1][j][s-1] != NEG_INF:
                        best_shield = max(best_shield, dp[i-1][j][s-1] + 0)
                    
                    if j > 0 and dp[i][j-1][s-1] != NEG_INF:
                        best_shield = max(best_shield, dp[i][j-1][s-1] + 0)
                    
                    dp[i][j][s] = max(dp[i][j][s], best_shield)
    
    # Answer: max over all shield counts at destination
    ans = NEG_INF
    for s in range(k + 1):
        ans = max(ans, dp[n-1][m-1][s])
    
    print(ans)

solve()
```

### 🔑 Yaad Rakhne Ki Cheezein:
- **Grid path + extra resource** → Add dimension to DP
- dp[i][j] becomes dp[i][j][shields_used]
- Shield sirf negative cells pe use karo (positive pe koi fayda nahi)
- K ko cap karo (path length se zyada shields useless)

---

# 📌 Pattern Recognition Cheat Sheet

| Question mein yeh dikhe | → Yeh approach use karo |
|------------------------|------------------------|
| "Minimize cost of combining/merging" | **Min Heap** |
| "Maximum tasks within deadlines" | **Sort by deadline + Greedy + Heap** |
| "Split array into K parts, minimize cost" | **Partition DP: dp[i][j]** |
| "Grid path with limited resource" | **3D DP: dp[i][j][resource]** |
| "Maximum subarray sum" | **Kadane's Algorithm** |
| "Minimize the maximum" or "Maximize the minimum" | **Binary Search on Answer** |
| "Buy items with diminishing returns" (like Food Stamps) | **Binary Search on threshold** |
| "Swap elements to maximize subarray" | **Try all subarrays + Greedy swap** |
| "Assignment with parity constraint" (like Lock & Parity) | **Find mathematical insight first** |
| "Path in graph with non-decreasing property" | **Layered DP, process by layer** |
