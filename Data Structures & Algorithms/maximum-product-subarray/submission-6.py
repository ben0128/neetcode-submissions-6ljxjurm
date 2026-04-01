class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currmin, currmax = 1, 1
        res = -10

        for n in nums:
            temp = n*currmin
            currmin = min(n, n*currmin, n*currmax)
            currmax = max(n, temp, n*currmax)
            res = max(currmax, res)
        return res
