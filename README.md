# 🎯 INFOSYS PLACEMENT KIT — SP/DSE Off-Campus 2026

Complete preparation kit for **Infosys Specialist Programmer (SP)** and **Digital Specialist Engineer (DSE)** off-campus recruitment coding round.

## 📊 Test Pattern

| Level | Topics | Time |
|-------|--------|------|
| **Easy** | Greedy, Heap, Sorting, Binary Search | 30 min |
| **Medium** | Kadane's, DP, Sliding Window, Two Pointers | 45 min |
| **Hard** | Graph+DP, Matching, Bitmask DP | 50 min |
| **Complex** | Layered Graph DP, Segment Trees | 55 min |

## 📁 Repository Structure

```
├── README.md
├── PREP_GUIDE.md              # Full preparation guide with expected questions
├── solutions/
│   ├── food_stamps.py         # Easy: Greedy + Binary Search on threshold
│   ├── mss_with_swaps.py      # Medium: Brute-force + Greedy swaps
│   ├── lock_and_parity.py     # Hard: Min even-cost pair matching
│   └── layer_split_path.py    # Complex: Layered Graph DP
└── expected_questions/
    ├── minimize_max_load.py   # Binary Search on Answer
    ├── connect_ropes.py       # Min-Heap Greedy
    ├── max_score_negations.py # Heap
    ├── minimum_platforms.py   # Sweep Line
    ├── partition_max_sum.py   # DP
    └── shortest_path_k_free.py # Modified Dijkstra
```

## ✅ Actual Questions & Solutions

| # | Question | Difficulty | Approach | Status |
|---|----------|-----------|----------|--------|
| 1 | **Food Stamps** | Easy | Binary Search + AP Sum Formula | ✅ All cases pass |
| 2 | **MSS With Swaps** | Medium | O(n³) Brute Force + Greedy Swap | ✅ All cases pass |
| 3 | **Lock & Parity** | Hard | Min Even-Cost Pair (Key Insight) | ✅ All cases pass |
| 4 | **Layer-Split Path** | Complex | Layered Graph DP | ✅ All cases pass |

## 🔮 Expected Questions

| # | Question | Pattern |
|---|----------|---------|
| 1 | Minimize Maximum Load | Binary Search on Answer |
| 2 | Minimum Cost to Connect Ropes | Min-Heap Greedy |
| 3 | Maximum Score with K Negations | Heap |
| 4 | Minimum Platforms | Sweep Line / Events |
| 5 | Partition Array Max Sum | Dynamic Programming |
| 6 | Shortest Path with K Free Passes | Modified Dijkstra |

## 🏆 Quick Tips

1. **Read ALL questions first** (5 min) — identify the Easy one
2. **Python users**: Use `import sys; input = sys.stdin.readline` for fast I/O
3. **Edge cases**: n=1, m=0, all negatives, max constraints
4. **Partial credit counts** — even brute-force on Hard is better than nothing

## 📋 Top Patterns to Know

| Pattern | When to Use |
|---------|-------------|
| Max-Heap Greedy | Repeatedly pick best option |
| Binary Search on Answer | "Minimize max" / "Maximize min" |
| Kadane's Algorithm | Maximum subarray sum |
| 0/1 Knapsack DP | Select items with weight limit |
| Dijkstra's Algorithm | Shortest path weighted graph |
| BFS/DFS | Graph traversal / components |

---

**Good luck! 🚀**
