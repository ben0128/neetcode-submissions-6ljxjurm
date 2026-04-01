class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            maxIdx = -1
            for idx in range(l, r+1):
                maxIdx = max(nums[idx]+idx, maxIdx)
            l = r+1
            r = maxIdx
            res += 1
        return res
