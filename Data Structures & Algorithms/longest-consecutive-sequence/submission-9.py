class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return len(nums)
        
        numSet = set(nums)
        maxLen = 0

        for num in numSet:
            if num-1 not in numSet:
                tempLen = 1
                while num+tempLen in numSet: 
                    tempLen += 1
                maxLen = max(maxLen, tempLen)
        return maxLen

        
                

