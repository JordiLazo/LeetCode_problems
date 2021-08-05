'''
Hi, here's your problem today. This problem was recently asked by LinkedIn:

Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
count the number of islands present in the grid.

The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input:
10001
11000
10110
00000

Output: 3
'''
import collections


def numIslands(grid):
    if not grid:
        return 0
    rows,cols = len(grid), len(grid[0])
    visit = set()
    islands = 0

    def bfs(r,c):
        q = collections.deque()
        visit.add((r,c))
        q.append((r,c))
        while q:
            row,col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            for dr,dc in directions:
                r,c = row + dr, col + dc
                if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c))
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visit:
                bfs(r,c)
                islands += 1
    return islands


if __name__ == '__main__':
    grid = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0]]
    print(numIslands(grid))
    # 3
