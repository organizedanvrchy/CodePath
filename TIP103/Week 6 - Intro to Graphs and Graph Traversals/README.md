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

[^1]:[GeeksForGeeks](https://www.geeksforgeeks.org/introduction-to-graphs-data-structure-and-algorithm-tutorials/)
