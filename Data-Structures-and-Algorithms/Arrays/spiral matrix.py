def spiral_order(matrix):
    """
    Given an m x n matrix, return all elements of the matrix in spiral order.
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
    results = []
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = n - 1
    top = 0
    bottom = m - 1
    while len(results) < m * n:
        for i in range(left, right + 1, 1):
            results.append(matrix[top][i])
            print(results)
        top += 1

        for i in range(top, bottom + 1, 1):
            results.append(matrix[i][right])
            print(results)
        right -= 1

        if left > right or top > bottom:
            break

        for i in range(right, left - 1, -1):
            results.append(matrix[bottom][i])
            print(results)
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            results.append(matrix[i][left])
        left += 1

    return results


if __name__ == '__main__':
    print(spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
