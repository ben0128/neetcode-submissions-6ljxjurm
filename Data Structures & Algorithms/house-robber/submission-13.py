class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        r1, r2 = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            temp = max(nums[i]+r1, r2)
            r1 = r2
            r2 = temp

        return r2
                

