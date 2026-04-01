class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) // 2
        if sum(nums) % 2 != 0:
            return False
        
        memo = set([0, nums[0]])
        if target in memo:
            return True

        for idx in range(1, len(nums)):
            memo.update([ nums[idx]+el for el in memo])
            if target in memo:
                return True
        return False

