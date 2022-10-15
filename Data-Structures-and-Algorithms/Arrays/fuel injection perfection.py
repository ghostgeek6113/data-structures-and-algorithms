def solution(n):
    operation_count = 0
    n = int(n)
    while n > 1:
        # bitmask = *0
        if n % 2 == 0:
            n /= 2
        # bitmask = 01
        elif n == 3 or n % 4 == 1:
            n -= 1
        # bitsmask = 11
        else:
            n += 1
        operation_count += 1
    return operation_count


# def print_result(count, steps):
#     for i in steps:

print(solution('4'))
print(solution('15'))
print(solution('309'))
