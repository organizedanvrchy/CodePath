# Graphs
Graphs are another important fundamental data structure that can often be used to represent the relationship between different data types. There are two primary __components__ of graphs:
1. Vertices (or Nodes)<br>
These are the data points that are stored. These points can either be labeled or unlabeled.
2. Edges<br>
These represent the connections between the data points (or vertices).<br>

Graphs are denoted as _G(V, E)_, where _V_ represents the vertices and _E_ represents the edges.

<picture>
  <img src="https://i.imgur.com/Zq3wULu.png" width="400">
</picture>

## Types of Graphs[^1]
### Weighted Graph
In a weighted graph, each edge has a "weight" (often used to represent distance, cost, or capacity).

### Unweighted Graph
In these graphs, all edges have equal weight or significance.

### Directed Graph
These graphs contain edges with direction, where nodes are ordered pairs. 
This essentially means that the relationship between two nodes is _one-way_.

### Undirected Graph
These are graphs that contain edges with no direction (or the modes are unordered pairs with respect to every edge).
This means that the relationship between two nodes is _mutual_.

<picture>
  <img src="https://i.imgur.com/JWL96oK.png" width="400">
</picture>

### Cyclic Graph
These graphs contain atleast one cycle, which is when a path starts and ends at the same vertex.
> [!TIP]
> A __Cycle Graph__ is a cycle in itself with a minimum of 2 degrees at each vertex.

### Acyclic Graph
This type of graph consists of no cycles. These are referred to as Directed Acyclic Graphs (or DAGs) and are often use in situations where tasks must be completed in a specific order. DAGs have special properties:
1. Sink<br>
These are nodes that have no outgoing edges and only incoming edges.
2. Source<br>
These are nodes that only have outgoing edges and no incoming edges. 

<picture>
  <img src="https://i.imgur.com/2z9J2E5.png" width="400">
</picture>

### Bipartite Graph
These graphs contain vertices that can be divided into two sets, where vertices in each set do not contain any edges between themselves. 

<picture>
  <img src="https://www.baeldung.com/wp-content/uploads/sites/4/2020/06/bipartite.png" width="400">
</picture>

## Graph Representations
### Adjacency Matrix
This is a 2D matric where the row and columns correspond to vertices and the value of the entries correspond to the weight of an edge between those vertices. This is useful for dense graphs that have mostly connected vertex pairs.

<picture>
  <img src="https://i.imgur.com/GzU4BKw.png" width="500">
</picture>

### Adjacency List
This is an efficient way to represent graphs, where each vertex has a list of adjacent vertices (or each node stores a list of adjacent vertices). In undirected graphs, each edge from __node a__ to __node b__ would be stored twice (once in __node a's__ adjacency list and once in __node b's__ adjacency list). This is suitable for sparse graphs that have only a few connected vertices. 

<picture>
  <img src="https://i.imgur.com/JwA2sxn.png" width="500">
</picture>

### Edge List
This is a simple list of all the edges in a graph. 

<picture>
  <img src="https://i.imgur.com/F2XET50.png" width="500">
</picture>

