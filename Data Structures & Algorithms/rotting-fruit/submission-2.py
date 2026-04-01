class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        r = len(grid)
        c = len(grid[0])
        ways = [(1,0), (-1,0), (0,1), (0,-1)]
        starts = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                elif grid[i][j] == 2:
                    grid[i][j] = 0
                    starts.append((i, j))
        if count == 0:
            return count

        ans = 0
        while len(starts) > 0:
            ans += 1
            n = len(starts)
            for idx in range(n):
                poped = starts.popleft()
                for way in ways:
                    nI = poped[0]+way[0]
                    nJ = poped[1]+way[1]
                    if 0 <= nI < r and 0 <= nJ < c and grid[nI][nJ] == 1:
                        grid[nI][nJ] = 2
                        count -= 1
                        if count == 0:
                            return ans
                        starts.append((nI, nJ))
        return -1 if count != 0 else ans