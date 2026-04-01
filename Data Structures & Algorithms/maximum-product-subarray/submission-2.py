class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # min = -6
        # max = 2
        # curr = -6
        res = max(nums)
        curmin, curmax = 1, 1

        for n in nums:
            temp = curmin * n
            curmin = min(n, curmin*n, curmax*n)
            curmax = max(n, temp, curmax*n)
            res = max(res, curmax)
        return res