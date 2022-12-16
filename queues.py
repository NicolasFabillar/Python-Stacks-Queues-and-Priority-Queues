# queues.py

from collections import deque
from dataclasses import dataclass
from heapq import heapify, heappop, heappush
from itertools import count
from typing import Any

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

class Stack(Queue): #Inherits the Queue class.
    def dequeue(self): #Overrides the function of dequeue in the parent class.
        return self._elements.pop() #Remove the elements on the right, removes the last in.

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

@dataclass(order=True)
class Element:
    priority: float
    count: int
    value: Any

class MutableMinHeap(IterableMixin):
    def __init__(self):
        super().__init__()
        self._elements_by_value = {}
        self._elements = []
        self._counter = count()

    def __setitem__(self, unique_value, priority):
        if unique_value in self._elements_by_value:
            self._elements_by_value[unique_value].priority = priority
            heapify(self._elements)
        else:
            element = Element(priority, next(self._counter), unique_value)
            self._elements_by_value[unique_value] = element
            heappush(self._elements, element)

    def __getitem__(self, unique_value):
        return self._elements_by_value[unique_value].priority

    def dequeue(self):
        return heappop(self._elements).value

