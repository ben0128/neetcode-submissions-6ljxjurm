class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(grid), len(grid[0])
        
        def bfs(nodes):
            queue = deque(nodes)
            count = -1

            while queue:
                queueLen = len(queue)
                count += 1

                for _ in range(queueLen):
                    r, c = queue.popleft()

                    for wr, wc in ways:
                        nR, nC = r+wr, c+wc
                        if 0 <= nR < m and 0 <= nC < n and grid[nR][nC] == 2147483647:
                            grid[nR][nC] = grid[r][c] + 1
                            queue.append((nR, nC))
            return

        gates = []
        for i in range(m):
            row = grid[i]
            for j in range(n):
                cell = row[j]
                if cell == 0:
                    gates.append((i, j))
        bfs(gates)
        return 