class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = [0]
        visited = set([tuple])
        ways = [(1, 0),(-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, count):
            print(r, c, count)
            visited.add((r, c))
            for way in ways:
                newRow = r+way[0]
                newCol = c+way[1]
                if 0 <= newRow < len(grid) and 0 <= newCol < len(grid[0]) and (newRow, newCol) not in visited and grid[newRow][newCol] == 1:
                    count[0] += 1
                    maxArea[0] = max(count[0], maxArea[0])
                    dfs(newRow, newCol, count)
            return 

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    maxArea[0] = max(1, maxArea[0])
                    dfs(r, c, [1])

        return maxArea[0]
                            
