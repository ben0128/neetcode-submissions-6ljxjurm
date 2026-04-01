class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i , j = 0, n-1
        curr = 0
        while curr <= j:
            num = nums[curr]
            if num == 0:
                nums[curr], nums[i] = nums[i], nums[curr]
                i += 1
                curr += 1
            elif num == 2:
                nums[curr], nums[j] = nums[j], nums[curr]
                j -= 1
            else:
                curr += 1