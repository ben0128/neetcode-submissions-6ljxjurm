class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            m = (l+r) // 2
            # 左邊有排序
            if nums[m] > nums[r]:
                l = m+1
            else: # 右邊有排序
                r = m
        return nums[l]