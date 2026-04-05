class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        ways = [1, 0, -1, 0, 1]
        def dfs(r, c):
            grid[r][c] = 0
            area = 1

            for k in range(4):
                newR, newC = r+ways[k], c+ways[k+1]
                if 0 <= newR < m and 0 <= newC < n and grid[newR][newC] == 1: 
                    area += dfs(newR, newC)
            return area

        for i in range(m):
            row = grid[i]
            for j, cell in enumerate(row):
                if cell == 0:
                    continue
                ans = max(ans, dfs(i, j))
        return ans