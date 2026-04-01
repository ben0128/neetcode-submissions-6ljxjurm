class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 上到下算一個column,共九個,每個column的c相同
        column = [(set()) for i in range(9)] 
        block = [(set()) for i in range(9)]

        for r in range(9):
            rowSet = set()
            for c in range(9):
                curr = board[r][c]
                if curr != ".":
                    idx = (r // 3)*3 + (c // 3)
                    if (curr in rowSet or
                       curr in column[c] or
                       curr in block[idx]):
                       return False
                    rowSet.add(curr)
                    column[c].add(curr)
                    block[idx].add(curr)
        return True

    


        