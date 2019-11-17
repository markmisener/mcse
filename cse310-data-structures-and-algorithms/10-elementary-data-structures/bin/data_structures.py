"""Python implementations of non-native data structures."""


class Stack:
    """The class is based on the basic principle of last-in-first-out.

    In addition to the basic push and pop operations, the class provides
        three more functions of empty, search and peek. The class can
        also be said to extend Vector and treats the class as a stack
        with the five mentioned functions.
    """

    def __init__(self):
        """Initialize a stack."""
        self.items = []

    def isEmpty(self):
        """Checks if the stack has no elements.

        Args:
            self: this stack.

        Returns:
            bool: True if the stack has no elements. False if the stack
                has one or more elements.

        """
        return self.items == []

    def push(self, item):
        """Adds an element to the end of the list.

        Args:
            self: this stack.
            item: the element to add to the stack.

        Returns:
            None

        """
        self.items.append(item)

    def pop(self):
        """Removes the last element from the stack.

        Args:
            self: this stack.

        Returns:
            this stack with the last element removed.

        """
        return self.items.pop()

    def peek(self):
        """Returns the last element in the stack.

        Args:
            self: this stack.

        Returns:
            the last element of the stack.

        """
        return self.items[len(self.items) - 1]

    def size(self):
        """Get the number of elements in the stack.

        Args:
            self: this stack.

        Returns:
            the number of elements in the stack.

        """
        return len(self.items)
