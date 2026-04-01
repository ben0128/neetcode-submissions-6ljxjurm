class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax = 1, 1
        res = max(nums)
        for n in nums:
            temp = curmin * n
            curmin = min(n, curmin*n, curmax*n)
            curmax = max(n, temp, curmax*n)
            res = max(curmax, res)
        return max(curmax, res)