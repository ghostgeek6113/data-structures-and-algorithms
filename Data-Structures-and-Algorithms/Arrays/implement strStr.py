def str_str(haystack, needle):
    """
    Implement strStr(). Given two strings needle and haystack, return the index of the first occurrence of needle in
    haystack, or -1 if needle is not part of haystack.
    Clarification:
    What should we return when needle is an empty string? This is a great question to ask during an interview.
    For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
    and Java's indexOf(). :type haystack: str :type needle: str :rtype: int
    """
    # return haystack.find(needle)
    if needle == '':
        return 0
    else:
        return search_substring(haystack, needle)


def search_substring(haystack, needle):
    len_substring = len(needle)
    for i in range(len(haystack)):
        if haystack[i: i + len_substring] == needle:
            return i
    return -1
