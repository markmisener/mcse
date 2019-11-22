"""Exercise 10.1-4."""
# Rewrite ENQUEQUE and DEQUEQUE to detect underflow and overflow of a queue.


class Queue:
    """The class is based on the basic principle of first-in-first-out.

    This class contains modified enqueue and dequeue functions.
    """

    def __init__(self, n=10):
        """Initilize a queue."""
        self.items = []
        self.max_items = n

    def enqueue(self, item):
        """Adds an element to the end of the queue.

        This modified function detects for queue overflow.

        Args:
            self: this queue.
            item: the element to add to the queue.

        Returns:
            None

        """
        if self.size() + 1 > self.max_items:
            raise OverflowError(
                "Queue overflow! Cannot have more than {} items in the queue".format(
                    self.max_items
                )
            )

        self.items.insert(0, item)

    def dequeue(self):
        """Removes the first element from the queue.

        This modified function detects for queue underflow.

        Args:
            self: this queue.

        Returns:
            this queue with the first element removed.

        """
        if self.size() == 0:
            raise IndexError("Queue underflow! There are no items in the queue.")
        return self.items.pop()

    def size(self):
        """Get the number of elements in the queue.

        Args:
            self: this queue.

        Returns:
            the number of elements in the queue.

        """
        return len(self.items)


if __name__ == "__main__":
    Q = Queue(n=10)

    # no items in queue, dequeue should fail
    try:
        Q.dequeue()
    except IndexError as e:
        print("Underflow successfully detected!")
        print("Returned: {}".format(e))

    # fill the queue
    for i in range(10):
        Q.enqueue(i)

    # try to overflow the queue, should fail
    try:
        Q.enqueue(11)
    except OverflowError as e:
        print("Overflow successfully detected!")
        print("Returned: {}".format(e))
