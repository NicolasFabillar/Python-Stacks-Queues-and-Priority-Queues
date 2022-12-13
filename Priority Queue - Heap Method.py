from heapq import heappop
from heapq import heappush


fruits = []
heappush(fruits, "mango")
heappush(fruits, "apple")
heappush(fruits, "banana")

print("The order is:", fruits)

heappop(fruits) #The first on on the heap will always be the one you will get when you pop.

print("\nThe first one is gone:", fruits)



