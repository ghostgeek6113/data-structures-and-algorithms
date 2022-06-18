# python3


def gcd_naive(a, b):
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    if b == 0:
        divisor = a
        return divisor
    else:
        reminder = a % b
        return gcd(b, reminder)


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    # input_a = int(input())
    # input_b = int(input())
    print(gcd(input_a, input_b))
