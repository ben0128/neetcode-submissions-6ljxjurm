class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        def bfs(row, col):
            count = 0
            tmp = deque([(row, col)])
            visited = set()
            while tmp:
                length = len(tmp)
                for _ in range(length):
                    popEl = tmp.popleft()
                    if popEl in visited:
                        continue
                    visited.add(popEl)
                    r, c  = popEl[0], popEl[1]
                    grid[r][c] = min(count, grid[r][c])
                    for i, j in ways:
                        nR, nC = r+i, c+j
                        if 0 <= nR < m and 0 <= nC < n and (nR, nC) not in visited and grid[nR][nC] != -1:
                            tmp.append((nR, nC))
                count += 1
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    bfs(row, col)
        return