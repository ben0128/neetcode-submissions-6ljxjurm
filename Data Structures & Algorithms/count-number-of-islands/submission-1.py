class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ways = [1, 0, -1, 0, 1]
        m, n = len(grid), len(grid[0])
        def checkArea(row, col):
            grid[row][col] = '0'

            for k in range(4):
                newR, newC = row+ways[k], col+ways[k+1]
                if 0 <= newR < m and 0 <= newC < n and grid[newR][newC] == '1':
                    checkArea(newR, newC)

        ans = 0
        for i in range(m):
            currRow = grid[i]
            for j, cell in enumerate(currRow):
                if cell == '0':
                    continue
                checkArea(i, j)
                ans += 1

        return ans