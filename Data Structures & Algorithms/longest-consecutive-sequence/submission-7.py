class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        start = 0
        maxLen = 0
        for idx in range(len(nums)):
            if nums[idx]-1 not in nums:
                start = idx
            if nums[idx]+1 not in nums:
                maxLen = max(maxLen, nums[idx]-nums[start]+1)
        return maxLen
        
                

