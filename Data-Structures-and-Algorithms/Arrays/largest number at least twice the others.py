def dominent_index(nums):
    """
    You are given an integer array nums where the largest integer is unique.
    Determine whether the largest element in the array is at least twice as much as every other number in the array. If
    it is, return the index of the largest element, or return -1 otherwise.
    """

    max_index = 0
    maximum = 0
    for i in range(len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
            max_index = i
    for i in range(len(nums)):
        if i != max_index and maximum < 2 * nums[i]:
            return -1
    return max_index
