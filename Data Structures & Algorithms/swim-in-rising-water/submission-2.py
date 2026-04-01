class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # (目前路線最大高度, row, col)
        minH = [(grid[0][0], 0, 0)] 

        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        n, m = len(grid), len(grid[0])

        def isInRange(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        visited = set()
        while minH:
            el = heapq.heappop(minH)
            if (el[1], el[2]) in visited:
                continue
            if el[1] == n-1 and el[2] == m-1:
                print('in', el)
                return el[0]
            visited.add((el[1], el[2]))

            for way in ways:
                newI = way[0]+el[1]
                newJ = way[1]+el[2]
                if not isInRange(newI, newJ):
                    continue
                if (newI, newJ) not in visited:
                    heapq.heappush(minH, (max(el[0], grid[newI][newJ]) , newI, newJ))

