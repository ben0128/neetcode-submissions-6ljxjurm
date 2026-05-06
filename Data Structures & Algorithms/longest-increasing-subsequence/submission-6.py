from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        tails = [nums[0]]
        for i in range(1, n):
            currNum = nums[i]
            insertIdx = bisect_left(tails, currNum)
            if len(tails) == insertIdx:
                tails.append(currNum)
            else:
                tails[insertIdx] = currNum
        return len(tails)