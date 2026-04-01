class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtracing(tmp, memo):
            if len(memo) == n:
                ans.append(tmp.copy())
                return 
            
            for k, num in enumerate(nums):
                if num in memo:
                    continue
                tmp.append(num)
                memo.add(num)
                backtracing(tmp, memo)
                tmp.pop()
                memo.discard(num)
            return
        
        backtracing([], set([]))
        return ans 