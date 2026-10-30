This project implements four data structures from first principles (without using Python's built-in insert(0) or pop(0)):
1.  ArrayStack 
2.  LinkedStack 
3.  ArrayQueue 
4.  LinkedQueue  


This includes the following application exercises:
-  Balanced parentheses checker ()[]{} using stack
-  Print queue simulation using FIFO queue


## Files
array_stack.py — Provides a fixed-size stack utilizing a sequential array backend.
linked_stack.py — Implements a dynamic stack structure built with interconnected nodes.
array_queue.py — Features a First-In, First-Out queue operating on a wrap-around circular buffer.
linked_queue.py — Constructs a dynamic queue managed via dedicated entry and exit references.
main.py — Houses the interactive console interface and core functional routines.
analysis.md — Documents the theoretical evaluation and answers to critical thinking questions.
README.md — Outlines project specifications and instructions for execution.


## Requirements
- Python 3

  
## How to Run
To execute the project, ensure Python 3 is installed on your environment. Clone or download all repository files into a single directory, open your terminal or command prompt in that directory, and run python main.py. You can then navigate through the interactive menu options to perform standard operations or purposely trigger and observe the handled overflow and underflow exceptions.


## Testing
1. Verify stack insertion, deletion, and inspection functions.
2. Trigger an underflow condition by attempting to extract an element from an empty container.
3. Trigger an overflow condition by exceeding the maximum limit of a fixed array structure.
4. Validate the circular buffer mechanism by removing an item and inserting a new element into the newly available index.
5. Evaluate expressions containing matching and mismatched bracket configurations.
6. Process simulated print tasks sequentially following First-In, First-Out (FIFO) ordering.


## Error Handling
Stack and queue operations explicitly manage errors by triggering an IndexError for underflows during pop(), peek(), dequeue(), or peek_front() on empty structures, and an OverflowError for overflows during push() or enqueue() on full array-based implementations (whereas dynamic linked structures do not overflow). These exceptions are wrapped in try...except blocks within the menu driver to catch errors and print warning messages cleanly without crashing the program.
