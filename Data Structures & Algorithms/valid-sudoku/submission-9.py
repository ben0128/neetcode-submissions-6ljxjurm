class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 上到下算一個column,共九個,每個column的c相同
        column = [(set()) for i in range(9)] 
        block = [(set()) for i in range(9)]
        def calBlockIdx(r,c):
            print(r,c)
            print((r // 3)*3 + (c // 3))
            return (r // 3)*3 + (c // 3);

        for r in range(9):
            rowSet = set()
            for c in range(9):
                if board[r][c] != ".":
                    oldLen = len(rowSet)
                    rowSet.add(board[r][c])
                    if (oldLen == len(rowSet)):
                        return False
                    oldLen = len(column[c])
                    column[c].add(board[r][c])
                    if oldLen == len(column[c]):
                        return False
                    blockIdx = calBlockIdx(r,c)
                    oldLen = len(block[blockIdx])
                    block[blockIdx].add(board[r][c])
                    if oldLen == len(block[blockIdx]):
                        return False
        return True

    


        