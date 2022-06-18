# Uses python3


def fibonacci_number_naive(n):
    print("Compute F sub", n)
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    fiblist = []
    fiblist.insert(0, 0)
    fiblist.insert(1, 1)
    for i in range(2, n + 1):
        fiblist.insert(i, (fiblist[i - 1] + fiblist[i - 2]))
    return fiblist[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