### Runtime Analysis
<table>
  <tr>
    <td>Representation</td>
    <td>All Adjacent Edges of a Vertex</td>
    <td>Traversal</td>
    <td>Edge Check</td>
    <td>Space</td>
  </tr>
  <tr>
    <td>Matrix</td>
    <td>O(V)</td>
    <td>O(V<sup>2</sup>)</td>
    <td>O(1)</td>
    <td>O(V<sup>2</sup>)</td>
  </tr>
  <tr>
    <td>Edge List</td>
    <td>O(E)</td>
    <td>O(E)</td>
    <td>O(E)</td>
    <td>O(E)</td>
  </tr>
  <tr>
    <td>Adjacency List</td>
    <td>O(1)</td>
    <td>O(V + E)</td>
    <td>O(Max # of edges to a vertex)</td>
    <td>O(E + V)</td>
  </tr>
</table>

## Graph Traversals
### Breadth First Search
BFS is used to traverse a graph layer by layer and is often used for _finding the shortest path between two nodes in an unweighted graph_ or _exploring all the vertices connected to a particular vertex_. This usually takes O(V + E) time. 

<picture>
  <img src="https://i.imgur.com/S0369iR.png" width="500">
</picture><br>

__Example Implementation__:
```python3
from collections import deque

def bfs(graph, start):
    # Initialize a set to track visited nodes
    visited = set()
    
    # Initialize a queue and add the start node to it
    queue = deque([start])
    
    # Traverse the graph
    while queue:
        # Dequeue a node from the front
        node = queue.popleft()
        visited.add(node)

        # If a node has neighbors, check them
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return visited

# Define a directed graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],  
    'E': ['F'],
}

# Perform BFS starting from vertex 0
bfs(graph, 0)
```

### Depth-First Search
DFS is used to explore as far down a branch as possible before backtracking. The start can be at an arbitrary node and then explore each neighbor fully before exploring the next node.This is commonly used for detecting cycles, finding components, and topological sorting. The runtime is O(V + E).
> [!TIP]
> __Topological Sorting__ is commonly used in DAGs to order vertices in a way that every directed edge points from an _earlier vertex_ to a _later vertex_. This is used in task scheduling and dependency resolution.

<picture>
  <img src="https://i.imgur.com/S0369iR.png" width="500">
</picture><br>

__Example Implementation__:
```python3
def dfs(graph, start):  
    # Initialize an empty set to track visited nodes to avoid revisiting them
    visited = set()

    # Use a stack (LIFO) to keep track of the vertices to explore next, starting with the start vertex
    stack = [start]  
    
    # Loop until there are no more vertices to explore
    while stack:
        # Pop the last vertex from the stack (depth-first manner: LIFO)
        vertex = stack.pop()
        
        # If this vertex hasn't been visited yet, we will process it
        if vertex not in visited:
            visited.add(vertex)  # Mark this vertex as visited
            
            # Check if the vertex is in the adjacency list (in case it has no outgoing edges)
            if vertex in graph:
                # Explore all unvisited neighbors of this vertex
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        # Add the neighbor to the stack for future exploration
                        stack.append(neighbor)
    
    # Return the set of visited vertices after the DFS completes
    return visited

# Define a directed graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],  
    'E': ['F'],
}

res = dfs(graph, 0)
print(res)
```

## Common Graph Algorithms
### Dijkstra's Algorithm
This algorithm finds the shortest path from a source vertex to all other vertices in a weighted graph. The time complexity is O((V+E)logV) with priority queues.
> [!NOTE]
> Walkthrough[^2]

### Floyd-Warshall Algorithm
This algorithm solves the all-pairs shortest path problem for weighted graphs with a time complexity of O(V<sup>3</sup>).

### Kruskal's and Prim's Algorithms[^3]
These algorithms are used for Minimum Spanning Trees to find a subset of edges that form a tree connecting all vertices with the minimum total edge weight. Kruskal's algorithm takes O(ElogE) time while Prim's algorithm takes O(V<sup>2</sup>) or O((V + E)logV) with priority queues.

## Practice Questions
### Session #2
[Problem 1: Number of Provinces](https://github.com/organizedanvrchy/LeetCode/blob/main/Number_of_Provinces.py)<br>
[Problem 2: Clone Graph](https://github.com/organizedanvrchy/CodePath/blob/main/TIP103/Week%206%20-%20Intro%20to%20Graphs%20and%20Graph%20Traversals/Clone_Graph.py)<br>
[Problem 3: Keys and Rooms](https://github.com/organizedanvrchy/LeetCode/blob/main/Integer_to_Roman.py)

[^1]:[GeeksForGeeks](https://www.geeksforgeeks.org/introduction-to-graphs-data-structure-and-algorithm-tutorials/)
[^2]:[Dijkstra's Algorithm Walkthrough](https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/)
[^3]:[Kruskal's and Prim's Algorithms](https://www.geeksforgeeks.org/difference-between-prims-and-kruskals-algorithm-for-mst/)
