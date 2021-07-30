'''
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
'''


def matrix_spiral_print(matrix):
    if not matrix:
        return False
    rowbegin = 0
    rowend = len(matrix)
    columnbegin = 0
    columnend = len(matrix[0])
    res = []

    while rowend > rowbegin and columnend > columnbegin:
        for i in range(columnbegin,columnend):
            res.append(matrix[rowbegin][i])

        for j in range(rowbegin+1, rowend-1):
            res.append((matrix[j][columnend-1]))
        if rowend != rowbegin+1:
            for i in range(columnend-1, columnbegin-1, -1):
                res.append(matrix[rowend-1][i])
        if columnbegin != columnend-1:
            for j in range(rowend-2, rowbegin, -1):
                res.append(matrix[j][columnbegin])
        rowbegin += 1
        rowend -= 1
        columnbegin += 1
        columnend -= 1
    return res


if __name__ == '__main__':
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]

    print(matrix_spiral_print(grid))
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
