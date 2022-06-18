# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(keys, query):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    assert 1 <= len(keys) <= 3 * 10 ** 4
    # sorted(keys)

    # print(len(keys))
    low_index = 0
    high_index = len(keys) - 1
    # print(high_index)
    while low_index <= high_index:
        mid_index = ((high_index + low_index) // 2)
        # print(low_index)
        # print(mid_index)
        # print(high_index)
        if query == keys[mid_index]:
            return mid_index
        elif query > keys[mid_index]:
            low_index = mid_index + 1
        elif query < keys[mid_index]:
            high_index = mid_index - 1
    return - 1


if __name__ == '__main__':

    input_number = int(input())
    input_keys = list(map(int, input().split()))[0:]
    input_number_number = int(input())
    input_queries = list(map(int, input().split()))[0:]
    # sorted_key = input_keys.sort()
    # print(sorted_key)
    # print(input_keys)
    # print(sorted(input_keys))
    # print(binary_search(input_keys, input_number), end=' ')
    for q in input_queries:
        # print(q)
        print(binary_search(input_keys, q), end=' ')
