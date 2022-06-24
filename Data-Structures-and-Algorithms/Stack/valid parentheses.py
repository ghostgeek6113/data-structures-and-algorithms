# Leetcode problem 20
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if
# the input string is valid.
# An input string is valid if:
#
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Example
# 1:
#
# Input: s = "()"
# Output: true
# Example
# 2:
#
# Input: s = "()[]{}"
# Output: true
# Example
# 3:
#
# Input: s = "(]"
# Output: false
def matches(opening, closing):
    return (opening + closing) in ['()', '{}', '[]']


def is_valid(s: str) -> bool:
    open_bracket = []
    for i, next in enumerate(s):
        if next in '([{':
            open_bracket.append(next)
        elif next in ')]}':
            if len(open_bracket) > 0:
                if matches(open_bracket[-1], next):
                    open_bracket.pop()
                else:
                    return False
            else:
                return False
    if len(open_bracket) > 0:
        return False
    return True


def main():
    text = input()
    mismatch = is_valid(text)
    print(mismatch)


if __name__ == "__main__":
    main()
