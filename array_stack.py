class Node:
    """A node class for linked structures."""
    def __init__(self, value):
        self.value = value
        self.next = None


class ArrayStack:
    """Fixed-size array-based stack implementation."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack overflow: Cannot push to a full array stack.")
        self.top += 1
        self.data[self.top] = value

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek.")
        return self.data[self.top]

    def __str__(self):
        if self.is_empty():
            return "ArrayStack (top to bottom): [Empty]"
        items = [str(self.data[i]) for i in range(self.top, -1, -1)]
        return f"ArrayStack (top to bottom): {' -> '.join(items)}"


