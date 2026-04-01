class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin, currmax = 1, 1
        res = nums[0]

        for n in nums:
            currmin, currmax = min(n, n*currmin, n*currmax), max(n, n*currmin, n*currmax)
            res = max(currmax, res)
        return res
