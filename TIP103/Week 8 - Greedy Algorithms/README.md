# Greedy Algorithms
Greedy algorithms are algorithms that employ a series of choices by selecting locally optimal option at each step, in hopes of leading to a globally optimal solution. These algorithms are often used in optimizations problems that required immediate, short-term decisions.

## Key Characteristics
### Greedy Choice Pattern
The algorithm makes a choice that seems best at that moment of each step without worrying about future consquences. This implies that selecting the local optimal solutions can result in a global optimal solution. 

### Optimal Substructure
Problems solved using this algorithm have optimal substructures if an optimal solution to the problems contain optimal solutions to its sub-problems. 

## Design
Greedy algorithms require defining the problem and possible choices, choosing the greedy strategy, proving that the greedy choice leads to an optimal solution, and then implementing the algorithm.

## Advantages and Disadvantages
### Advantages
These algorithms are simple to implement and can be efficient with better time complexities than other algorithms. 

### Disadvantages
These algorithms may not always provide the optimal solution to every problem, and local greedy solutions may lead to suboptimal global results in some cases. 

## Common Applications
### Dijkstra's Algorithm
Finding the shortest path in a graph from a starting vertex to all other vertices.

### Prim's and Kruskal's Algorithms
Finding the minimum spanning tree (MST) of a weight, connected graph

### Fractional Knapsack Problem
This involves maximizing the total values of items placed in a weight limited knapsack, allowing for fractional parts of items. 

### Activity Selection[^1]
This involves selecting the maximum number of non-overlapping activities from a list, where each activity has a start and end time. 

### Huffman Coding[^2]
This is the construction of an optimal binary prefix code to compress data, where more frequent characters have shorter codes. 

[^1]: [GeeksForGeeks - Activity Selection](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)
[^2]: [GeeksForGeeks - Huffman Coding](https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/)
