# Binary Search
The program checks to see if a value is found inside a list. If it is, it returns the index of the value, otherwise it returns -1.

## Collaboration
Chris Ball, Andrew Helmer, and Tim Schoen worked together on whiteboarding the problem, but split apart to work on code individually.

## Challenge
Write a function called `binary_search` which takes in 2 parameters: a sorted array and the search key. Without utilizing any of the built-in methods available to your language, return the index of the array’s element that is equal to the search key, or -1 if the element does not exist.

## Approach
We found the mid point of the array and checked to see if the element at that index matched the input value. If yes, we printed the element at that index. If the input value was higher than the element at the midpoint, we changed the start point to be the current midpoint, then changed the midpoint to be the center of the new list section and repeated the process. If the input value was lower than the element at the midpoint, we changed the end point to be the current midpoint and then changed the midpoint to be the center of the new list section and repeated the process. Once the input value equals the element at the midpoint, it would print the index of that element.

## Efficiency
Time = O(log(n))
Space = O(1)

## Solution
![array_shift image](../assets/array_binary_search.jpg)