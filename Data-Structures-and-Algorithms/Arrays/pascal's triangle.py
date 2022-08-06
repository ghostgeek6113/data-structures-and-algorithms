def generate(num_rows):
    """
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly
    :type num_rows: int
    :rtype: List[List[int]]
    """
    pascal_triangle = [None] * num_rows

    for i in range(num_rows):
        pascal_triangle[i] = [None] * (i + 1)
        pascal_triangle[i][0] = pascal_triangle[i][i] = 1

        for j in range(1, i):
            pascal_triangle[i][j] = pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]

    return pascal_triangle
