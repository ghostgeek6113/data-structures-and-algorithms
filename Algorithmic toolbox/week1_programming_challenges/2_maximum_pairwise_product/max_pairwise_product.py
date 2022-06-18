# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                               numbers[first] * numbers[second])
#
#     return max_product
#

def max_pairwise_product_fast(numbers):
    sorted_list = sorted(numbers)
    first_largest_number = sorted_list[-1]
    second_largest_number = sorted_list[-2]
    max_product = first_largest_number * second_largest_number
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
