class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracing(l, r, tmp):
            if l < 0 or r < 0 or l > r:
                return
            if l == 0 and r == 0:
                ans.append(''.join(tmp))
                return
            #  2, 3
            #  1, 2
            nl, nr = l-1, r-1
            tmp.append('(')
            backtracing(nl, r, tmp)
            tmp.pop()
    
            tmp.append(')')
            backtracing(l, nr, tmp)
            tmp.pop()
            
            return

        backtracing(n, n, [])
        return ans