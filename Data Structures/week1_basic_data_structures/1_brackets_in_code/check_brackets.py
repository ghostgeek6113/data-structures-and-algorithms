# python3 Task. Your friend is making a text editor for programmers. He is currently working on a feature that will
# find errors in the usage of different types of brackets. Code can contain any brackets from the set []{}(),
# where the opening brackets are [,{, and ( and the closing brackets corresponding to them are ],}, and ). For
# convenience, the text editor should not only inform the user that there is an error in the usage of brackets,
# but also point to the exact place in the code with the problematic bracket. First priority is to find the first
# unmatched closing bracket which either doesn’t have an opening bracket before it, like ] in ](), or closes the
# wrong opening bracket, like } in ()[}. If there are no such mistakes, then it should find the first unmatched
# opening bracket without the corresponding closing bracket after it, like ( in {}([]. If there are no mistakes,
# text editor should inform the user that the usage of brackets is correct. Apart from the brackets, code can contain
# big and small latin letters, digits and punctuation marks. More formally, all brackets in the code should be
# divided into pairs of matching brackets, such that in each pair the opening bracket goes before the closing
# bracket, and for any two pairs of brackets either one of them is nested inside another one as in (foo[bar]) or they
# are separate as in f(a,b)-g[c]. The bracket [ corresponds to the bracket ], { corresponds to }, and ( corresponds
# to ).
# Input Format. Input contains one string 𝑆 which consists of big and small latin letters, digits, punctuation
# marks and brackets from the set []{}().
# Constraints. The length of 𝑆 is at least 1 and at most 105.
# Output Format. If the code in 𝑆 uses brackets correctly, output “Success" (without the quotes).
# Otherwise, output the 1-based index of the first unmatched closing bracket, and if there are no unmatched closing
# brackets, output the 1-based index of the first unmatched opening bracket.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)

        elif next in ")]}":
            if len(opening_brackets_stack) > 0:
                if are_matching(opening_brackets_stack[-1], next):
                    opening_brackets_stack.pop()
                else:
                    return i + 1
            else:
                return i + 1
    if len(opening_brackets_stack) > 0:
        return len(opening_brackets_stack)
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
