class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def enqueue(self, element):
        if not self.is_full():
            self.queue.append(element)
        else:
            raise Exception("Queue is full")

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None


queue1 = Queue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
print(queue1.is_full())  # Output: False
print(queue1.front())    # Output: 1
print(queue1.dequeue())  # Output: 1
print(queue1.front())    # Output: 2
print(queue1.dequeue())  # Output: 2
print(queue1.is_empty()) # Output: True
