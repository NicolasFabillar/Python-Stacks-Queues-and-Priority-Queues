# queues.py

from collections import deque

class Queue:
    # this make it so that it can accept multiple elements initially or it can create deque without elements.)
    def __init__(self, *element):
        self._elements = deque(element)

    def __len__(self): #this makes it compatible with len function, we can now use len on the elements.
        return len(self._elements)

    def __iter__(self):#this makes it compatible with loops, we can now use the elements on loops.
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
