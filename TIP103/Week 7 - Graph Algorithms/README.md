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

# Shortest Path
## Bellman Ford's Algorithm
## Dikstra's Algorithm
## Floyd-Warshall's Algorithm
