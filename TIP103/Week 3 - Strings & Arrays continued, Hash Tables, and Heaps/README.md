# Hash Tables
This is a data structure that maps keys to values using the hash function. The data is generally stored in an _array_ where the position of each entry is determined by applying a hash function to the key. The main components of these data structures are:
1. __Hash Function__ <br> This transforms a key into an index
2. __Collision Handling__ <br> This includes strategies like _chaining_ and _open addressing_.

> [!TIP]
> Chaining is used when two different keys produce the same hash and map to the same index in the hash table. This includes the use of a _linked list_ at each index to hold all the key-value pairs that hash to the same index. Chaining offers a simple implementation and flexible growth but can produce memory overhead and slower lookups. <br><br>
> Open Addressing, on the other hand, keeps all entries in a hash table array itself and finds alternative positions for the colliding elements. Open addressing reduces clustering by implementing 1 of 3 possible techniques: __Linear Probing__, __Quadratic Probing__, and __Double Hashing__.

## Common Operations
Hash Tables are efficient for insertion, deletion, and lookup. Usually, these operations have an average O(1) time complexity, thus, making Hash Tables a popular choice for databases, compiler implementation, and language interpreters for symbol tables, quick lookups, and caching.

### Insertion
The insertion a key-value pair involves computing the hash of the key using a hash function, mapping the hash to an indea in the underlying array, and adding the element to that index. 
### Deletion
The removal of an element involves computing the hash of the key, locating the key in the corresponding 'bucket' and removing it (by adjusting pointers in chaining or marking as deleted in open addressing). 
### Lookup
Looking up a value involves computing the hash of the key and checking the bucket for the presence of the key. 

```python3
# Initialize a hash table (dictionary in Python)
hash_table = {}

# 1. Insertion
# Adding key-value pairs
hash_table["name"] = "Vimal"
hash_table["age"] = 25
hash_table["country"] = "Guyana"
print("After Insertion:", hash_table)

# 2. Deletion
# Removing a key-value pair
del hash_table["age"]
print("After Deletion:", hash_table)

# 3. Lookup
# Retrieving a value using a key
name = hash_table.get("name", "Key not found")  # Use .get() to handle missing keys gracefully
print("Lookup 'name':", name)

# Lookup for a non-existent key
state = hash_table.get("state", "Key not found")
print("Lookup 'state':", state)
```

# Heaps
These data structures are a specialized binary tree-based data structure that satisfies a __heap__ property. Data is commonly stored in arrays, where the parent and child relationships can be calculated by index (eg, for index _i_, left child is _(2 * i + 1)_, while right child is _(2 * i + 2)_. Heaps can either be:
1. __Max Heaps__ <br> This is where the parent node is greater than or equal to its children nodes.
2. __Min Heaps__ <br> This is where the parent node is less than or equal to its children nodes.

## Common Operations
Heaps are useful in scenarios that require efficient min or max element retrievals.

### Insertion
This is the addition of an element to the heap while maintaining the heap property. 
```python3
import heapq

# Create an empty heap
heap = []

# Insert elements
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 15)

print("After Insertion:", heap)  # Output will be a valid min-heap
```
Alternatively, for __Priority Queues__, __Dijkstra's Algorithm__, and __Scheduling Tasks__, we can use negative values or create a wrapper to simultae the max-heap since _heapq_ only supports min-heaps. This is done as:
```python3
max_heap = []
heapq.heappush(max_heap, -10)  # Insert negative value
heapq.heappush(max_heap, -20)
print("Max-Heap:", [-x for x in max_heap])  # Convert back to positive for readability

```
### Deletion
This is the removal of the root element while maintaining the heap property. 
```python3
# Remove the smallest element (root of the heap)
min_element = heapq.heappop(heap)
print("Deleted Element:", min_element)
print("After Deletion:", heap)
```
### Heapify
This is the transformation of an arbitrary list into a valid heap in O(n) time. 
```python3
# Given an unordered list
unsorted_list = [20, 1, 15, 10, 5, 25]

# Transform the list into a heap
heapq.heapify(unsorted_list)
print("After Heapify:", unsorted_list)  # Output will be a valid min-heap
```
