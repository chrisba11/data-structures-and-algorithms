# Insertion Sort

## Challenge
- Write a function for insertion sort that takes in an unsorted array and returns the array sorted using insertion sort.

## Approach
- I started by comparing the first two elements in the array, if the one on the right was smaller, I swapped the two.
- Then I moved through each one in a loop repeating that process until the current was not smaller than the one to its left.
- Once I hit the length of the array, I stop the outer loop.

## Efficiency
Time: O(n^2)
SPace: O(1) because I am modifying the array in place and the memory usage does not change with the input array size.



