class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [0] * 9
        block = [0] * 9

        for i in range(9):
            curr = 0
            row = board[i]
            for j in range(9):
                cell = row[j]
                if cell == '.':
                    continue
                num = int(cell)
                
                # row 
                if (curr >> num) & 1 == 1:
                    return False
                curr |= 1 << num
                
                # col
                if (col[j] >> num) & 1 == 1:
                    return False
                col[j] |= 1 << num

                # block
                idx = ((i // 3) * 3) + (j // 3)
                if (block[idx] >> num) & 1 == 1:
                    return False
                block[idx] |= 1 << num
        return True
                