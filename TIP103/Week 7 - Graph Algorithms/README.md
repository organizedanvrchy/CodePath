# Topological Sort
This is a common graphing concept that produces a linear ordering of vertices (nodes) in a DAG, where every for directed edge(_u -> v_), vertex _u_ comes before vertex _v_. This process entails: 
1. Identifying vertices with no incoming edges (indegree).
2. Removing the vertex and its outgoing edges.
3. Repeating the above.

### Kahn's Algorithm
This algorithm uses an "indegree" array and a queue to keep track of vertices with no incoming edges. This algorithm can detect cycles in graphs and can also be used for applications where tasks must be done in sequence. This algorithm works by:<br>
1. Calculating the "indegrees" (simply, number of incoming edges to a node) for each vertex;
2. Initializing a queue;
3. Enqueuing all vertices with 0 "indegrees";
4. Checking while the queue is not empty;
5. Dequeuing a vertex and adding it to the topological order;
6. Reducing the "indegree" for each adjacent vertex of u by 1;
7. Enqueuing the vertex if the "indegree" becomes 0;
8. Checking for cycles (by checking if the queue is emptied and topological order does not contain all vertices)

```python3
from collections import defaultdict, deque

# Function to perform Kahn's Algorithm for topological sorting
def kahns_algorithm(vertices, edges):
    # Step 1: Calculate in-degrees of all vertices
    in_degree = {i: 0 for i in range(vertices)}  # Initialize in-degree of all vertices to 0
    adj_list = defaultdict(list)  # Adjacency list to store the graph

    # Build the graph and update in-degrees
    for u, v in edges:
        adj_list[u].append(v)  # Add edge u -> v
        in_degree[v] += 1      # Increase in-degree of vertex v

    # Step 2: Initialize a queue and enqueue all vertices with in-degree 0
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    
    topological_order = []  # List to store the topological order

    # Step 3: Process the queue
    while queue:
        node = queue.popleft()  # Dequeue a vertex
        topological_order.append(node)  # Add it to the topological order

        # Decrease the in-degree of all adjacent vertices
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)  # Enqueue if in-degree becomes zero

    # Step 4: Check if topological sorting is possible (no cycles)
    if len(topological_order) == vertices:
        return topological_order  # Return the topological order
    else:
        return "Graph contains a cycle, topological sorting not possible"

# Example Usage
vertices = 6
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

topological_order = kahns_algorithm(vertices, edges)
print("Topological Order:", topological_order)
```

```python3
Topological Order: [4, 5, 2, 3, 1, 0]
```
### DFS
This technique uses recursion to visit nodes, mark them as visited, fully explore neighbors, and then add them to the output stack. 

```python3
from collections import defaultdict

# Function to perform DFS and store the topological order
def dfs(node, visited, stack, adj_list):
    visited[node] = True  # Mark the current node as visited

    # Recur for all vertices adjacent to this vertex
    for neighbor in adj_list[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, stack, adj_list)

    # Push current vertex to stack after all its neighbors are processed
    stack.append(node)

# Function to perform topological sort using DFS
def topological_sort_dfs(vertices, edges):
    adj_list = defaultdict(list)  # Adjacency list representation of the graph

    # Build the graph
    for u, v in edges:
        adj_list[u].append(v)

    visited = [False] * vertices  # Keep track of visited vertices
    stack = []  # Stack to store the topological order

    # Perform DFS for each vertex
    for i in range(vertices):
        if not visited[i]:
            dfs(i, visited, stack, adj_list)

    # Return the elements in the stack in reverse order (since stack gives us reverse topological order)
    return stack[::-1]

# Example Usage
vertices = 6
edges = [
    (5, 2),
    (5, 0),
    (4, 0),
    (4, 1),
    (2, 3),
    (3, 1)
]

topological_order = topological_sort_dfs(vertices, edges)
print("Topological Order:", topological_order)
```
```python3
Topological Order: [5, 4, 2, 3, 1, 0]
```
<table>
    <tr>
        <td></td>
        <td>Complexity</td>
    </tr>
    <tr>
        <td>Time</td>
        <td>O(V + E)</td>
    </tr>
    <tr>
        <td>Space</td>
        <td>O(V + E)</td>
    </tr>
</table>

---

# Disjoint Set Union (Union Find)
This is a data structure that efficiently handles the union and find operations on a collection of disjoint (non-overlapping) sets. This structure is useful for inspecting connectivity in graph algorithms. These operations include initializing a parent and rank arrays, implementing a union operation, and implementing a find operation. 

```python3
# Union by Rank and Path Compression
parent = [i for i in range(len(nodes))]
rank = [0] * len(nodes)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    xroot, yroot = find(x), find(y)
    if xroot != yroot:
        if rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
    else:
        parent[xroot] = parent[yroot]
         if rank[xroot] == rank[yroot]:
             rank[yroot] += 1
```

