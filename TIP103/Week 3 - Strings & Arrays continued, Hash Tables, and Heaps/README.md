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
### Deletion
### Lookup

# Heaps
These data structures are a specialized tree-based data structure that satisfies a __heap__ property. Data is commonly stored in arrays, where the parent and child relationships can be calculated by index (eg, for index _i_, left child is _(2 * i + 1)_, while right child is _(2 * i + 2)_. Heaps can either be:
1. __Max Heaps__ <br> This is where the parent node is greater than or equal to its children nodes.
2. __Min Heaps__ <br> This is where the parent node is less than or equal to its children nodes.

## Common Operations
Heaps are useful in scenarios that require efficient min or max element retrievals, 
### Insertion
### Deletion
### Heapify
