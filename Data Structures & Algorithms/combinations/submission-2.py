class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrace(start, path):
            if len(path) == k:
                ans.append(path.copy())
                return
            
            for i in range(start, n+2-(k-len(path))):
                path.append(i)
                backtrace(i+1, path)
                path.pop()
            
        backtrace(1, [])
        return ans
        
# [1,2,3,4,5] k = 2

