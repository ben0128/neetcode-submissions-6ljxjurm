class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()
        q = deque([])
        m, n = len(grid), len(grid[0])
        
        # 先紀錄起點位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))

        def markPoint(x, y, dis):
            nonlocal m, n
            if (x, y) not in visited and 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                visited.add((x,y))
                q.append((x,y))
                grid[x][y] = dis

        # 利用while 將q拿出一個後, 上下左右擴散
        distance = 1
        while q:
            for _ in range(len(q)):
                el = deque.popleft(q)
                markPoint(el[0]+1, el[1], distance)
                markPoint(el[0]-1, el[1], distance)
                markPoint(el[0], el[1]+1, distance)
                markPoint(el[0], el[1]-1, distance)
            distance += 1
        
