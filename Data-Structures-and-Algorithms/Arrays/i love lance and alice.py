def solution(s):
    lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    new_s = []
    for i in range(len(s)):
        if s[i] in lower:
            new_s.append(lower[25 - lower.index(s[i])])
        else:
            new_s.append(s[i])
    return ''.join(new_s)


print(solution("vmxibkgrlm"))
print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))
print(solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"))