```python3
# Alternative Class Creation
class UnionFind:
    def __init__(self, n):
        # Initialize each node to be its own parent (self loop) and rank of 0
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Path compression: point x directly to its root to flatten the structure
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Find roots of the elements
        rootX = self.find(x)
        rootY = self.find(y)

        # Elements are already in the same set
        if rootX == rootY:
            return False
        
        # Union by rank: attach the smaller tree under the larger tree
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True
```

---

# Minimum Spanning Trees (MST)
A **Minimum Spanning Tree (MST)** of a connected, undirected graph is a subset of the edges that connects all the vertices in the graph, without any cycles, and with the minimum possible total edge weight. 

## Kruskal's Algorithm
**Kruskal's Algorithm** is a greedy algorithm that finds the minimum spanning tree by sorting all the edges in non-decreasing order of their weights and adding them one by one to the MST, ensuring that no cycles are formed. It uses a **Union-Find (Disjoint Set Union, DSU)** data structure to check and manage the connected components.

### Steps of Kruskal's Algorithm:
1. **Sort** all edges in the graph in increasing order of their weights.
2. Initialize an empty MST.
3. For each edge in the sorted list:
   - If the edge connects two different components (checked using Union-Find), add the edge to the MST.
   - Otherwise, discard the edge.
4. Repeat until the MST contains `V-1` edges (where `V` is the number of vertices).

```python3
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

def kruskal(n, edges):
    mst = []
    disjoint_set = DisjointSet(n)
    
    # Sort the edges by weight
    edges.sort(key=lambda x: x[2])
    
    for u, v, weight in edges:
        if disjoint_set.find(u) != disjoint_set.find(v):
            mst.append((u, v, weight))
            disjoint_set.union(u, v)
    
    return mst

# Example Usage
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4  # Number of vertices
mst = kruskal(n, edges)
print("Edges in MST:", mst)
```

## Prim's Algorithm
**Prim's Algorithm** is another greedy algorithm that finds an MST by growing the tree from an arbitrary starting vertex. It starts with a single vertex and repeatedly adds the smallest edge that connects a vertex in the tree to a vertex outside the tree.

### Steps of Prim's Algorithm:
1. Initialize the MST with an arbitrary starting vertex.
2. Use a priority queue (min-heap) to keep track of the edges connecting the MST to the rest of the graph.
3. At each step, add the edge with the smallest weight that connects a vertex in the MST to a vertex outside it.
4. Repeat until the MST contains all the vertices.

```python3
import heapq

def prim(n, edges):
    adj_list = {i: [] for i in range(n)}
    for u, v, weight in edges:
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
    
    # Initialize variables
    mst = []
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex) starting from vertex 0
    
    while min_heap:
        weight, u = heapq.heappop(min_heap)
        
        if visited[u]:
            continue
        
        visited[u] = True
        if weight > 0:  # Skip the first 0-weight edge (starting point)
            mst.append((prev, u, weight))
        
        for v, edge_weight in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v))
                prev = u
    
    return mst

# Example Usage
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
n = 4  # Number of vertices
mst = prim(n, edges)
print("Edges in MST:", mst)
```

## Comparison of Kruskal's and Prim's Algorithms

| **Property**              | **Kruskal's Algorithm**                                | **Prim's Algorithm**                                  |
|---------------------------|--------------------------------------------------------|-------------------------------------------------------|
| **Type of Approach**       | Greedy (edge-based)                                   | Greedy (vertex-based)                                 |
| **Data Structure**         | Union-Find (Disjoint Set Union)                       | Priority Queue (Min-Heap)                             |
| **Time Complexity**        | O(E log E) or O(E log V)                              | O(E log V) (using Min-Heap)                           |
| **Best For**               | Sparse graphs (many edges but few vertices)           | Dense graphs (many vertices and edges)                |
| **Edge Sorting**           | Requires sorting of edges initially                   | No need for sorting, operates on edges in a priority queue |


---

# Shortest Path Algorithms
Shortest path algorithms are used to find the shortest path between nodes in a graph, which may represent, for example, road networks, communication networks, or social networks. This section provides brief descriptions of three well-known algorithms for solving the shortest path problem:

- **Bellman-Ford's Algorithm**
- **Dijkstra's Algorithm**
- **Floyd-Warshall's Algorithm**

## Bellman-Ford's Algorithm
**Bellman-Ford's Algorithm** is an algorithm for finding the shortest paths from a single source vertex to all other vertices in a graph. It works even when the graph has negative weight edges, and it can also detect negative weight cycles. The algorithm works by relaxing all the edges **V-1** times (where `V` is the number of vertices).

