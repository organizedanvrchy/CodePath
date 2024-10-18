# Big O Complexity Analysis
This notation is most often used when describing the time and space complexities of algorithms. In this case, __time__ refers to _how long it takes the algorithm to complete_ and __space__ refers to _how much memory the algorithm uses during execution_. Hence, Big-O notation is a standardized way of measuring the _efficiency_ of an algorithm, whereby; it represents the __worst case__ or __upper bound__ time complexity. Big-O notation is denoted as: __O(f(n))__ where __f(n)__ often represents the __number of steps__ that an algorithm takes to solve a problem of size n.[^1]

## Important Properties
### 1. Non-negativity
   - The growth rate described by Big-O notation is always non-negative.
### 2. Transitivity
   - If f(n) is in O(g(n)) and g(n) is in O(h(n)), then __f(n) is also in O(h(n))__.
### 3. Constants are Ignored
   - e.g. O(2n) is expressed as O(n).
### 4. Sum Rule
   - If f(n) is in O(g(n)) and h(n) is in O(g(n)), then __f(n) + h(n) = O(g(n))__.
### 5. Product Rule
   - If f(n) is in O(g(n)) and h(n) is in O(k(n)), then __f(n) * h(n) = O(g(n) * (k(n))__.
### 6. Composition Rule
   - If f(n) is in O(g(n)) and g(n) is in O(h(n)), then __f(g(n)) = O(h(n))__.
  
## Common Big-O Notations
### 1. Constant Time Complexity: O(1)
   - This notation refers to algorithms that take the same amount of time to complete, while ignoring the input size. Essentially, they only take "one" step.
### 2. Linear Time Complexity: O(n)
   - This notation indicates that the running time of an algorithm grows linearly with the input size. The algorithm performs the same set of steps for each input element.
### 3. Logarithmic Time Complexity: O(logn)
   - This notation refers to algorithms that have running times that grow logarithmically relative to their input size. This is common for algorithms such as Divide and Conquer and Binary Search.
### 4. Linearithmic Time Complexity: O(nlogn)
   - This notation describes an algorithm with a running time that grows proportionally to the input size * the logarithm of the input size. This is common for many Divide and Conquer algorithms and for Merge Sort, Quick Sort, and Heap sort. 
### 5. Quadratic Time Complexity: O(n<sup>2</sup>) 
   - This notation indicates that the performance of algorithm is directly proportional to the square of the input size. This is the common runtime for nested loops, graphing problems, and sorting algorithms (such as Bubble Sort, Selection Sort, and Insertion Sort).
### 6. Cubic Time Complexity: O(n<sup>3</sup>)
   - This notation indicates that the performance of algorithm is directly proportional to the cube of the input size. This is common in matrix multiplication algorithms.
### 7. Exponential Time Complexity: O(2<sup>n</sup>)
   - This notation refers to algorithms with running times that double with each addition to input size. This is common in Recursive algorithms, Tree Depth algorithms, or Brute Force algorithms.
### 8. Factorial Time Complexity: O(n!)
   - This notation indicates that the algorithm grows factorially with the size of the input. This is common in algorithms that have to generate all permutations of a data set.

<picture>
   <img alt="Shows an illustrated sun in light mode and a moon with stars in dark mode." src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/mypic.png">
</picture>

> [!NOTE]
> Images and further explanations can be found at GeeksForGeeks (Link in footnotes)

# Recursion with Memoization
## Recursion
This is when a function calls itself directly or indirectly for the purpose of breaking a component down into smaller components (to solve a problem). Recursion usually allows for simple and elegant code but can often be less efficient than iterative solutions, consume stack space, and perform redudant calculations.[^2] Recursive solutions are generally composed of __3__ key components:
### 1. Base Case
   - This is the condition that stops recursion when met. Must be included to prevent infinite recursion and stack overflow.
### 2. Recursive Case
   - This is the logic portion of the recursive function that breaks the problem into subproblems and gradually moves towards the base case.
### 3. Call Stack
   - This exists to keep track of each call of a recursive function, where when the base case is reached, the calls are resolves in reverse order (LIFO).

### e.g. Calculating the Fibonacci Sequence (in Python)
```python3
def fibonacci(n):
    if n <= 1:  # Base case
        return n
    else:  # Recursive Case
        return fibonacci(n - 1) + fibonacci(n - 2)
```
### Tail Recursion
A special case of recursion to improve performance, where the recursive call is the last operation in the function.
```python3
def tail_recursive_fib(n, a=0, b=1):
    if n == 0:
        return a
    return tail_recursive_fib(n - 1, b, a + b)  # Tail call
```

## Memoization
This is an optimization technique, particularly useful in recursion, that improves the efficiency of algorithms by storing computation results in a cache (temporary data store) and then retrieving the same information from the cache when same inputs occur again. This technique maintains the simple implementation found in recursion while siginificantly improving the efficiency of the algorithm, but can cause increased memory consumption due to creation of a cache.[^3] The __3__ main concepts of Memoization are:
### 1. Storage of Results 
   - The output of each function call is stored in a cache, which can be a hash table or dictionary. This allows for reusability of the stored results when/if the algorithm encounters the same inputs.
### 2. Avoiding Redundancy
   - Prevents recomputation of results for same inputs.
### 3. Implementation
   - This can be manually implemented rather easily.
### e.g. Calculating the Fibonacci Sequence with Memoization (in Python)
```python3
def fibonacci_memo(n, memo={}):
    if n in memo:  # Check if result is already computed
        return memo[n]
    if n <= 1:  # Base case
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)  # Store result
    return memo[n]
```
## Practice Questions
### Warmups
[Problem 1: Add Two Numbers](https://github.com/organizedanvrchy/LeetCode/blob/main/Add_Two_Numbers.py)<br>
[Problem 2: Decode String](https://github.com/organizedanvrchy/LeetCode/blob/main/Decode_String.py)

### Session #1
[Problem 1: Substring](https://github.com/organizedanvrchy/CodePath/blob/main/TIP103/Week%201%20-%20Big%20O%20%7C%20Recursion%20with%20Memoization/Substring.py)<br>
[Problem 2: Longest Common Prefix](https://github.com/organizedanvrchy/LeetCode/blob/main/Longest_Common_Prefix.py)<br>
[Problem 3: Add Binary](https://github.com/organizedanvrchy/LeetCode/blob/main/Add_Binary.py)

### Session #2
[Problem 1: Integer Replacement](https://github.com/organizedanvrchy/LeetCode/blob/main/Integer_Replacement.py)<br>
[Problem 2: Roman to Integer](https://github.com/organizedanvrchy/LeetCode/blob/main/Roman_to_Integer.py)<br>
[Problem 3: Integer to Roman](https://github.com/organizedanvrchy/LeetCode/blob/main/Integer_to_Roman.py)

[^1]: [GeeksForGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/#what-is-bigo-notation)
[^2]: [CodeAcademy](https://www.codecademy.com/resources/blog/recursion/)
[^3]: [FreeCodeCamp](https://www.freecodecamp.org/news/memoization-in-javascript-and-react)
