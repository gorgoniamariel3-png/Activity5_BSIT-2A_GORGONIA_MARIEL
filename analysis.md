# Analysis Questions & Answers

Why does the linked-list stack push and pop at the head instead of the tail?
A linked-list stack performs push and pop operations at the head because insertion and deletion at the beginning of a singly linked list can be executed in constant time $O(1)$. If operations were performed at the tail, removing an element (popping) would require traversing the entire list to find the second-to-last node so its `next` pointer could be set to `None`, resulting in an inefficient $O(n)$ time complexity.

Why must the array queue be implemented as circular?
In a naive linear array implementation of a queue, dequeueing elements from the front leaves unused empty spaces behind, eventually causing a false overflow even when physical space is available. Alternatively, shifting all remaining elements forward after every dequeue operation takes $O(n)$ time. By treating the array as circular using the modulo operator (`(front + size) % capacity`), indices wrap around the ends, allowing empty slots at the beginning of the array to be reused efficiently while maintaining $O(1)$ time complexity for both enqueue and dequeue operations.
