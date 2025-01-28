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

#### Advantages
- Easier to implement for problems where recursion naturally fits (e.g., tree traversal).
- Can handle irregular or non-linear sub-problem dependencies effectively.
  
#### Disadvantages
- Higher memory usage due to recursive stack calls.
- Slower compared to bottom-up approaches if the problem has significant overlapping sub-problems and a high recursion depth.
It starts solving the problem from the top (main problem) and breaks it into smaller sub-problems.

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
A DP table is a 2D or 1D array used to store the results of sub-problems. While it helps avoid redundant calculations, it can increase space complexity significantly, especially for problems with large inputs. This can be mitigated using techniques like a rolling array, which reduces the storage requirement by only keeping track of the most recent rows or columns of the table, depending on the problem. This helps in avoiding redundant calculations by reusing precomputed values.

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
Dynamic programming is often combined with backtracking to reconstruct the solution from the DP table. Backtracking complements dynamic programming by tracing the path of decisions that led to the optimal solution, helping to extract the actual set of choices (or sequences) contributing to the result. This process is particularly important in optimization problems where not only the value of the solution but also the specific elements forming it are needed.

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
#### Importance of Backtracking in DP
- Reconstructing Solutions: In problems like the Longest Common Subsequence (LCS) or the Knapsack problem, backtracking identifies the sequence of decisions.
- Understanding Problem Structure: It aids in debugging and verifying the correctness of the DP table.
- Applicability Beyond DP: Backtracking is used in other algorithmic techniques, such as DFS, to explore all potential solutions systematically before committing to an optimal one.

## Applications
- Longest Common Subsequence (LCS)
- Shortest Path Problems (e.g., Floyd-Warshall)
- Matrix Chain Multiplication
- Subset Sum Problem

---

### Warmups
[Problem 1: Climbing Stairs](https://github.com/organizedanvrchy/LeetCode/blob/main/Climbing_Stairs.py) <br>
[Problem 2: Min Path Sum](https://github.com/organizedanvrchy/LeetCode/blob/main/Min_Path_Sum.py) <br>

### Session #1


### Session #2

