# Stacks and Queues

## Challenge
- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
    - This object should be aware of a default empty value assigned to top when the stack is created.
    - Define a method called `push` which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
    - Define a method called `pop` that does not take any argument, removes the node from the top of the stack, and returns the node’s **_value_**.
    - Define a method called `peek` that does not take an argument and returns the **_value_** of the node located on the top of the stack.
- Create a Queue class that has **_front_** and **_rear_** attributes. It creates an empty queue when instantiated.
    - This object should be aware of a default empty value assigned to front when the queue is created.
    - Define a method called `enqueue` which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
    - Define a method called `dequeue` that does not take any argument, removes the node from the front of the queue, and returns the node’s **_value_**.
    - Define a method called `peek` that does not take an argument and returns the **_value_** of the node located in the front of the stack.
- At no time should an exception or stack trace be shown to the end user. Catch and handle any such exceptions and return a printed value or operation which cleanly represents the state and either stops execution cleanly, or provides the user with clear direction and output.
- Be sure to follow your languages best practices for naming conventions.

## Approach
For the Node class, I simply utilized the Node class we produced in our Linked List challenge, which initializes a new node with an attribute for the *data* passed in and an attribute for the next node in whichever data structure it is used in.

---

For the Stack class, I initialize a stack with an attribute of **_top_**. 

For Stack's `push` method, I create a new node and I check to see if there are nodes in the stack. If not, I just assign the stack's **_self.top_** attribute to the new node. If the stack is not empty, I assign the new node's **_\_next_** attribute equal to **_self.top_** and reassign **_self.top_** to the new node.

For Stack's `pop` method, I check to see if there are nodes in the stack. If so, I use a temporary variable **_current_** to store the **_self.top_** value. I then reassign **_self.top_** to be the value of its **_\_next_** attribute. Last, I assign **_current.\_next_** to **None** and then return **_current.data_**. If the stack is empty, I return the string 'Empty Stack'.

For the Stack's `peek` method, I check that the stack's **_self.top_** is not **None**. If not, I return **_self.top.data_**. If **_self.top_** is **None**, I return the string 'Empty Stack'.

---

For the Queue class, I initialize a queue with attributes of **_front_** and **_rear_**.

For the Queue's enqueue method, I create a new node and I check to see if **_self.rear_** is None. If it is, I reassign **_self.rear_** & **_self.front_** to the new node. If not, I assign **_self.rear.\_next_** to be the new node and then change **_self.rear_** to the new node.

For the Queue's `dequeue` method, I verify that **_self.front_** is not **None**. Then I assign a temporary variable current to the value of **_self.front_**. Next, I reassign **_self.front_** to equal **_self.front.\_next_** and **_current.\_next_** to **None**. Then I return **_current.data_**. If self.front was **None** to start, then I return the string 'Empty Queue'.

For the Queue's `peek` method, I verify that the queue's **_self.front_** is not **None**. If not, I return **_self.front.data_**. If **_self.front_** is **None**, I return the string 'Empty Queue'.

## Efficiency
All Methods in this module have the same BigO time and space complexity of O(1).



