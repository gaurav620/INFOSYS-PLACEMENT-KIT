# 📝 Infosys SP/DSE Mock Test 1

**Duration: 3 Hours | 4 Questions | Languages: Python, C++, Java**

---

## Easy : Rope Connection

You have N ropes of different lengths. You need to connect all ropes into one single rope.

The cost of connecting two ropes is equal to the **sum of their lengths**.

You want to minimize the total cost of connecting all ropes.

### Input Format
The first line contains an integer, n, denoting the number of ropes.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing length[i].

### Constraints
1 <= n <= 10^5
1 <= length[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
4
3
2
6
```
Output:
```
29
```
Explanation:
Step 1: Connect ropes 2 and 3 → new rope = 5, cost = 5
Step 2: Connect ropes 4 and 5 → new rope = 9, cost = 9
Step 3: Connect ropes 6 and 9 → new rope = 15, cost = 15
Total cost = 5 + 9 + 15 = 29

**Case 2**

Input:
```
2
5
10
```
Output:
```
15
```
Explanation:
Only one connection needed: 5 + 10 = 15, cost = 15.

**Case 3**

Input:
```
5
1
2
3
4
5
```
Output:
```
33
```
Explanation:
Step 1: 1 + 2 = 3 (cost 3)
Step 2: 3 + 3 = 6 (cost 6)
Step 3: 4 + 5 = 9 (cost 9)
Step 4: 6 + 9 = 15 (cost 15)
Total = 3 + 6 + 9 + 15 = 33

---

## Medium : Chef's Special

A chef has N dishes. Each dish has a preparation time p[i] and an expiry time e[i].

The chef can only prepare **one dish at a time**. Once the chef starts a dish, it takes exactly p[i] minutes to complete.

A dish must be **completed before or at its expiry time** e[i]. The chef starts at time 0.

Find the **maximum number of dishes** the chef can prepare before they expire.

### Input Format
The first line contains an integer, n, denoting the number of dishes.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains two space-separated integers describing p[i] and e[i].

### Constraints
1 <= n <= 10^5
1 <= p[i] <= e[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
4
1 2
2 4
3 6
4 8
```
Output:
```
3
```
Explanation:
- Dish 1: start=0, end=1 ≤ 2 ✓
- Dish 2: start=1, end=3 ≤ 4 ✓
- Dish 3: start=3, end=6 ≤ 6 ✓
- Dish 4: start=6, end=10 > 8 ✗
Maximum = 3 dishes

**Case 2**

Input:
```
3
3 3
3 3
3 3
```
Output:
```
1
```
Explanation:
All dishes take 3 minutes and expire at time 3.
- Dish 1: start=0, end=3 ≤ 3 ✓
- Dish 2: start=3, end=6 > 3 ✗
Only 1 dish can be prepared.

**Case 3**

Input:
```
5
1 10
2 10
3 10
4 10
5 10
```
Output:
```
4
```
Explanation:
- Dish 1: start=0, end=1 ≤ 10 ✓
- Dish 2: start=1, end=3 ≤ 10 ✓
- Dish 3: start=3, end=6 ≤ 10 ✓
- Dish 4: start=6, end=10 ≤ 10 ✓
- Dish 5: start=10, end=15 > 10 ✗
Maximum = 4 dishes

---

## Hard : Treasure Split

You have an array of N positive integers. You must split this array into **exactly K contiguous subarrays**.

The cost of a subarray is defined as:
**cost = (max element in subarray) - (min element in subarray)**

Find the **minimum possible total cost** (sum of costs of all K subarrays).

### Input Format
The first line contains an integer, n, denoting the size of the array.
The next line contains an integer, k, denoting the number of subarrays.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer describing arr[i].

### Constraints
1 <= k <= n <= 500
1 <= arr[i] <= 10^9

### Sample Test Cases

**Case 1**

Input:
```
5
3
1
5
2
8
3
```
Output:
```
9
```
Explanation:
Split: [1,5,2] [8] [3]
Cost: (5-1) + (8-8) + (3-3) = 4 + 0 + 0 = 4

Wait, can we do better?
Split: [1] [5,2] [8,3]
Cost: (1-1) + (5-2) + (8-3) = 0 + 3 + 5 = 8

Split: [1,5] [2,8] [3]
Cost: (5-1) + (8-2) + (3-3) = 4 + 6 + 0 = 10

Split: [1,5] [2] [8,3]
Cost: (5-1) + (2-2) + (8-3) = 4 + 0 + 5 = 9

Split: [1] [5] [2,8,3]
Cost: 0 + 0 + (8-2) = 6

Split: [1] [5,2,8] [3]
Cost: 0 + (8-2) + 0 = 6

Split: [1] [5,2] [8,3]
Cost: 0 + 3 + 5 = 8

Best: [1] [5] [2,8,3] → cost = 6

Actually checking all: [1,5,2,8] [3] would be k=2, not valid for k=3.

Let me recalculate: minimum total cost = 6

But wait, [1] [5,2] [8,3] = 0+3+5 = 8
[1,5] [2] [8,3] = 4+0+5 = 9
[1] [5] [2,8,3] = 0+0+6 = 6
[1,5,2] [8] [3] = 4+0+0 = 4 ← THIS IS BETTER!

Minimum = 4 ✓

Output: 4

**Case 2**

Input:
```
4
2
3
3
3
3
```
Output:
```
0
```
Explanation:
All elements are same. Any split gives cost = 0.

**Case 3**

Input:
```
6
3
10
1
20
2
30
3
```
Output:
```
30
```
Explanation:
Split: [10,1] [20,2] [30,3]
Cost: (10-1) + (20-2) + (30-3) = 9 + 18 + 27 = 54

Split: [10] [1,20] [2,30,3]
Cost: 0 + 19 + 28 = 47

Split: [10,1,20,2] [30] [3]
Cost: 19 + 0 + 0 = 19 ← Better!

Split: [10,1,20] [2,30] [3]
Cost: 19 + 28 + 0 = 47

Split: [10,1,20] [2] [30,3]
Cost: 19 + 0 + 27 = 46

Split: [10,1] [20,2,30] [3]
Cost: 9 + 28 + 0 = 37

Split: [10] [1,20,2,30] [3]
Cost: 0 + 29 + 0 = 29

Split: [10] [1,20,2] [30,3]
Cost: 0 + 19 + 27 = 46

Split: [10] [1] [20,2,30,3]
Cost: 0 + 0 + 28 = 28

Split: [10,1,20,2] [30] [3] = 19 + 0 + 0 = 19 ← BEST

Output: 19

---

## Complex : Grid Treasure Hunt

You are given a grid of N rows and M columns. Each cell (i,j) has a value grid[i][j] which can be positive (treasure) or negative (trap).

You start at the **top-left corner** (0,0) and want to reach the **bottom-right corner** (N-1, M-1).

At each step, you can move **right** or **down**.

However, you have a special ability: you can use a **shield** at most K times during the journey. When you use a shield on a cell, any negative value becomes 0 (you avoid the trap). Positive values are unaffected by the shield.

Find the **maximum sum** you can collect along any path from (0,0) to (N-1,M-1).

### Input Format
The first line contains an integer, n, denoting the number of rows.
The next line contains an integer, m, denoting the number of columns.
The next line contains an integer, k, denoting the number of shields.
Each line i of the n subsequent lines (where 0 ≤ i < n) contains m space-separated integers describing grid[i][0], grid[i][1], ..., grid[i][m-1].

### Constraints
1 <= n, m <= 200
0 <= k <= n + m
-10^6 <= grid[i][j] <= 10^6

### Sample Test Cases

**Case 1**

Input:
```
2
2
1
1 -5
-3 4
```
Output:
```
5
```
Explanation:
Path right then down: 1 + (-5) + 4 = 0
Path down then right: 1 + (-3) + 4 = 2

With 1 shield:
Path right then down with shield on (-5): 1 + 0 + 4 = 5 ✓
Path down then right with shield on (-3): 1 + 0 + 4 = 5

Maximum = 5

**Case 2**

Input:
```
3
3
0
1 2 3
4 5 6
7 8 9
```
Output:
```
29
```
Explanation:
No shields needed. Best path: 1→4→7→8→9 = 29
Or: 1→2→3→6→9 = 21
Or: 1→4→5→6→9 = 25
Or: 1→4→5→8→9 = 27
Best: 1→4→7→8→9 = 29

**Case 3**

Input:
```
2
3
2
5 -10 3
-10 -10 8
```
Output:
```
16
```
Explanation:
Path: (0,0)→(0,1)→(0,2)→(1,2)
Values: 5 + (-10) + 3 + 8 = 6
With 2 shields on (-10): 5 + 0 + 3 + 8 = 16

Path: (0,0)→(1,0)→(1,1)→(1,2)
Values: 5 + (-10) + (-10) + 8 = -7
With 2 shields: 5 + 0 + 0 + 8 = 13

Maximum = 16
