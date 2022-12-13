from queues import Stack

lifo = Stack("1st", "2nd", "3rd")
lifo.enqueue("4th")
lifo.enqueue("5th")
lifo.enqueue("6th")

print("\nNow the elements are printed in reverse, which means that it is in Last in, First-out order.")
for element in lifo:
    print(element)