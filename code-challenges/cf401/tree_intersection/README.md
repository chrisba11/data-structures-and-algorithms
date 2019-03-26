# Tree Intersection
This function takes in a string and checks to see if any of the words are repeated. If there is a repeat, it will return a string of the first word that is repeated. If there are no repeats, it will return False.

## Challenge
- Write a function called `tree_intersection` that takes two binary tree parameters.
- Without utilizing any of the built-in library methods available to your language, return a set of values found in both trees.

## Approach
- I instantiated a hashtable and an empty array to start. 
- I then created an internal function that adds every node in the first binary tree to the hashtable. 
- I then created another internal function that runs the hashtables `contains` method to determine if the `data` property of each node of the second binary tree is found in the hashtable. 
    - If a match is found, that value is appended to the array. 
- I called the first function with the first binary tree and the second function with the second binary tree.
- Then I return the array of matching values.

## Efficiency
- BigO of time is O(n), since it has to add each of the first tree's node values to the hashtable and it has to run through every node of the second tree to see if there's a match.
- BigO of space is O(n), since we are pushing the value from each node of the first tree into a hashtable and generating an array of matching values.

## Solution
![repeated_word image](../assets/repeated_word.jpg)