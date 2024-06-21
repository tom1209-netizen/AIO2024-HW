class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return IndexError("Queue is empty")

    def enqueue(self, element):
        if not self.is_full():
            self.items.append(element)
        else:
            raise OverflowError("Queue is full")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return IndexError("Queue is empty")


queue1 = Queue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())  # Output: False
print(queue1.front())    # Output: 1
print(queue1.dequeue())  # Output: 1
print(queue1.front())    # Output: 2
print(queue1.dequeue())  # Output: 2
print(queue1.is_empty())  # Output: True
