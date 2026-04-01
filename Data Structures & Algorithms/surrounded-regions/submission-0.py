class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def dfs(x, y):
            visited.add((x,y))
            for way in ways:
                newR = way[0] + x
                newC = way[1] + y
                if 0<= newR < row and 0 <= newC < col and board[newR][newC] == "O" and (newR, newC) not in visited:
                    dfs(newR, newC)


        # 左右側, (0, 0), (1, 0), (2, 0)...
        for currRow in range(row):
            if board[currRow][0] == 'O' and (currRow, 0) not in visited:
                dfs(currRow, 0)
            if board[currRow][col-1] == 'O' and (currRow, col-1) not in visited:
                dfs(currRow, col-1)
        
        # 上下側, (0, 0), (0, 1), (0, 2)...
        for currCol in range(col):
            if board[0][currCol] == 'O' and (0, currCol) not in visited:
                dfs(0, currCol)
            if board[row-1][currCol] == 'O' and (row-1, currCol) not in visited:
                dfs(row-1, currCol)

        for r in range(1, row-1):
            for c in range(1, col-1):
                if board[r][c] == "O" and (r,c) not in visited:
                    board[r][c] = "X"