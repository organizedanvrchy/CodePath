# LINKED LISTS
Linked Lists are fundamental data structures for storing collections of elements. Linked Lists allow for more efficient insertion and deletion operations when compared to arrays since they consist of nodes that point to the next node in a sequence and do not use contiguous blocks or memory. 

## Structure
A Linked List is comprised of nodes containing 2 parts:
1. Data: the value or information stored in the node
2. Pointer: a reference to the next node in the sequence

## Common Types
### Singly Linked Lists
In a Singly Linked List, each node only points to the next node and the last node points to null.

```python3
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   # value or information stored in node
        self.next = None   # pointer to next node 
```

### Doubly Linked Lists
In this type of list, each node contains a pointer to both the next node and the previous node. This type of list allows for more efficient traversal in both direction of the list when compared to the singly linked list. This also allows for quick insertion and deletion of nodes. 

```python3
class Node:
    def __init__(self, data):
        self.data = data   # value or information stored in node 
        self.next = None   # pointer to next node
        self.prev = None   # pointer to previous node
```

### Circular Linked List
In this linked list, the last node points back to the first node, forming a loop or circle. These lists are helpful for tasks that include scheduling and managing playlists. Circular Linked Lists can either be:

1. Circular Singly Linked Lists<br>
  - where each node has just one pointer to the next node and the last node points back to the first node instead of null.
<picture>
   <img alt="Circular Singly Linked Lists" src="https://media.geeksforgeeks.org/wp-content/uploads/20240806130914/Representation-of-circular-linked-list.webp">
</picture>

2. Circular Doubly Linked Lists<br>
  - where each node has two pointers to the previous and next nodes, but here, there first node's previous pointer points to the last node and the last node's next pointer points to the first node. 
<picture>
   <img alt="Circular Doubly Linked Lists" src="https://media.geeksforgeeks.org/wp-content/uploads/20240806145223/Representation-of-circular-doubly-linked-list.webp">
</picture>

```
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initilize and allocate memory for nodes
first = Node(2)
second = Node(3)
last = Node(4)

# Connect nodes
first.next = second
second.next = last
last.next = first
```
