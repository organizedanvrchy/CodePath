# Big O Complexity Analysis
This notation is most often used when describing the time and space complexities of algorithms. In this case, __time__ refers to _how long it takes the algorithm to complete_ and __space__ refers to _how much memory the algorithm uses during execution_. Hence, Big-O notation is a standardized way of measuring the _efficiency_ of an algorithm, whereby; it represents the __worst case__ or __upper bound__ time complexity. Big-O notation is denoted as: __O(f(n))__ where __f(n)__ often represents the __number of steps__ that an algorithm takes to solve a problem of size n[^1]. 

## Important Properties
1. Non-negativity
   - The growth rate described by Big-O notation is always non-negative.
2. Transitivity
   - If f(n) is in O(g(n)) and g(n) is in O(h(n)), then __f(n) is also in O(h(n))__.
3. Constants are Ignored
   - e.g. O(2n) is expressed as O(n).
4. Sum Rule
   - If f(n) is in O(g(n)) and h(n) is in O(g(n)), then __f(n) + h(n) = O(g(n))__.
5. Product Rule
   - If f(n) is in O(g(n)) and h(n) is in O(k(n)), then __f(n) * h(n) = O(g(n) * (k(n))__.
6. Composition Rule
   - If f(n) is in O(g(n)) and g(n) is in O(h(n)), then __f(g(n)) = O(h(n))__.
  
## Common Big-O Notations
1. Constant Time Complexity: O(1)
   - This notation refers to algorithms that take the same amount of time to complete, while ignoring the input size. Essentially, they only take "one" step. 
2. Linear Time Complexity: O(n)
   - This notation indicates that the running time of an algorithm grows linearly with the input size. The algorithm performs the same set of steps for each input element.
3. Quadratic Time Complexity: O(n<sup>2</sup>) 









[^1]: [GeeksForGeeks](https://www.geeksforgeeks.org/analysis-algorithms-big-o-analysis/#what-is-bigo-notation)
