def maxArea(height) -> int:
    current_area = 0
    for i in range(0, len(height)):
        for j in range(i + 1, len(height)):
            product = (j - i) * min(height[i], height[j])
            if current_area < product:
                current_area = product
    return current_area


def maxArea_optimized(height) -> int:
    maximum_area = 0
    left_pointer = 0
    right_pointer = len(height) - 1
    while left_pointer < right_pointer:
        width = right_pointer - left_pointer
        min_height = min(height[right_pointer], height[left_pointer])
        maximum_area = max(maximum_area, (width * min_height))
        if (height[left_pointer] < height[right_pointer]):
            left_pointer += 1
        else:
            right_pointer -= 1
    return maximum_area


print(maxArea_optimized([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# let’s see the two-pointer approach, here we need to first understand the problem, then need to check where we can start the pointers and how to move them.

# Here to calculate the most water contained, we need to consider the width as the x-axis distance between two verticle lines and the height, as the min height of the two verticle line.

# Now to get the maximum area we need to either maximize the width or maximize the height as we will get the maxArea by multiplying width and height.

# So here we will start with widest container means left will be 0 and right will be (height.length-1) and as we progress the width will be shorter so the only way to get the maximum area , we need to find out the maximum height.

# lets to see the steps :

# We will start with two pointers at the leftmost vertical lines, left and rightmost vertical lines, right. This is the widest container.
# We calculate the area and use that as a starting value for our maximum water containment
# We check which of the vertical lines is shortest, and we move the corresponding pointer closer to the other pointer – that way, even though we are making the container less wide, we have a better chance to make the container more tall
# We repeat this process while the left pointer is less than the right pointer, all the while keeping track of the max area we’ve seen.
# We return our tracked maximum.
