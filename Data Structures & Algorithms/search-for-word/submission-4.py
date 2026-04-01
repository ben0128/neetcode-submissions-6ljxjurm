class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ways = [(1, 0),(-1, 0),(0, 1),(0, -1)]
        wLastIdx = len(word)-1
        m, n, head = len(board), len(board[0]), word[0]

        def findWord(x, y, path):
            if board[x][y] != word[len(path)]:
                return False
            if len(path) == wLastIdx and board[x][y] == word[wLastIdx]:
                return True

            path.add((x, y))
            for row, col in ways:
                nR, nC = row+x, col+y
                if 0 <= nR < m and 0 <= nC < n and (nR, nC) not in path and findWord(nR, nC, path):
                    return True
            path.discard((x, y))
            return False
        
        
        for i in range(m):
            row = board[i]
            for j, cell in enumerate(row):
                if findWord(i, j, set()):
                    return True
        return False