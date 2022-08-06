def find_diagonal_order(mat):
    """
    Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
    """
    dictionary = {}
    results = []
    m = len(mat)
    n = len(mat[0])
    for i in range(m):
        for j in range(n):
            if i + j not in dictionary:
                dictionary[i + j] = [mat[i][j]]
            else:
                dictionary[i + j].append(mat[i][j])
    for item in dictionary.items():
        if item[0] % 2 == 0:
            [results.append(x) for x in item[1][::-1]]
        else:
            [results.append(x) for x in item[1]]

    return results


if __name__ == '__main__':
    print(find_diagonal_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
