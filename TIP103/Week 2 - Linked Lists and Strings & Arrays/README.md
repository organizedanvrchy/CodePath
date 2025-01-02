<table>
    <tr>
        <td>Jump to --></td>
        <td><a href="https://github.com/organizedanvrchy/CodePath/blob/main/TIP103/Week%202%20-%20Linked%20Lists%20and%20Strings%20%26%20Arrays/README.md#strings" target="_blank">Strings</td>
        <td><a href="https://github.com/organizedanvrchy/CodePath/blob/main/TIP103/Week%202%20-%20Linked%20Lists%20and%20Strings%20%26%20Arrays/README.md#arrays" target="_blank">Arrays</td>
        <td><a href="https://github.com/organizedanvrchy/CodePath/blob/main/TIP103/Week%202%20-%20Linked%20Lists%20and%20Strings%20%26%20Arrays/README.md#linked-lists" target="_blank">Linked Lists</td>
    </tr>
</table>

# Strings
Strings are a sequence of characters stored in contiguous memory locations and can include letters, numbers, symbols, and whitespaces. Characters in a string can be represented by specific encoding, such as ASCII (Maps 128 characters to numbers 0 to 127) or Unicode. In some programming languages, strings are immutable (cannot be changed after creation), where operations on the string often lead to the creation of a new string instead of modifying the original. While in other programming languages, strings are mutable (such as in C++), where they can be modified in-place. Strings are often represented using either single quotes or double quotes; however, some languages will mostly likely use single quotes to denote characters and double quotes to denote strings. 
> [!NOTE]
> When using a language that supports ASCII (such as Python), the ord() function can be used to get the integer value that the character is mapped to and chr() can be used to get the character that the integer value is mapped to. 

## Common Escape Sequences
Escape sequences are special character sequences that are non-printable. They usually start with a "\\". Some frequent examples include:
1. __\\n__ - Newline
2. __\\t__ - Tab
3. __\\\\__ - Backslash
4. __\\"__ - Double Quote

## Common Operations
### Concatenation
This is the joining of two or more strings together.

```python3
"Hello, " + "world!"
```
### Substring Extraction
This operation allows for the extraction of a part of a string. In Python, this can be done using slicing, with syntax __string[start:end]__, where the start and end indices are inclusive.

```python3
string = "Hello"
substring = string[1:4]  # Extracts characters from index 1 to 3 (end index is exclusive)
print(substring)  # Output: "ell"
```

### Searching
This operation finds the position of a character or substring in a string. In Python, this can be done using the find() function, where the index of the first occurrence of the character or substring is returned (or -1 if not found). 

```python3
string = "Hello"
position = string.find("l")  # Finds the first occurrence of "l"
print(position)  # Output: 2
```

### Length
The length of the string is a very useful piece of information that can be used in other operations. This operation specifically sums up the number of characters in a given string. In Python, this can be done using the len() function. 

```python3
string = "Hello"
length = len(string)
print(length)  # Output: 5
```

### Iteration
This operation loops through the characters in a string and also enables other string operations. In Python, this can be done using a _for_ loop.

```python3
string = "Hello"
for char in string:
    print(char, end=" ")  # Output: H e l l o 
```

# Arrays
Arrays are fundamental and linear data structures that are used to store a collection of same data type elements in contiguous memory locations. Each element in an array is indexed (starting from 0) which allows for quick access and modification in most cases. Arrays are generally of fixed sized, but some languages support dynamically sized arrays using underlying fixed sized arrays (generally involving doubling the array size before it is full). In Python, arrays are implemented as lists, allowing for dynamic sizing, whereas in other languages (such as C and Java) arrays are declared with a specific type and size. 

```python3
# Python
arr = [1, 2, 3, 4, 5]
```

```java
// Java
int[] arr = new int[5];  // Array of integers with size 5
arr[0] = 10;  // Initializing the first element
```

## Indexing
Elements in arrays can be accessed and modified using their index. Generally, the first element is at index 0, while the second element is at index 1, and so forth. 

```python3
arr = [10, 20, 30, 40]
print(arr[0])  # Access the first element (Output: 10)

arr[1] = 25    # Modify the second element
print(arr[1])  # Output: 25
```

## Common Operations
### Traverse
Traversing through an array involves looping through its elements and processing each one at a time.

```python3
arr = [10, 20, 30, 40]
for elem in arr:
    print(elem)
```

