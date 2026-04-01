import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # case 1: target < matrix[0][0] or target > matrix[-1][-1] => False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        rowIdx = bisect.bisect_left([row[-1] for row in matrix], target)
        row = matrix[rowIdx]

        j = bisect.bisect_left(row, target)
        return True if row[j] == target else False

        # case 2: find the number => True
        # case 3: can't find the number => False
