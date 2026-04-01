class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        def dfs(idx, currTotal):            
            if currTotal == 0:
                return True
            elif currTotal < 0 or idx == len(nums):
                return False

            return dfs(idx+1, currTotal) or dfs(idx+1, currTotal-nums[idx])
            
        return dfs(0, sum(nums)//2)
        

        