### Search
Finding an element in an array can be done using either the value or the index of the element. In Python, array.index(x) is used to find the index of the first occurrence of the x (where x is an integer). 

### Insert
Adding elements to array are generally only done by overwriting an existing element or creating a new array. In Python, since arrays are lists, arr.append() and arr.insert() functions can be used to efficiently insert elements to an array. However, in other languages, the insertion of an element is rather costly. 

### Delete
Deleting an element from a static array is also very costly in many languages. However, in Python, dynamic arrays allow for efficient deletion using the arr.remove() function.

### Sort
This is the rearranging of elements in an array in either ascending or descending order. In Python, arrays can be sorted using arr.sort() or sorted(arr) functions and returns a newly sorted list. 

## Multidimensional Arrays
Arrays can also be __multidimensional__ allowing for the storing of data in more than 1D (such as the creation of matrices). This can be done in Python as follows:

```python3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Accesses the element in the second row, third column (Output: 6)
```

# Linked Lists
Linked Lists are fundamental data structures for storing collections of elements. Linked Lists allow for more efficient insertion and deletion operations when compared to arrays since they consist of nodes that point to the next node in a sequence and do not use contiguous blocks or memory. Linked Lists also have dynamic size, allowing for growing and shrinking as necessary. However, these lists have the disadvantage of __no backward traversals__ and __no direct access__. These lists also require additional memory for the pointers and only offer sequential access to nodes (which might be slower than random access in arrays).[^1]

## Structure
A Linked List is comprised of nodes containing 2 parts:
1. Data: the value or information stored in the node
2. Pointer: a reference to the next node in the sequence

## Common Types
### Singly Linked Lists
In a Singly Linked List, each node only points to the next node and the last node points to null.

<picture>
   <img alt="Singly Linked Lists" src="https://www.w3schools.com/dsa/img_linkedlists_singly.svg">
</picture>

> [!NOTE]
> Images sourced from this link (in footnotes)[^2]

```python3
class Node:
    def __init__(self, data):
       # Data part of the node
        self.data = data   # value or information stored in node
        self.next = None   # pointer to next node 
```

### Doubly Linked Lists
In this type of list, each node contains a pointer to both the next node and the previous node. This type of list allows for more efficient traversal in both direction of the list when compared to the singly linked list. This also allows for quick insertion and deletion of nodes. 

<picture>
   <img alt="Doubly Linked Lists" src="https://www.w3schools.com/dsa/img_linkedlists_doubly.svg">
</picture>

> [!NOTE]
> Images sourced from this link (in footnotes)[^2]

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
  - where each node has just one pointer to the next node and the last node points back to the first node instead of null. These lists have similar drawbacks to those in normal Singly Linked Lists.
  - 
<picture>
   <img alt="Circular Singly Linked Lists" src="https://www.w3schools.com/dsa/img_linkedlists_circsingly.svg">
</picture>

> [!NOTE]
> Images sourced from this link (in footnotes)[^2]

2. Circular Doubly Linked Lists<br>
  - where each node has two pointers to the previous and next nodes, but here, there first node's previous pointer points to the last node and the last node's next pointer points to the first node. These lists offer efficient navigation and have no special cases for end of list; however, the require pointer updating and create more memory overhead.

<picture>
   <img alt="Circular Doubly Linked Lists" src="https://www.w3schools.com/dsa/img_linkedlists_circdoubly.svg">
</picture>

> [!NOTE]
> Images sourced from this link (in footnotes)[^2]

```python3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Initialize and allocate memory for nodes
first = Node(2)
second = Node(3)
last = Node(4)

# Connect nodes
first.next = second
second.next = last
last.next = first
```

## Common Operations
### Traverse
This is simply the visiting of each node in the linked link and is generally the precursor to some other operation such as print or process the data in a node. This can be done as shown below (using Python):

```python3
def traverseLL(head):
    curr = head # Initialize a current node to point to the head of the list

    # Walk curr down the list until it reaches the end (last node points to None)
    while curr is not None:
        print(curr.data) # Or some other operation
        curr = curr.next # Move to the next node
```

### Search
This operation finds a node with a specific value within the Linked List. This method involves traversing the list and checking if the current node's data matches the target value and returns True if a match is found. This can be implemented as:

