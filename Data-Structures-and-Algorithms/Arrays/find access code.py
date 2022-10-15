def solution(l):
    # solution: https://randomds.com/2022/02/18/google-foobar-challenge-level-3-find-the-access-codes/
    if len(l) < 3:
        return 0
    triplets = [0] * len(l)
    triplets_count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                triplets[i] = triplets[i] + 1
                triplets_count += triplets[j]
    return triplets_count


print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 1, 1]))
