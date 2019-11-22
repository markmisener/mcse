"""Python implementation of a queue."""


class Queue:
    """The class is based on the basic principle of first-in-first-out.

    In addition to the basic enqueue and dequeue operations, the class provides
        two more functions of isempty and size.
    """

    def __init__(self):
        """Initilize a queue."""
        self.items = []

    def isEmpty(self):
        """Checks if the stack has no elements.

        Args:
            self: this queue.

        Returns:
            bool: True if the queue has no elements. False if the queue
                has one or more elements.

        """
        return self.items == []

    def enqueue(self, item):
        """Adds an element to the end of the queue.

        Args:
            self: this queue.
            item: the element to add to the queue.

        Returns:
            None

        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes the first element from the queue.

        Args:
            self: this queue.

        Returns:
            this queue with the first element removed.

        """
        return self.items.pop()

    def size(self):
        """Get the number of elements in the queue.

        Args:
            self: this queue.

        Returns:
            the number of elements in the queue.

        """
        return len(self.items)