```python3
def searchLL(head, target):
    # Traverse Linked List
    while head is not None:
        # Check if current node's data matches target value
        if head.data == target:
            return True        # Matching value found
        head = head.next       # Move to next node
    return False               # No matching value found
```
### Length
This is a common operation to find the total number of nodes in a list. This can be done as follows:

```python3
def findLength(head):
    length = 0    # Initialize a counter to store length
    curr = head   # Start from head of list

    # Traverse the Linked List
    while curr is not None:
        length += 1        # Increment the counter for each node visited
        curr = curr.next   # Move to next node

    # Return the final length of the list
    return length
```

### Insert
This operation adds a new node to the list. Node insertion can either be at the beginning of a list, end of a list, or a specific position in the list. 

In __Singly Linked Lists__, insertion involves creating a new node while ensuring that the list remaing properly linked. In these lists, there is only a _next_ pointer to consider.

```python3
# Structure of a Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insertion at the Beginning
def insertAtBeginning(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node  # The new node becomes the head

# Insertion at the End
def insertAtEnd(head, data):
    new_node = Node(data)
    if head is None:
        return new_node  # The list was empty, so new node becomes the head
    temp = head
    while temp.next:  # Traverse to the last node
        temp = temp.next
    temp.next = new_node  # Link the last node to the new node
    return head

# Insertion at a Specific Position
def insertAtPosition(head, data, position):
    new_node = Node(data)
    
    # Insertion at the beginning
    if position == 0:
        new_node.next = head
        return new_node
    
    # Traverse to the node just before the desired position
    temp = head
    for _ in range(position - 1):
        if temp is None:
            raise Exception("Position out of bounds")
        temp = temp.next
    
    # Insert the new node
    new_node.next = temp.next
    temp.next = new_node
    
    return head
```

<table>
    <tr>
        <td>Insertion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

In a __Doubly Linked List__, inserting a new node involves adjusting the _next_ and _prev_ pointers to adjacent nodes. 

```python3
# Structure of a Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Insertion at the Beginning
def insertAtBeginning(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        new_node.next = head
        head.prev = new_node
        head = new_node
    return head

# Insertion at the End
def insertAtEnd(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    return head

# Insertion at a Specific Position
def insertAtPosition(head, data, position):
    new_node = Node(data)
    if position == 0:
        return insertAtBeginning(head, data)
    
    temp = head
    for _ in range(position - 1):
        if temp is None:
            raise Exception("Position out of bounds")
        temp = temp.next
    
    if temp.next is None:  # Insertion at the end
        temp.next = new_node
        new_node.prev = temp
    else:
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp
    
    return head
```

<table>
    <tr>
        <td>Insertion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

In a __Circular Linked List__, the last node points back to the head. These lists can be either singly or doubly linked, but are most notable for having no nodes with a __None__ reference.

```python3
# Structure of a Circular Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insertion at the Beginning
def insertAtBeginning(head, data):
    new_node = Node(data)
    
    if head is None:
        new_node.next = new_node  # The list was empty, so the new node points to itself
        return new_node
    
    # Find the last node
    temp = head
    while temp.next != head:
        temp = temp.next
    
    # Insert the new node
    new_node.next = head
    temp.next = new_node
    return new_node  # The new node becomes the new head

# Insertion at the End
def insertAtEnd(head, data):
    new_node = Node(data)
    
    if head is None:
        new_node.next = new_node  # The list was empty, so the new node points to itself
        return new_node
    
    # Traverse to the last node
    temp = head
    while temp.next != head:
        temp = temp.next
    
    # Insert the new node
    temp.next = new_node
    new_node.next = head
    return head

# Insertion at a Specific Position
def insertAtPosition(head, data, position):
    new_node = Node(data)
    
    if position == 0:
        return insertAtBeginning(head, data)
    
    # Traverse to the node just before the desired position
    temp = head
    for _ in range(position - 1):
        if temp.next == head:  # Position is out of bounds
            raise Exception("Position out of bounds")
        temp = temp.next
    
    # Insert the new node
    new_node.next = temp.next
    temp.next = new_node
    
    return head
```

<table>
    <tr>
        <td>Insertion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

