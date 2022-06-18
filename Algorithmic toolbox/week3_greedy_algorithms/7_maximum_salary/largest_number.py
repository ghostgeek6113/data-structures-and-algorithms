# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def comparison(digit, max_digit):
    return int(str(digit) + str(max_digit)) >= int(str(max_digit) + str(digit))


def largest_number(numbers):
    answer = []
    while numbers:
        max_digit = 0
        for digit in numbers:
            if comparison(digit, max_digit):
                max_digit = digit
        answer.append(max_digit)
        numbers.remove(max_digit)

    return ''.join([str(i) for i in answer])


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
