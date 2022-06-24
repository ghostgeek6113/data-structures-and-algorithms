# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        # print(i)
        # print(next)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            print(opening_brackets_stack)
            # pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                return False
            if are_matching(opening_brackets_stack[-1], next):
                print(opening_brackets_stack)
                opening_brackets_stack.pop()
                return "success"
            else:
                print(opening_brackets_stack)
                return i
            # pass



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)
    # print(are_matching('{','}'))


if __name__ == "__main__":
    main()