```python3
# Structure of a Circular Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Insertion at the Beginning
def insertAtBeginning(head):
    new_node = Node(data)
    
    if head is None:  # Empty list
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    
    # Find the tail (last node)
    tail = head.prev
    
    # Insert the new node at the beginning
    new_node.next = head
    new_node.prev = tail
    head.prev = new_node
    tail.next = new_node
    
    return new_node  # The new node becomes the new head

# Insertion at the End
def insertAtEnd(head, data):
    new_node = Node(data)
    
    if head is None:  # Empty list
        new_node.next = new_node
        new_node.prev = new_node
        return new_node
    
    # Find the tail (last node)
    tail = head.prev
    
    # Insert the new node at the end
    new_node.next = head
    new_node.prev = tail
    tail.next = new_node
    head.prev = new_node
    
    return head

# Insertion at a Specific Position
def insertAtPosition(head, data, position):
    new_node = Node(data)
    
    # Insertion at the beginning
    if position == 0:
        return insertAtBeginning(head, data)
    
    temp = head
    for _ in range(position - 1):
        if temp.next == head:
            raise Exception("Position out of bounds")
        temp = temp.next
    
    # Insert the new node between temp and temp.next
    new_node.next = temp.next
    new_node.prev = temp
    temp.next.prev = new_node
    temp.next = new_node
    
    return head
```

<table>
    <tr>
        <td>Insertion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

### Delete
This is the operation used to remove a node from a list while maintaining the structure and integrity of the remaining list. Similar to insertion, this maintenance involves pointer manipulation. 

In __Singly Linked Lists__, deletion is similar to insertion where only the _next_ pointer is managed, but instead of adding a node, we are simply removing a node.

```python3
# Structure of a Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Deletion at the Beginning
def deleteAtBeginning(head):
    if head is None:
        return None  # List is already empty
    
    return head.next  # Move the head to the next node

# Deletion at the End
def deleteAtEnd(head):
    if head is None:
        return None  # List is already empty
    
    if head.next is None:  # Only one node in the list
        return None  # The list becomes empty after deletion
    
    temp = head
    while temp.next.next:  # Traverse to the second-to-last node
        temp = temp.next
    
    temp.next = None  # Remove the last node
    return head

# Deletion at a Specific Position
def deleteAtPosition(head, position):
    if head is None:
        return None  # List is already empty
    
    if position == 0:  # Deletion at the beginning
        return head.next
    
    temp = head
    for _ in range(position - 1):
        if temp.next is None:
            raise Exception("Position out of bounds")  # Invalid position
        temp = temp.next
    
    if temp.next is None:
        raise Exception("Position out of bounds")  # Invalid position
    
    temp.next = temp.next.next  # Skip over the node to delete
    return head
```

<table>
    <tr>
        <td>Deletion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

In a __Doubly Linked List__, deletion of a node also involves adjusting the _next_ and _prev_ pointers to adjacent nodes. 

```python3
# Structure of a Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Deletion at the Beginning
def deleteAtBeginning(head):
    if head is None:
        return None  # List is empty, nothing to delete
    
    if head.next is None:  # Only one node
        return None  # The list becomes empty after deletion
    
    head = head.next  # Move head to the next node
    head.prev = None  # Set the new head's prev to None
    
    return head

# Deletion at the End
def deleteAtEnd(head):
    if head is None:
        return None  # List is empty
    
    if head.next is None:  # Only one node in the list
        return None  # The list becomes empty after deletion
    
    temp = head
    while temp.next:  # Traverse to the last node
        temp = temp.next
    
    # temp is the last node
    temp.prev.next = None  # Set the second-to-last node's next to None
    
    return head

# Deletion at a Specific Position
def deleteAtPposition(head, position):
    if head is None:
        return None  # List is empty
    
    if position == 0:  # Deletion at the beginning
        return deleteAtBeginning(head)
    
    temp = head
    for _ in range(position):
        if temp.next is None:
            raise Exception("Position out of bounds")  # Invalid position
        temp = temp.next
    
    # Adjust the pointers of adjacent nodes
    if temp.next is not None:
        temp.next.prev = temp.prev
    
    temp.prev.next = temp.next
    
    return head
```

<table>
    <tr>
        <td>Deletion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End (Tail Pointer)</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End (Traverse List)</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

In a __Circular Linked List__, deleting nodes is similar to the above linked lists but requires additional handling to maintain the circular nature of the list. 

