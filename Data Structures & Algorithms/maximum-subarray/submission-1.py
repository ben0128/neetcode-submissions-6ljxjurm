class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = -float('inf')
        ansMax = -float('inf')

        for num in nums:
            currMax = max(num, currMax+num)
            ansMax = max(currMax, ansMax)
        return ansMax