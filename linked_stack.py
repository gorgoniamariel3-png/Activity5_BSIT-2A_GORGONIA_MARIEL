class LinkedStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def is_full(self):
        return False  # Linked stacks do not overflow unless memory runs out

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: Cannot pop from an empty stack.")
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty: Cannot peek.")
        return self.top.value

    def __str__(self):
        if self.is_empty():
            return "LinkedStack (top to bottom): [Empty]"
        items = []
        current = self.top
        while current is not None:
            items.append(str(current.value))
            current = current.next
        return f"LinkedStack (top to bottom): {' - '.join(items)}"
