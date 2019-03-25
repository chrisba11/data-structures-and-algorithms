# Repeated Word
<!-- This function takes in a tree and replaces all numbers divisible by 3 with 'Fizz', all numbers divisible by 5 with 'Buzz' and all numbers divisible by 3 and 5 with 'Fizz-Buzz'. It then returns the modified tree. -->

## Challenge
<!-- - Write a function called FizzBuzzTree which takes a tree as an argument.
- Without utilizing any of the built-in methods available to your language, determine weather or not the value of each node is divisible by 3, 5 or both, and change the value of each of the nodes:
- If the value is divisible by 3, replace the value with “Fizz”
- If the value is divisible by 5, replace the value with “Buzz”
- If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
- Return the tree with its new values. -->

## Approach
<!-- I traversed the tree in a pre-order and checked the values to see if they fit the requirements, if so, I replaced the value and then checked the children, if they existed and recursed. -->

## Efficiency
<!-- Time O(n) Space O(n) -->

## Solution
![repeated_word image](../assets/repeated_word.jpg)