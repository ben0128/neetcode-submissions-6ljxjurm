class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        ways = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(x, y):
            board[x][y] = "E"
            for way in ways:
                newR = way[0] + x
                newC = way[1] + y
                if 0<= newR < row and 0 <= newC < col and board[newR][newC] == "O":
                    dfs(newR, newC)


        # 左右側, (0, 0), (1, 0), (2, 0)...
        for currRow in range(row):
            if board[currRow][0] == 'O':
                dfs(currRow, 0)
            if board[currRow][col-1] == 'O':
                dfs(currRow, col-1)
        
        # 上下側, (0, 0), (0, 1), (0, 2)...
        for currCol in range(col):
            if board[0][currCol] == 'O':
                dfs(0, currCol)
            if board[row-1][currCol] == 'O':
                dfs(row-1, currCol)

        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"