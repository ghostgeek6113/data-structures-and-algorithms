# Uses python3
import sys


def optimal_sequence(n):
    table = [0] * (n + 1)

    for t in range(1, len(table)):
        table[t] = table[t - 1] + 1
        if t % 2 == 0:
            table[t] = min(table[t], table[t // 2] + 1)
        if t % 3 == 0:
            table[t] = min(table[t], table[t // 3] + 1)

    # return (table[-1] - 1)  #is the length of the list of sequences including

    number_sequence = [1] * table[-1]
    for t in range(1, table[-1]):
        number_sequence[-t] = n

        if table[n - 1] == table[n] - 1:
            n -= 1
        elif n % 2 == 0 and (table[n // 2] == table[n] - 1):
            n //= 2
        else:
            n //= 3
    return number_sequence


if __name__ == '__main__':
    # input = int(input())
    n = int(input())
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
