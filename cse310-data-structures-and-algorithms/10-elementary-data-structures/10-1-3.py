"""Exercise 10.1-3."""
# Using Figure 10.2 as a model, illustrate the result of each operation in the
# sequence ENQUEQUE(Q,4), ENQUEQUE(Q,1), ENQUEQUE(Q,3), DEQUEQUE(Q),
# ENQUEQUE(Q,8), and DEQUEQUE(Q) on an initially empty queue Q stored in
# array Q[1...6].
from data_structures.Queue import Queue

if __name__ == "__main__":
    Q = Queue()
    print(Q.items)

    Q.enqueue(4)
    print(Q.items)

    Q.enqueue(1)
    print(Q.items)

    Q.enqueue(3)
    print(Q.items)

    Q.dequeue()
    print(Q.items)

    Q.enqueue(8)
    print(Q.items)

    Q.dequeue()
    print(Q.items)
