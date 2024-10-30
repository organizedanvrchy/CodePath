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

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)
    
    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        
        for i in range(self.V):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        
        return stack[::-1]  # return reversed stack for topological order
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

# Disjoint Set Union (Union Find)

# Minimum Spanning Trees
## Kruskal's Algorithm
## Prim's Algorithm

# Shortest Path
## Bellman Ford's Algorithm
## Dikstra's Algorithm
## Floyd-Warshall's Algorithm
