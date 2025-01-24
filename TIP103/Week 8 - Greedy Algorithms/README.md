# Dynamic Programming (DP)
Dynamic programming is a method for solving complex problems by breaking them down into simpler sub-problems. It is particularly useful for optimization problems and problems with overlapping sub-problems.

## Key Concepts
### Top-Down Approach
This approach uses recursion with memoization to solve problems. It starts solving the problem from the top (main problem) and breaks it into smaller sub-problems.

```python3
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Example usage:
print(fibonacci(10))
```

### Bottom-Up Approach
This approach solves all sub-problems iteratively, starting from the smallest, and uses their solutions to build up solutions to larger sub-problems.

```python3
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage:
print(fibonacci(10))
```

### Dynamic Programming Table
A DP table is a 2D or 1D array used to store the results of sub-problems. This helps in avoiding redundant calculations by reusing precomputed values.

```python3
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack(values, weights, capacity))
```

### Backtracking
Dynamic programming is often combined with backtracking to reconstruct the solution from the DP table.

```python3
def knapsack_with_items(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtracking to find items included
    w = capacity
    items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], items

# Example usage:
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
print(knapsack_with_items(values, weights, capacity))
```


## Applications
- Longest Common Subsequence (LCS)
- Shortest Path Problems (e.g., Floyd-Warshall)
- Matrix Chain Multiplication
- Subset Sum Problem

---

# Greedy Algorithms
Greedy algorithms employ a series of choices by selecting the locally optimal option at each step, with the hope of arriving at a globally optimal solution. These algorithms are often used in optimization problems that require immediate, short-term decisions.

## Key Characteristics
### Greedy Choice Pattern
The algorithm makes a choice that seems best at that moment in each step without worrying about future consequences. This implies that selecting the local optimal solutions can result in a global optimal solution.

### Optimal Substructure
Problems solved using this algorithm exhibit an optimal substructure if an optimal solution to the problem contains optimal solutions to its sub-problems.

## Design
To design a greedy algorithm, the following steps are typically followed:

- Define the Problem and Choices: <br>
  Understand the problem requirements and list possible choices at each step.

- Choose a Greedy Strategy: <br>
  Identify a rule to make the best local choice at each step.

- Prove Optimality: <br>
  Demonstrate that the greedy choice will always lead to a globally optimal solution. (This can often be proven mathematically.)

- Implement the Algorithm: <br>
  Write the code to apply the greedy approach.
  
## Advantages and Disadvantages
### Advantages
- Simple to implement.

- Efficient with better time complexities compared to other algorithms like dynamic programming in certain problems.

### Disadvantages
- May not always provide the optimal solution.

- Local greedy solutions can lead to suboptimal global results in some cases.

## Common Applications
### Dijkstra's Algorithm
Finding the shortest path in a graph from a starting vertex to all other vertices.

```python3
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(dijkstra(graph, 'A'))
```

### Prim's and Kruskal's Algorithms
Finding the minimum spanning tree (MST) of a weight, connected graph.

```python3
import heapq

def prim(graph):
    start = next(iter(graph))  # Pick an arbitrary starting node
    mst = []
    visited = set()
    min_heap = [(0, start, None)]  # (weight, node, parent)

    while min_heap:
        weight, current_node, parent = heapq.heappop(min_heap)
        if current_node in visited:
            continue

        visited.add(current_node)
        if parent:
            mst.append((parent, current_node, weight))

        for neighbor, edge_weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return mst

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
print(prim(graph))
```

### Fractional Knapsack Problem
Maximizing the total value of items placed in a weight-limited knapsack, allowing for fractional parts of items. 

```python3
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[2], reverse=True)

    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# Example usage:
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50
print(fractional_knapsack(items, capacity))
```

### Activity Selection[^1]
Selecting the maximum number of non-overlapping activities from a list, where each activity has a start and end time.

```python3
def activity_selection(activities):
    # Sort activities by their finish times
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end_time = 0

    for start, end in activities:
        if start >= last_end_time:
            selected.append((start, end))
            last_end_time = end

    return selected

# Example usage:
activities = [(1, 3), (2, 5), (4, 7), (6, 8), (5, 9)]
print(activity_selection(activities))
```

### Huffman Coding[^2]
Constructing an optimal binary prefix code to compress data, where more frequent characters have shorter codes.

```python3
import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_codes(node, prefix="", codes={}):
    if node:
        if node.char is not None:
            codes[node.char] = prefix
        build_codes(node.left, prefix + "0", codes)
        build_codes(node.right, prefix + "1", codes)
    return codes

# Example usage:
frequencies = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree = huffman_encoding(frequencies)
codes = build_codes(huffman_tree)
print(codes)
```

---

### Warmups
[Problem 1: Largest Number](https://github.com/organizedanvrchy/LeetCode/blob/main/Largest_Number.py) <br>

### Session #1
[Problem 1: Accounts Merge](https://github.com/organizedanvrchy/LeetCode/blob/main/Accounts_Merge.py) <br>
[Problem 2: Path Sum II](https://github.com/organizedanvrchy/LeetCode/blob/main/Path_Sum_II.py) <br>


### Session #2
[Problem 1: Rabbits in Forest](https://github.com/organizedanvrchy/LeetCode/blob/main/Rabbits_in_Forest.py) <br>

---

[^1]: [GeeksForGeeks - Activity Selection](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)
[^2]: [GeeksForGeeks - Huffman Coding](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)
