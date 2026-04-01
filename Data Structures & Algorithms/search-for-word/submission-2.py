class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        ways = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(row, column, path):
            if len(path) == n:
                return True
                
            for way in ways:
                newRow = row + way[0]
                newColumn = column + way[1]
                point = (newRow, newColumn)
                if -1 < newRow < len(board) and -1 < newColumn < len(board[0]) and board[newRow][newColumn] == word[len(path)] and point not in path:
                    path.add(point)
                    res = dfs(newRow, newColumn, path)
                    if res:
                        return True
                    path.discard(point)
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    res = dfs(r, c, set([(r, c)]))
                    if res:
                        return True
        return False