# Uses python3
import sys


def get_change(m):
    min_coins = dict()
    min_coins[0] = 0
    denominations = [1, 3, 4]
    for i in range(1, m + 1):
        min_coins[i] = 1000000
        for j in denominations:
            if i >= j:
                coins = 1 + min_coins[i - j]
                if coins < min_coins[i]:
                    min_coins[i] = coins

    return min_coins[m]


if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
