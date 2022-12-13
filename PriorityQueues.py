from heapq import heappop, heappush
from itertools import count

class IterableMixin: #Make it so that you can reuse the code in different classes.
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value) #Now elements with the same priority value can be sorted by their arrival time.
        heappush(self._elements, element)

    def dequeue(self):
        return heappop(self._elements)[-1] #prints the message without the 1st and 2nd value in the tuple.
