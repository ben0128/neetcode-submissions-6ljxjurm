class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(i, j):
            tmp = [(i, j)]
            visited = set([(i, j)])
            # [(0, 0), (1, 0), (0, 1)]
            count = 0
            
            # [(1, 0), (0, 1)]
            while tmp:
                row, col = tmp.pop()
                for addR, addC in ways:
                    nR, nC = row+addR, col+addC
                    if 0 <= nR < m and 0 <= nC < n and grid[nR][nC] == 1:
                        if (nR, nC) not in visited:
                            tmp.append((nR, nC))
                            visited.add((nR, nC))
                    else: # 邊: (1) 超出範圍 (2) 遇到水 
                        count += 1
            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return bfs(i, j)