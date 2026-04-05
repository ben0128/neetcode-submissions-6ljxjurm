class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        # colSet = set()
        # diaSet1 = set() # row - col
        # diaSet2 = set() # col + row
        # (0, 0), (0, 1), (0, 2)
        # (1, 0), (1, 1), (1, 2)
        # (2, 0), (2, 1), (2, 2)
        def backtracing(path, colSet, diaSet1, diaSet2):
            row = len(path)
            if row == n:
                ans.append(path.copy())
                return
            
            for col in range(n):
                if col in colSet or row-col in diaSet1 or col+row in diaSet2:
                    continue
                # add
                path.append('.' * col + 'Q' + '.' * (n-col-1))
                colSet.add(col)
                diaSet1.add(row-col)
                diaSet2.add(col+row)

                backtracing(path, colSet, diaSet1, diaSet2)
                # discard
                path.pop()
                colSet.discard(col)
                diaSet1.discard(row-col)
                diaSet2.discard(col+row)
            return

        backtracing([], set(), set(), set()) 
        return ans