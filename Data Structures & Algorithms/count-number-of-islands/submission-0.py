class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        row = len(grid)
        column = len(grid[0])
        res = 0

        def dfs(r, c):
            grid[r][c] = '0'

            for way in ways:
                newR = r + way[0]
                newC = c + way[1]
                if 0 <= newR < row and 0 <= newC < column and grid[newR][newC] == '1':
                    dfs(newR, newC)

        for r in range(row):
            for c in range(column):
                point = grid[r][c]
                if point == '1':
                    dfs(r, c)
                    res += 1
        return res