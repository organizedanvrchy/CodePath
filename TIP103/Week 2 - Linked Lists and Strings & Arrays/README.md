# Strings
Strings are a sequence of characters stored in contiguous memory locations and can include letters, numbers, symbols, and whitespaces. Characters in a string can be represented by specific encoding, such as ASCII (Maps 128 characters to numbers 0 to 127) or Unicode. In some programming languages, strings are immutable (cannot be changed after creation), where operations on the string often lead to the creation of a new string instead of modifying the original. While in other programming languages, strings are mutable (such as in C++), where they can be modified in-place. Strings are often represented using either single quotes or double quotes; however, some languages will mostly likely use single quotes to denote characters and double quotes to denote strings. 
> [!NOTE]
> When using a language that supports ASCII (such as Python), the ord() function can be used to get the integer value that the character is mapped to and chr() can be used to get the character that the integer value is mapped to. 

## Common Escape Sequences
Escape sequences are special character sequences that are non-printable. They usually start with a "\". Some frequent examples include:
1. __\n__ - Newline
2. __\t__ - Tab
3. __\\__ - Backslash
4. __\"__ - Double Quote

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
WIP...
# Linked Lists
Linked Lists are fundamental data structures for storing collections of elements. Linked Lists allow for more efficient insertion and deletion operations when compared to arrays since they consist of nodes that point to the next node in a sequence and do not use contiguous blocks or memory. Linked Lists also have dynamic size, allowing for growing and shrinking as necessary. However, these lists require additional memory for the pointers and only offer sequential access to nodes (which might be slower than random access in arrays).[^1]

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
  - where each node has just one pointer to the next node and the last node points back to the first node instead of null.
  - 
<picture>
   <img alt="Circular Singly Linked Lists" src="https://www.w3schools.com/dsa/img_linkedlists_circsingly.svg">
</picture>

> [!NOTE]
> Images sourced from this link (in footnotes)[^2]

2. Circular Doubly Linked Lists<br>
  - where each node has two pointers to the previous and next nodes, but here, there first node's previous pointer points to the last node and the last node's next pointer points to the first node.

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
### Traversal
This is simply the visiting of each node in the linked link and is generally the precursor to some other operation such as print or process the data in a node. This can be done as shown below (using Python):

```python3
def traverseLL(head):
    curr = head # Initialize a current node to point to the head of the list

    # Walk curr down the list until it reaches the end (last node points to None)
    while curr is not None:
        print(curr.data) # Or some other operation
        curr = curr.next # Move to the next node
```

### Searching
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
### Finding Length of a Linked List
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

### Insertion
This operation adds a new node to the list. Node insertion can either be at the beginning of a list, end of a list, or a specific position in the list. 

__Inserting at the beggining of the list__ <br>
In Singly Linked Lists, insertion at the beginning involves creating a new node, setting the next point of the the new node to the current head of the list, moving the head to point to the new node, and return the new head.

```python3
```

In a Doubly Linked List,

```python3
```

In a Circular Linked List, 

```python3
```

__Inserting at the end of the list__ <br>
In Singly Linked Lists, insertion at the end involves

```python3
```

In a Doubly Linked List,

```python3
```

In a Circular Linked List, 

```python3
```

__Inserting at a specific point in the list__ <br>
In Singly Linked Lists, insertion at the end involves

```python3
```

In a Doubly Linked List,

```python3
```

In a Circular Linked List, 

```python3
```
### Deletion

### Deletion



[^1]:[GeekForGeeks](https://www.geeksforgeeks.org/linked-list-data-structure/)
[^2]:[Images from W3Schools](https://www.w3schools.com/dsa/dsa_data_linkedlists_types.php)
