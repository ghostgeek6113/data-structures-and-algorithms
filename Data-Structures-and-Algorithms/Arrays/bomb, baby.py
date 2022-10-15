def solution(m, f):
    # From the first look, what I can infer is that I basically have to find the number of subtractions that are
    # required to find the Greatest Common Divisor of M & F.
    m, f = int(m), int(f)
    generations = 0
    while m != 1 and f != 1:
        if m % f == 0:
            return "impossible"
        else:
            generations += int(max(m, f) / min(m, f))
            m, f = max(m, f) % min(m, f), min(m, f)
    return str(generations + max(m, f) - 1)


print(solution('2', '4'))
print(solution('20', '4'))
print(solution('2', '1'))
print(solution('4', '7'))
