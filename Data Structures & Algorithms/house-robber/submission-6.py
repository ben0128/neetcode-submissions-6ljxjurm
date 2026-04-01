class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1]*len(nums)
        def recur(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            temp = max(recur(i+1), nums[i]+recur(i+2))
            memo[i] = temp
            return temp
        
        return recur(0)

