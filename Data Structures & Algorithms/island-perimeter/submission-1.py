class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            tmp = [(i, j)]
            # [(0, 0), (1, 0), (0, 1)]
            count = 0
            
            # [(1, 0), (0, 1)]
            while tmp:
                row, col = tmp.pop()
                if grid[row][col] == 2:
                    continue
                grid[row][col] = 2
                for addR, addC in ways:
                    nR, nC = row+addR, col+addC

                    if 0 <= nR < m and 0 <= nC < n:
                        if grid[nR][nC] == 1:
                            tmp.append((nR, nC))
                        elif grid[nR][nC] == 0:
                            count += 1
                    else: # 邊: (1) 超出範圍 (2) 遇到水
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)