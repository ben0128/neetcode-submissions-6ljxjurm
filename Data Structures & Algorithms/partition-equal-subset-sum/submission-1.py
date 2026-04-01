class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        def dfs(idx, currTotal, target):            
            if currTotal == target:
                return True
            elif currTotal > target or idx == len(nums):
                return False

            return dfs(idx+1, currTotal, target) or dfs(idx+1, currTotal+nums[idx], target)
            
        return dfs(0, 0, sum(nums)//2)
        

        