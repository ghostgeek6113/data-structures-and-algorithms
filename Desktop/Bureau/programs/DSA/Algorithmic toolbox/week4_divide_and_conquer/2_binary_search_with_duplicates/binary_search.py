def binary_search(keys, query):
    low_index = 0
    high_index = len(keys) - 1
    while low_index <= high_index:
        mid_index = ((high_index + low_index) // 2)
        if query == keys[mid_index]:
            if mid_index - 1 < 0:
                return mid_index
            if query != keys[mid_index - 1]:
                return mid_index
            high_index = mid_index - 1
        elif query > keys[mid_index]:
            low_index = mid_index + 1
        elif query < keys[mid_index]:
            high_index = mid_index - 1
    return - 1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
