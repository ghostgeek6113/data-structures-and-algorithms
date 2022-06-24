# def sum_numbers(array, target, k) -> list:
#     if (k > len(array)):
#         print(k)
#         return -1
#     current_sum = 0
#     for i in range(0, len(array)):
#         current_sum += array[i] + array[i + (k-1)]
#         # if(i >= k-1 ):
#         if (current_sum == target ):
#             print("index k:", k)
#             print("index i:", i)
#             print("index i-k+1:", i+k-1)
#             return [i+k-1, i]
#         # else:
#             # current_sum -= array[i-(k-1)]
#         return sum_numbers(array, target, k+1)

def sum_numbers_brute_force(array, target) -> list:
    current_sum = 0
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            if current_sum == target:
                return [i, j]
    return -1


def sum_numbers_efficient(array, target) -> list:
    values_map = {}
    for i in range(0, len(array)):
        current_sub = target - array[i]
        if current_sub in values_map:
            return [values_map[current_sub], i]
        else:
            values_map[array[i]] = i


num = [2, 7, 10, 15, 17, 21, 32, 4, 0, 6, 12]
target = 10
results1 = sum_numbers_brute_force(num, target)
results2 = sum_numbers_efficient(num, target)
print(sum_numbers_brute_force(num, target))
print(sum_numbers_efficient(num, target))
