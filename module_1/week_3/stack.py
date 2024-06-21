class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        return self.stack.pop()

    def push(self, element):
        self.stack.append(element)

    def top(self):
        return self.stack[-1]


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
print(stack1.is_full())  # Output: False
print(stack1.top())      # Output: 2
print(stack1.pop())      # Output: 2
print(stack1.top())      # Output: 1
print(stack1.pop())      # Output: 1
print(stack1.is_empty()) # Output: True
