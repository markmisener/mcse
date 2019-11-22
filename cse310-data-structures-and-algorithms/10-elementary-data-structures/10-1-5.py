"""Exercise 10.1-5."""
# Whereas a stack allows insertion and deletion of elements at only one end
# and a queue allows insertion at one end and deletion at the other end,
# a deque (double-ended queue) allows insertion and deletion at both ends.
# Write four O(1)-time procedures to insert elements into and delete
# elements from both ends of a deque implemented by an array.
from data_structures.Deque import Deque


if __name__ == "__main__":
    D = Deque(n=5)
    D.show()

    # insert at head
    D.insert_head(10)
    D.show()

    # insert at tail
    D.insert_tail(1)
    D.show()

    # remove at head
    D.remove_head()
    D.show()

    # remove at tail
    D.remove_tail()
    D.show()
