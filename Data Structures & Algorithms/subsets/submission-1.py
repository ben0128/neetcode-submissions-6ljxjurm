class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        # [[], [1], [2], [1, 2]]
        
        for num in nums:
            n = len(dp)

            for i in range(n):
                el = dp[i]
                newLi = el.copy()
                newLi.append(num)
                dp.append(newLi)
        return dp

