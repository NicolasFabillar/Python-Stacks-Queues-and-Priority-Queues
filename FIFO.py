from queues import Queue
fifo = Queue("1 - 1st", "2 - 2nd", "3 - 3rd")
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print("\nThe number of elements in deque:", len(fifo)) #this should print 6 because we added 6 elements.

print("\nThe elements: ")
for elements in fifo: #this shows all the elements by using the dequeue function, meaning it will remove the elements from the queue.
    print(elements)

print("\nThe number of elements in deque:", len(fifo)) #this should print 0 because the loop removed the elements.




