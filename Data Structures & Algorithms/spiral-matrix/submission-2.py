class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix[0]) == 1:
            return [num[0] for num in matrix]
        if len(matrix) == 1:
            return matrix[0]
            
        ans = [matrix[0][0]]
        idx = 0
        ways = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y = 0, 0
        lm, ln = len(matrix), len(matrix[0])
        path = set()
        while (x+ways[idx%4][0], y+ways[idx%4][1]) not in path:
            curr = idx % 4
            path.add((x, y))
            while 0 <= x+ways[curr][0] < lm and 0 <= y+ways[curr][1] < ln and (x+ways[curr][0], y+ways[curr][1]) not in path:
                x = x+ways[curr][0]
                y = y+ways[curr][1]
                ans.append(matrix[x][y])
                path.add((x, y))
            idx += 1

        return ans
