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
