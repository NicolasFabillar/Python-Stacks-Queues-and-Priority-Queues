# queues.py

from collections import deque

class Queue:
    # this make it so that it can accept multiple elements initially or it can create deque without elements.)
    def __init__(self, *element):
        self._elements = deque(element)

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
