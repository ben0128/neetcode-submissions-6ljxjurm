class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        resMax = 1
        m, n = len(matrix), len(matrix[0])
        cellDis = [[1] * n for _ in range(m)] 
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            nonlocal m, n, resMax
            tmp = deque([(r, c)])
            while tmp:
                i, j = tmp.popleft()
                for x, y in ways:
                    nR = x+i
                    nC = y+j
                    if 0<= nR < m and 0 <= nC < n and matrix[nR][nC] > matrix[i][j] and cellDis[nR][nC] < cellDis[i][j]+1:
                        cellDis[nR][nC] = cellDis[i][j]+1
                        resMax = max(resMax, cellDis[i][j]+1)
                        tmp.append((nR, nC))

        for i in range(m):
            for j in range(n):
                isBfs = True
                for x, y in ways:
                    nR = x+i
                    nC = y+j
                    if 0<= nR < m and 0 <= nC < n and matrix[nR][nC] < matrix[i][j] and cellDis[nR][nC] == 1:
                        isBfs = False
                        continue
                        
                if isBfs:
                    bfs(i, j)

        return resMax