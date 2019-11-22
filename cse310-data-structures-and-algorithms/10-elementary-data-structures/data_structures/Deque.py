"""Python implementation of a double-ended queue, allowing insertion and deletion at both ends."""

from Queue import Queue


class Deque(Queue):
    """A double-ended queue."""

    def __init__(self, n):
        """Initializes a deque."""
        self.head = 0
        self.tail = n - 1
        self.array = [None for i in range(n)]
        self.items = self.set_items()

    def set_items(self):
        self.items = [x for x in self.array if x is not None]

    def show(self):
        """Prints the deque's array."""
        print(self.array)

    def insert_head(self, item):
        """Inserts an item at the front of the deque.

        Args:
            self: this deque.
            item: item to insert.

        Returns:
            None

        """
        self.array[self.head] = item
        self.head = self.head + 1
        self.set_items()

    def insert_tail(self, item):
        """Inserts an item at the end of the deque.

        Args:
            self: this deque.
            item: item to insert.

        Returns:
            None

        """
        self.array[self.tail] = item
        self.tail = self.tail - 1
        self.set_items()

    def remove_head(self):
        """Removes the item at the front of the deque.

        Args:
            self: this deque.

        Returns:
            None

        """
        self.head = self.head - 1
        self.array[self.head] = None
        self.set_items()

    def remove_tail(self):
        """Removes the item at the end of the deque.

        Args:
            self: this deque.

        Returns:
            None

        """
        self.tail = self.tail + 1
        self.array[self.tail] = None
        self.set_items()
