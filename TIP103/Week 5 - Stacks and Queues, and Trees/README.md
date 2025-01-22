# Stacks, Queues, and Trees

## Stack
### Definition
A linear data structure that follows the **LIFO (Last In, First Out)** principle.

### Operations
  - **Push**: Add an element to the top of the stack.
  - **Pop**: Remove the top element from the stack.
  - **Peek/Top**: Retrieve the top element without removing it.

### Applications
  - Function call management (e.g., recursion).
  - Undo mechanisms in text editors.
  - Expression evaluation (postfix/prefix).
  - Syntax parsing.

### Example
```python3
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self.stack.append(item)

    def pop(self):
        """Remove and return the top item of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        """Return the top item without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self.stack)

    def display(self):
        """Display the stack."""
        print("Stack:", self.stack)

# Example usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  # Output: Stack: [10, 20, 30]

    print("Top element:", stack.peek())  # Output: Top element: 30
    print("Popped element:", stack.pop())  # Output: Popped element: 30
    stack.display()  # Output: Stack: [10, 20]

    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False
    stack.pop()
    stack.pop()
    print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? True
```

---

## Queue
### Definition
A linear data structure that follows the **FIFO (First In, First Out)** principle.

### Variants
  - **Simple Queue**: Elements are enqueued at the rear and dequeued from the front.
  - **Circular Queue**: The last position connects back to the first to utilize unused space.
  - **Priority Queue**: Elements are dequeued based on priority rather than order.
  - **Deque**: Double-ended queue allowing insertion/removal from both ends.

### Applications
  - Job scheduling (CPU scheduling).
  - Breadth-first search (BFS) in graphs and trees.
  - Data buffering (e.g., IO Buffers).
  - 
### Example
```python3
# Queue Implementation in Python using a List

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty!"

    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def display(self):
        """Display the queue."""
        print("Queue:", self.queue)

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  # Output: Queue: [10, 20, 30]

    print("Front element:", queue.peek())  # Output: Front element: 10
    print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 10
    queue.display()  # Output: Queue: [20, 30]

    print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
    queue.dequeue()
    queue.dequeue()
    print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? True
```

**Alternatively, a 'deque' can be used as follows**:
```python3
from collections import deque

# Queue Implementation using deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        self.queue.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return "Queue is empty!"

    def peek(self):
        """Return the front item without removing it."""
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty!"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.queue)

    def display(self):
        """Display the queue."""
        print("Queue:", list(self.queue))

# Example usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  # Output: Queue: [10, 20, 30]

    print("Front element:", queue.peek())  # Output: Front element: 10
    print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 10
    queue.display()  # Output: Queue: [20, 30]

    print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? False
    queue.dequeue()
    queue.dequeue()
    print("Is queue empty?", queue.is_empty())  # Output: Is queue empty? True
```

---

## Trees
### Definition
A hierarchical data structure consisting of nodes connected by edges. It has one root node and zero or more child nodes. Nodes with no children are called leaves.

### Common Types of Trees
1. **Binary Tree**: Each node has at most two children.
2. **Binary Search Tree (BST)**: A binary tree where the left child is smaller than the parent, and the right child is larger.
3. **AVL Tree**: A self-balancing BST.
4. **Heap**:
   - **Max-Heap**: Parent nodes are greater than their children.
   - **Min-Heap**: Parent nodes are smaller than their children.
5. **Trie**: A tree for storing strings, used in prefix matching.
6. **N-ary Tree**: Each node can have at most N children.

### Key Properties
- **Depth**: Distance from the root to a node.
- **Height**: The longest path from the root to a leaf.
- **Full Binary Tree**: Every node has 0 or 2 children.
- **Complete Binary Tree**: All levels except possibly the last are completely filled, and nodes are as left as possible.

### Applications
- Hierarchical data representation (e.g., file systems).
- Expression parsing (expression trees).
- Searching and sorting (BST, AVL, etc.).
- Networking (routing tables).
- Artificial intelligence (decision trees).

### Example
```python3
# Binary Tree Node Class
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Binary Tree Class
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a new node with the given key into the binary tree."""
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        """Helper function to recursively insert a node."""
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        elif key > node.value:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        """Search for a node with the given key."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Helper function to recursively search for a node."""
        if node is None or node.value == key:
            return node
        if key < node.value:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self):
        """In-order traversal of the binary tree."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Helper function for in-order traversal."""
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):
        """Pre-order traversal of the binary tree."""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        """Helper function for pre-order traversal."""
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Post-order traversal of the binary tree."""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        """Helper function for post-order traversal."""
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

# Example usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    print("In-order traversal:", tree.inorder())  # Output: [20, 30, 40, 50, 60, 70, 80]
    print("Pre-order traversal:", tree.preorder())  # Output: [50, 30, 20, 40, 70, 60, 80]
    print("Post-order traversal:", tree.postorder())  # Output: [20, 40, 30, 60, 80, 70, 50]

    # Searching for a value
    search_result = tree.search(40)
    if search_result:
        print("Found node with value:", search_result.value)  # Output: Found node with value: 40
    else:
        print("Node not found")
```

---

## Comparison Table

| Feature            | Stack            | Queue            | Tree                     |
|--------------------|------------------|------------------|--------------------------|
| **Structure**      | Linear           | Linear           | Hierarchical             |
| **Order**          | LIFO             | FIFO             | No strict order          |
| **Operations**     | Push/Pop         | Enqueue/Dequeue  | Insert/Delete/Traverse   |
| **Applications**   | Call stack, undo | BFS, scheduling  | Searching, sorting, AI   |

---
