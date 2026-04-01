class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        half = total / 2
        def dfs(idx, currTotal, target):            
            currTotal += nums[idx]
            if currTotal == target:
                return True
                
            for j in range(idx+1, len(nums)):
                if nums[j] + currTotal == target:
                    return True
                if nums[j] + currTotal < target and dfs(j, currTotal, target):
                    return True
            return False
        return dfs(0, 0, half)
        

        