class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin, currmax = 1, 1
        res = -10

        for n in nums:
            temp_min = min(n, n*currmin, n*currmax)
            temp_max = max(n, n*currmin, n*currmax)
            currmin, currmax = temp_min, temp_max
            res = max(currmax, res)
        return res
