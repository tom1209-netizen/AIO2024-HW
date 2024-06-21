class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")
        return self.items.pop()

    def push(self, element):
        if self.is_full():
            raise OverflowError("Cannot push to a full stack.")
        self.items.append(element)

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.items[-1]


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())  # Output: False
print(stack1.top())      # Output: 2
print(stack1.pop())      # Output: 2
print(stack1.top())      # Output: 1
print(stack1.pop())      # Output: 1
print(stack1.is_empty()) # Output: True
