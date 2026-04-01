class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        rowZero = False
        colZero = False

        for r in range(R):
            if matrix[r][0] == 0:
                rowZero = True
                break

        for c in range(C):
            if matrix[0][c] == 0:
                colZero = True
                break
        
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if rowZero:
            for r in range(R):
                matrix[r][0] = 0

        if colZero:
            for c in range(C):
                matrix[0][c] = 0