```python3
# Structure of a Circular Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Deletion at the Beginning
def deleteAtBeginning(head):
    if head is None:
        return None  # List is empty
    
    if head.next == head:  # Only one node
        return None  # The list becomes empty
    
    last = head
    while last.next != head:  # Find the last node
        last = last.next
    
    last.next = head.next  # Last node now points to the new head
    head = head.next  # Move head to the next node
    
    return head

# Deletion at the End
def deleteAtEnd(head):
    if head is None:
        return None  # List is empty
    
    if head.next == head:  # Only one node
        return None  # The list becomes empty
    
    temp = head
    while temp.next.next != head:  # Traverse to the second-to-last node
        temp = temp.next
    
    temp.next = head  # Second-to-last node points to the head
    
    return head

# Deletion at a Specific Position
def deleteAtPosition(head, position):
    if head is None:
        return None  # List is empty
    
    if position == 0:  # Deletion at the beginning
        return delete_at_beginning(head)
    
    temp = head
    for _ in range(position - 1):
        if temp.next == head:  # Reached the end, invalid position
            raise Exception("Position out of bounds")
        temp = temp.next
    
    temp.next = temp.next.next  # Bypass the node at the position
    
    return head
```

<table>
    <tr>
        <td>Deletion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(n) or O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(n)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

```python3
# Structure of a Circular Singly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Deletion at the Beginning
def deleteAtBeginning(head):
    if head is None:
        return None  # List is empty
    
    if head.next == head:  # Only one node
        return None  # The list becomes empty
    
    last = head.prev  # Last node
    last.next = head.next  # Last node now points to new head
    head.next.prev = last  # New head's prev points to last node
    
    head = head.next  # Move head to the next node
    
    return head

# Deletion at the End
def deleteAtEnd(head):
    if head is None:
        return None  # List is empty
    
    if head.next == head:  # Only one node
        return None  # The list becomes empty
    
    last = head.prev  # Last node
    last.prev.next = head  # Second-to-last node points to head
    head.prev = last.prev  # Head's prev points to new last node
    
    return head

# Deletion at a Specific Position
def deleteAtPosition(head, position):
    if head is None:
        return None  # List is empty
    
    if position == 0:  # Deletion at the beginning
        return delete_at_beginning(head)
    
    temp = head
    for _ in range(position):
        if temp.next == head:  # Invalid position
            raise Exception("Position out of bounds")
        temp = temp.next
    
    temp.prev.next = temp.next  # Adjust prev node's next
    temp.next.prev = temp.prev  # Adjust next node's prev
    
    return head
```

<table>
    <tr>
        <td>Deletion</td>
        <td>Time Complexity</td>
    </tr>
    <tr>
        <td>Beginning</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>End</td>
        <td>O(1)</td>
    </tr>
    <tr>
        <td>Specific Position</td>
        <td>O(n)</td>
    </tr>
</table>

## Practice Questions
### Warmups
[Problem 1: Linked List Cycle](https://github.com/organizedanvrchy/LeetCode/blob/main/Linked_List_Cycle.py)<br>
[Problem 2: Delete Node in a Linked List](https://github.com/organizedanvrchy/LeetCode/blob/main/Delete_Node_in_a_Linked_List.py)

### Session #1
[Problem 1: Rotate List](https://github.com/organizedanvrchy/LeetCode/blob/main/Rotate_List.py)<br>
[Problem 2: Swap Nodes in Pairs](https://github.com/organizedanvrchy/LeetCode/blob/main/Swap_Nodes_in_Pairs.py)<br>
[Problem 3: Remove Nth Node from List](https://github.com/organizedanvrchy/LeetCode/blob/main/Remove_Nth_Node_From_End_of_List.py)

### Session #2
[Problem 1: Shifting Letters](https://github.com/organizedanvrchy/LeetCode/blob/main/Shifting_Letters.py)<br>
[Problem 2: Set Matrix Zeroes](https://github.com/organizedanvrchy/LeetCode/blob/main/Set_Matrix_Zeroes.py)<br>
[Problem 3 (Bonus): Longest Repeated Character Replacement](https://github.com/organizedanvrchy/LeetCode/blob/main/Longest_Repeating_Character_Replacement.py)<br>
[Problem 4 (Bonus): Group Anagrams](https://github.com/organizedanvrchy/LeetCode/blob/main/Group_Anagrams.py)

[^1]:[GeekForGeeks](https://www.geeksforgeeks.org/linked-list-data-structure/)
[^2]:[Images from W3Schools](https://www.w3schools.com/dsa/dsa_data_linkedlists_types.php)