### Steps:
1. Initialize the distances to all vertices as infinity, except for the source vertex which is set to 0.
2. Relax all edges `V-1` times.
3. After `V-1` relaxations, check for negative-weight cycles by relaxing the edges once more.

```python3
def bellman_ford(graph, V, start):
    distances = [float("inf")] * V
    distances[start] = 0
    
    # Relax all edges V-1 times
    for _ in range(V - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains negative weight cycle")
            return None
    
    return distances

# Example usage
graph = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 4, -3), (4, 3, 3)]
V = 5  # Number of vertices
start = 0  # Source vertex
distances = bellman_ford(graph, V, start)
print("Shortest distances from source:", distances)
```

## Dikstra's Algorithm
**Dijkstra's Algorithm** is a greedy algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights. It selects the vertex with the smallest tentative distance, updates the distances of its adjacent vertices, and repeats this process until all vertices have been visited.

### Steps:
1. Initialize the distances to all vertices as infinity, except for the source vertex which is set to 0.
2. Use a priority queue (min-heap) to select the vertex with the smallest tentative distance.
3. Update the distances to the neighboring vertices of the selected vertex.
4. Repeat the process until all vertices are processed.

```python3
import heapq

def dijkstra(graph, V, start):
    distances = [float("inf")] * V
    distances[start] = 0
    pq = [(0, start)]  # Priority queue: (distance, vertex)
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        if current_distance > distances[u]:
            continue
        
        for v, weight in graph[u]:
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    return distances

# Example usage
graph = {0: [(1, -1), (2, 4)], 1: [(2, 3), (3, 2), (4, 2)], 2: [(3, 5)], 3: [(2, 5), (4, -3)], 4: [(3, 3)]}
V = 5  # Number of vertices
start = 0  # Source vertex
distances = dijkstra(graph, V, start)
print("Shortest distances from source:", distances)
```

## Floyd-Warshall's Algorithm
**Floyd-Warshall's Algorithm** is an algorithm for finding shortest paths between all pairs of vertices in a graph. It can handle negative weight edges, but does not work for graphs with negative weight cycles. It uses dynamic programming to compute the shortest path between each pair of vertices.

### Steps:
1. Initialize the distance matrix with edge weights.
2. For each vertex, update the matrix to reflect the shortest path between all pairs of vertices by considering each vertex as an intermediate point.
3. Repeat the process for all vertices

```python3
def floyd_warshall(graph, V):
    # Initialize distance matrix
    dist = [[float("inf")] * V for _ in range(V)]
    
    for u in range(V):
        dist[u][u] = 0
    
    for u, v, weight in graph:
        dist[u][v] = weight
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example usage
graph = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 4, -3), (4, 3, 3)]
V = 5  # Number of vertices
distances = floyd_warshall(graph, V)
print("Shortest distance matrix:")
for row in distances:
    print(row)
```

## Summary of Algorithms

| **Algorithm**      | **Time Complexity**         | **Graph Type**                              | **Handles Negative Weights**  | **Handles Negative Cycles**  |
|--------------------|-----------------------------|---------------------------------------------|-------------------------------|------------------------------|
| **Bellman-Ford**    | O(V * E)                    | Works for both dense and sparse graphs      | Yes                           | Yes                          |
| **Dijkstra**        | O((V + E) log V)            | Works only for graphs with non-negative weights | No                            | No                           |
| **Floyd-Warshall**  | O(V^3)                      | All-pairs shortest path problem             | Yes                           | No                           |

---

## Practice Questions
### Warmups
[Problem 1: Find All Possible Recipes from Given Supplies](https://github.com/organizedanvrchy/LeetCode/blob/main/Find_All_Possible_Recipes_from_Given_Supplies.py)<br>

### Session #1
[Problem 1: 01 Matrix](https://github.com/organizedanvrchy/LeetCode/blob/main/01_Matrix.py)<br>
[Problem 2: Flood Fill](https://github.com/organizedanvrchy/LeetCode/blob/main/Flood_Fill.py)<br>
[Problem 3: Word Search](https://github.com/organizedanvrchy/LeetCode/blob/main/Word_Search.py)<br>
[Problem 4: Rotting Oranges](https://github.com/organizedanvrchy/LeetCode/blob/main/Rotting_Oranges.py)<br>

### Session #2
[Problem 1: Number of Provinces](https://github.com/organizedanvrchy/LeetCode/blob/main/Number_of_Provinces.py)<br>
[Problem 2: Clone Graph](https://github.com/organizedanvrchy/LeetCode/blob/main/Clone_Graph.py)<br>
[Problem 3: Keys and Rooms](https://github.com/organizedanvrchy/LeetCode/blob/main/Keys_and_Rooms.py)

