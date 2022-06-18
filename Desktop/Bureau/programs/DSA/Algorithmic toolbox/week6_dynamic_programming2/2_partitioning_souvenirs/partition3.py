# Uses python3
import sys
import itertools


def partition3(A):
    total = sum(A)
    if total % 3 != 0:
        return 0

    size = total // 3
    n = len(A)

    count = 0
    table = [[0] * (n + 1) for _ in range(size + 1)]
    for i in range(1, size + 1):
        for j in range(1, n + 1):
            table[i][j] = table[i][j - 1]
            if A[j - 1] <= i:
                temp = table[i - A[j - 1]][j - 1] + A[j - 1]
                if temp > table[i][j]:
                    table[i][j] = temp
            if table[i][j] == size:
                count += 1

    if count < 3:
        return 0
    else:
        return 1


if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(partition3(A))
