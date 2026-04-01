class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # remove duplicate
        numSet = set(nums)
        tmpLen = 0
        # 1,2,3  , 8,  11,12
        for num in numSet:
            if num-1 in numSet:
                continue
            curr = num
            while curr+1 in numSet:
                curr += 1
            tmpLen = max(tmpLen, curr-num+1)
        return tmpLen