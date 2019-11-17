"""Exercise 10."""
# Using Figure 10.1 as a model, illustrate the result of each operation in the
# sequence PUSH(S,4), PUSH(S,1), PUSH(S,3), POP(S), PUSH(S,8), and POP(S) on
# an initially empty stack S stored in array S[1...6].
from bin import data_structures

if __name__ == "__main__":
    S = data_structures.Stack()
    print(S.items)

    S.push(4)
    print(S.items)

    S.push(1)
    print(S.items)

    S.push(3)
    print(S.items)

    S.pop()
    print(S.items)

    S.push(8)
    print(S.items)

    S.pop()
    print(S.items)
