# Hash Tables
This is a data structure that maps keys to values using the hash function. The data is generally stored in an _array_ where the position of each entry is determined by applying a hash function to the key. The main components of these data structures are:
1. __Hash Function__ <br> This transforms a key into an index
2. __Collision Handling__ <br> This includes strategies like _chaining_ and _open addressing_.

> [!TIP]
> Chaining is used when two different keys produce the same hash and map to the same index in the hash table. This includes the use of a _linked list_ at each index to hold all the key-value pairs that hash to the same index. Chaining offers a simple implementation and flexible growth but can produce memory overhead and slower lookups. <br><br>
> Open Addressing, on the other hand, keeps all entries in a hash table array itself and finds alternative positions for the colliding elements. 


# Heaps
