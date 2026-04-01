class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for i in range(1, len(matrix)):
            x, y = i, i
            while x-1 >= 0:
                matrix[x-1][i], matrix[i][y-1] = matrix[i][y-1], matrix[x-1][i]
                x = x-1
                y = y-1

