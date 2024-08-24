from collections import deque


# Queue => dequeue , enqueue
# Stack => peek , is_empty, size

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            self.queue.pop()
            return
        raise Exception('Stack is empty')

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        raise Exception('Stack is empty')

    def size(self):
        return len(self.queue)