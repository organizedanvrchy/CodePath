# Topological Sort
This is a common graphing concept that produces a linear ordering of vertices (nodes) in a DAG, where every for directed edge(_u -> v_), vertex _u_ comes before vertex _v_. This process entails: 
1. Identifying vertices with no incoming edges (indegree).
2. Removing the vertex and its outgoing edges.
3. Repeating the above.

### Kahn's Algorithm
This algorithm uses an "indegree" array and a queue to keep track of vertices with no incoming edges.

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
        <td>Complexity</td>
        <td>Big-O</td>
    </tr>
    <tr>
        <td>Time</td>
        <td>O(E + V)</td>
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
