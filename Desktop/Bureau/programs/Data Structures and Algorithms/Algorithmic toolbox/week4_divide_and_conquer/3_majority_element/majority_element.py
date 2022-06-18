# # Uses python3
# import sys
#
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(15000)
#
#
# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     for i in range(left, right):
#         current_element = a[i]
#         count = 0
#         for j in range(left, right):
#             if a[j] == current_element:
#                 count += 1
#         if count > len(a) / 2:
#             return a[i]
#     return -1
#
#
# def merge(a, b):
#     c = []
#     if a:
#         for i in range(0, len(a)):
#             c.append(a[i])
#     if b:
#         for j in range(0, len(b)):
#             c.append(b[j])
#     return c
#
#
# def get_majority_element_divide_and_conquer(a, left, right):
#     if left == right - 1:
#         return a[left]
#     middle = int(len(a) / 2)
#     left_array = a[:middle]
#     right_array = a[middle:]
#     elements_left = get_majority_element_divide_and_conquer(left_array, left, middle)
#     elements_right = get_majority_element_divide_and_conquer(right_array, middle + 1, right)
#     element_left_count = 0
#     element_right_count = 0
#
#     for i in a:
#         if i == elements_left:
#             element_left_count += 1
#         if i == elements_right:
#             element_right_count += 1
#     if element_left_count > middle:
#         return elements_left
#     elif element_right_count > middle:
#         return elements_right
#     else:
#         return -1
#
#
# if __name__ == '__main__':
#     input_n = int(input())
#     # n, *a = list(map(int, input.split()))
#     input_array = list(map(int, input().split()))[0:]
#     if get_majority_element_divide_and_conquer(input_array, 0, input_n) != -1:
#         print(1)
#     else:
#         print(0)

import sys


def get_majority_element(seq, left, right):
    """
    Gets the element in the sequence that makes up the majority if it exists.

    :param seq: sequence of elements
    :param left: starting index in the sequence
    :param right: end index in the sequence
    :return: the majority element count, otherwise -1 if DNE

    >>> get_majority_element([2, 3, 9, 2, 2], 0, 5)
    3

    >>> get_majority_element([1, 2, 3, 4], 0, 4)
    -1

    >>> get_majority_element([1, 2, 3, 1], 0, 4)
    -1
    """
    if left == right:
        return -1

    if left + 1 == right:
        return seq[left]

    seq.sort()
    current = left
    next_index = left

    while next_index < right:
        count = 0

        while next_index < right and seq[next_index] == seq[current]:
            next_index += 1
            count += 1

        if count > left + ((right - left) // 2):
            return next_index

        current = next_index

    return -1


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
