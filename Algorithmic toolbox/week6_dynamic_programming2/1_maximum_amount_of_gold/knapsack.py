# Uses python3
import sys


def optimal_weight(W, w):
    value = dict()
    length = len(w)
    for i in range(length):
        value[0, i] = 0
    for x in range(W + 1):
        value[x, 0] = 0
    for i in range(1, length + 1):
        for x in range(1, W + 1):
            value[x, i] = value[x, i - 1]
            if w[i - 1] <= x:
                val = value[x - w[i - 1], i - 1] + w[i - 1]
                if val > value[x, i]:
                    value[x, i] = val
    return value[W, length]


if __name__ == '__main__':
    capacity, number_bar = list(map(int, input().split()))
    weight_bars = list(map(int, input().split()))
    print(optimal_weight(capacity, weight_bars))
