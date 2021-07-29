'''
Hi, here's your problem today. This problem was recently asked by Amazon:

You are given a 2D array of characters, and a target string. Return whether or not the word target word exists in the matrix.
Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

Example:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

Given this matrix, and the target word FOAM, you should return true, as it can be found going up-to-down in the first column.
'''


def word_search(matrix, word):
    ROWS, COLS = len(matrix), len(matrix[0])
    path = set()

    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != matrix[r][c] or (r,c) in path):
            return False
        path.add((r,c))
        res = (dfs(r+1, c, i+1)) or (dfs(r-1, c, i+1)) or (dfs(r, c+1, i+1)) or (dfs(r, c-1, i+1))
        path.remove((r,c))
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r,c,0):
                return True
    return False


# Fill this in.
if __name__ == '__main__':

    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
    print(word_search(matrix, 'FACI'))
    # True
