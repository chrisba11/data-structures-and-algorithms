# Hashtable

## Challenge
- Implement a Hashtable with the following methods:

    - add: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.
    - get: takes in the key and returns the value from the table.
    - contains: takes in the key and returns a boolean, indicating if the key exists in the table already.
    - hash: takes in an arbitrary key and returns an index in the collection.

## Approach
I brought in my `Node` and `LinkedList` classes from our linked list challenge.

For the `Hashtable` class, I initialized an instance with an array full or buckets holding empty linked lists.

The `hash` method will take in a key and hash it to return an index between 0 and 1024.

The `add` method will take in a key and value and insert a node into the linked list at the index of the array generated by the the hashed key. This method will allow you to add duplicates of the same key.

The `get` method will check the index of a key (by hashing the key to get the index) and check to see if the key is found in any of the linked list's nodes. If it is found, the value of that key will be returned. If more than one matching key is found, it will return a string of each value that matches the supplied key. The values will be separated by ' | ' so they can be read easily or split apart by the caller.

The `contains` method will check the index of a key (by hashing the key to get the index) and check to see if the key is found in any of the linked list's nodes. If it is found, it will return **_True_**. If not, it will return **_False_**.

## Efficiency
`hash` has time and space efficiencies of O(1).

`add` has time and space efficiencies of O(1).

`get` has time and space efficiencies of O(1), but really it's higher because it has to traverse the linked list to check for the key and they I'm producing an array of values that then get iterated through to produce a string that is being returned. But, it's not going to run through all of the indices of the hashtable array, so it's a tough call.

`contains` has the same predicament as `get`. O(1), mostly.



