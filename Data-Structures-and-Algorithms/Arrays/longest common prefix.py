def longest_common_prefix(strs):
    """
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

    Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
    Explanation: There is no common prefix among the input strings.
    :type strs: List[str]
    :rtype: str
    """
    result = min(strs)
    for i in range(len(strs)):
        for j in range(len(result)):
            if strs[i][j] != result[j]:
                result = result[:j]
                break
    return result
