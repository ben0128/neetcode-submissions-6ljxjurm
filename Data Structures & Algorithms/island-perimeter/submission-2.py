class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for addR, addC in ways:
                        nR, nC = i+addR, j+addC
                        if not (0 <= nR < m) or not (0 <= nC < n) or grid[nR][nC] == 0:
                            count += 1
        return count